#target photoshop

// Function to prompt the user for the output folder
function getOutputFolder() {
    var outputFolder = Folder.selectDialog("Select the folder to save PNG files");
    if (outputFolder == null) {
        alert("No folder selected. Operation cancelled.");
        exit();
    }
    return outputFolder;
}

// Function to sanitize file/folder names
function sanitizeName(name) {
    // Remove illegal characters
    return name.replace(/[\\\/\:\*\?\"\<\>\|]/g, "_");
}

// Function to map DocumentMode to NewDocumentMode
function getNewDocumentMode(docMode) {
    switch (docMode) {
        case DocumentMode.BITMAP:
            return NewDocumentMode.BITMAP;
        case DocumentMode.GRAYSCALE:
            return NewDocumentMode.GRAYSCALE;
        case DocumentMode.RGB:
            return NewDocumentMode.RGB;
        case DocumentMode.CMYK:
            return NewDocumentMode.CMYK;
        case DocumentMode.LAB:
            return NewDocumentMode.LAB;
        default:
            // Default to RGB if mode is unsupported
            return NewDocumentMode.RGB;
    }
}

// Function to save the target layer as PNG with alpha
function saveLayerAsPNG(doc, layer, outputPath) {
    // Map the document mode to NewDocumentMode
    var newDocMode = getNewDocumentMode(doc.mode);

    // Create a new temporary document with the same dimensions and settings
    var tempDoc = app.documents.add(doc.width, doc.height, doc.resolution, "TempDoc", newDocMode, DocumentFill.TRANSPARENT);

    // Ensure the original document is active before duplicating
    app.activeDocument = doc;

    // Duplicate the target layer to the new document
    layer.duplicate(tempDoc, ElementPlacement.PLACEATBEGINNING);

    // Ensure the temp document is active
    app.activeDocument = tempDoc;

    // Save options
    var pngOptions = new PNGSaveOptions();
    pngOptions.compression = 9; // Adjust compression if needed (0-9)
    pngOptions.interlaced = false;

    // Save the file
    var file = new File(outputPath);
    tempDoc.saveAs(file, pngOptions, true, Extension.LOWERCASE);

    // Close the temp document without saving
    tempDoc.close(SaveOptions.DONOTSAVECHANGES);

    // Ensure the original document is active
    app.activeDocument = doc;
}

// Function to traverse layers and save them
function processLayers(doc, layers, parentGroupPath) {
    for (var i = layers.length - 1; i >= 0; i--) {
        var layer = layers[i];
        if (layer.typename == "LayerSet") {
            // Create subfolder for the group
            var groupName = sanitizeName(layer.name);
            var groupPath = parentGroupPath + "/" + groupName;
            var folder = new Folder(outputFolder.fsName + groupPath);
            if (!folder.exists) folder.create();

            // Recursively process the group's layers
            processLayers(doc, layer.layers, groupPath);
        } else if (
            layer.kind == LayerKind.NORMAL ||
            layer.kind == LayerKind.SOLIDFILL ||
            layer.kind == LayerKind.GRADIENTFILL ||
            layer.kind == LayerKind.PATTERNFILL ||
            layer.kind == LayerKind.SMARTOBJECT ||
            layer.kind == LayerKind.TEXT ||
            layer.kind == LayerKind.VIDEO ||
            layer.kind == LayerKind.LAYER3D
        ) {
            var layerName = sanitizeName(layer.name);
            var outputPath = outputFolder.fsName + parentGroupPath + "/" + layerName + ".png";
            saveLayerAsPNG(doc, layer, outputPath);
        }
    }
}

// Main script execution
if (app.documents.length === 0) {
    alert("No documents are open.");
    exit();
}

var doc = app.activeDocument;

// Prompt the user to select the output folder
var outputFolder = getOutputFolder();

// Start processing layers from the root
processLayers(doc, doc.layers, "");

// Notify the user when done
alert("Layers have been saved as PNG files.");

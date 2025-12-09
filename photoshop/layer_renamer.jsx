#target photoshop

// Function to get selected layers without grouping/ungrouping
function getSelectedLayers() {
    var selectedLayers = [];
    var ref = new ActionReference();
    ref.putProperty(stringIDToTypeID("property"), stringIDToTypeID("targetLayersIDs"));
    ref.putEnumerated(stringIDToTypeID("document"), stringIDToTypeID("ordinal"), stringIDToTypeID("targetEnum"));
    var desc = executeActionGet(ref);
    if (desc.hasKey(stringIDToTypeID("targetLayersIDs"))) {
        var list = desc.getList(stringIDToTypeID("targetLayersIDs"));
        for (var i = 0; i < list.count; i++) {
            var id = list.getReference(i).getIdentifier();
            var layer = getLayerByID(id, app.activeDocument);
            if (layer != null) {
                selectedLayers.push(layer);
            }
        }
    } else {
        selectedLayers.push(app.activeDocument.activeLayer);
    }
    return selectedLayers;
}

// Recursive function to find a layer by its ID
function getLayerByID(id, parent) {
    for (var i = 0; i < parent.layers.length; i++) {
        var layer = parent.layers[i];
        if (layer.id == id) {
            return layer;
        } else if (layer.typename == "LayerSet") {
            var foundLayer = getLayerByID(id, layer);
            if (foundLayer != null) {
                return foundLayer;
            }
        }
    }
    return null;
}

// Function to pad numbers with leading zeros
function padNumber(num, size) {
    var s = num + "";
    while (s.length < size) s = "0" + s;
    return s;
}

// Main script execution
if (app.documents.length === 0) {
    alert("No documents open.");
    exit();
}

var selectedLayers = getSelectedLayers();

if (selectedLayers.length === 0) {
    alert("No layers selected.");
    exit();
}

// **Optional:** Reverse the order of selected layers if needed
// selectedLayers.reverse();

// Prompt user for base name
var baseName = prompt("Enter base name for layers:", "layer");
if (baseName === null) exit();

// Prompt user for number of digits for padding
var paddingInput = prompt("Enter number of digits for padding (e.g., 3 for 001):", "3");
if (paddingInput === null) exit();
var padding = parseInt(paddingInput, 10);
if (isNaN(padding) || padding < 0) {
    alert("Invalid number of digits.");
    exit();
}

// Rename the selected layers
for (var i = 0; i < selectedLayers.length; i++) {
    var number = padNumber(i + 1, padding);
    selectedLayers[i].name = baseName + number;
}

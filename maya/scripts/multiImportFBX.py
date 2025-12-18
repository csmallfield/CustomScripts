import maya.cmds as cmds
import os

def batch_import_files():
    # Open file browser with multi-select
    file_paths = cmds.fileDialog2(
        fileMode=4,
        caption="Select Files to Import",
        fileFilter="FBX Files (*.fbx);;OBJ Files (*.obj);;All Files (*.*)",
        dialogStyle=2
    )
    
    if not file_paths:
        print("No files selected.")
        return
    
    # Import each file
    imported_count = 0
    for file_path in file_paths:
        try:
            # Get filename for naming
            filename = os.path.splitext(os.path.basename(file_path))[0]
            
            # Import and get the new nodes
            imported_nodes = cmds.file(file_path, i=True, type="FBX", ignoreVersion=True, 
                                      returnNewNodes=True)
            
            # Get top-level transforms (parent nodes)
            transforms = [node for node in imported_nodes if cmds.nodeType(node) == 'transform' 
                         and not cmds.listRelatives(node, parent=True)]
            
            # Rename top-level objects with the filename
            for j, transform in enumerate(transforms):
                new_name = f"{filename}_{j}" if len(transforms) > 1 else filename
                cmds.rename(transform, new_name)
                print(f"  Renamed: {transform} -> {new_name}")
            
            print(f"Imported: {filename}")
            imported_count += 1
            
        except Exception as e:
            print(f"Failed to import {file_path}: {str(e)}")
    
    print(f"\nBatch import complete! Imported {imported_count} of {len(file_paths)} files.")

# Run the function
batch_import_files()
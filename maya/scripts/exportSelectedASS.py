import maya.cmds as cmds
import os

def export_selected_to_ass():
    """
    Export selected objects/groups to individual .ass files
    """
    # Check if Arnold plugin is loaded
    if not cmds.pluginInfo('mtoa', query=True, loaded=True):
        try:
            cmds.loadPlugin('mtoa')
        except:
            cmds.warning("Could not load Arnold plugin (mtoa)")
            return
    
    # Get selection
    selection = cmds.ls(selection=True, long=True)
    
    if not selection:
        cmds.warning("Nothing selected. Please select objects or groups to export.")
        return
    
    # File dialog to choose export location
    export_dir = cmds.fileDialog2(
        fileMode=3,  # Directory mode
        caption="Choose Export Directory for .ass Files",
        okCaption="Export Here"
    )
    
    if not export_dir:
        return  # User cancelled
    
    export_dir = export_dir[0]
    
    # Store original selection to restore later
    original_selection = selection[:]
    
    exported_files = []
    
    # Process each selected item
    for obj in selection:
        # Get short name for filename (without path)
        short_name = obj.split('|')[-1]
        
        # Clean name for filename (remove special characters)
        clean_name = short_name.replace(':', '_').replace('|', '_')
        
        # Create output filepath
        output_file = os.path.join(export_dir, clean_name + '.ass')
        
        # Select only this object/group for export
        cmds.select(obj, replace=True)
        
        # Export to .ass using Arnold
        try:
            # Arnold standalone export command
            cmds.arnoldExportAss(
                filename=output_file,
                selected=True,
                shadowLinks=True,
                mask=24,  # AI_NODE_SHAPE | AI_NODE_SHADER
                lightLinks=True,
                compressed=False,
                boundingBox=True
            )
            exported_files.append(output_file)
            print("Exported: {}".format(output_file))
            
        except Exception as e:
            cmds.warning("Failed to export {}: {}".format(short_name, str(e)))
    
    # Restore original selection
    cmds.select(original_selection, replace=True)
    
    # Summary message
    if exported_files:
        cmds.confirmDialog(
            title="Export Complete",
            message="Successfully exported {} .ass file(s) to:\n{}".format(
                len(exported_files), 
                export_dir
            ),
            button="OK"
        )
    else:
        cmds.warning("No files were exported.")

# Run the function
export_selected_to_ass()
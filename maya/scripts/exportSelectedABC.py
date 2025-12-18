import maya.cmds as cmds
import os

def export_selected_to_abc():
    """
    Export selected objects/groups to individual .abc files (static geometry)
    """
    # Check if Alembic plugin is loaded
    if not cmds.pluginInfo('AbcExport', query=True, loaded=True):
        try:
            cmds.loadPlugin('AbcExport')
        except:
            cmds.warning("Could not load Alembic plugin (AbcExport)")
            return
    
    # Get selection
    selection = cmds.ls(selection=True, long=True)
    
    if not selection:
        cmds.warning("Nothing selected. Please select objects or groups to export.")
        return
    
    # File dialog to choose export location
    export_dir = cmds.fileDialog2(
        fileMode=3,  # Directory mode
        caption="Choose Export Directory for .abc Files",
        okCaption="Export Here"
    )
    
    if not export_dir:
        return  # User cancelled
    
    export_dir = export_dir[0]
    
    exported_files = []
    
    # Process each selected item
    for obj in selection:
        # Get short name for filename (without path)
        short_name = obj.split('|')[-1]
        
        # Clean name for filename (remove special characters)
        clean_name = short_name.replace(':', '_').replace('|', '_')
        
        # Create output filepath and normalize to forward slashes (Maya prefers these)
        output_file = os.path.join(export_dir, clean_name + '.abc').replace('\\', '/')
        
        # Build Alembic export command for static geometry
        try:
            # Export single frame (current frame) with geometry data
            export_command = '-frameRange 1 1 -uvWrite -worldSpace -writeVisibility -autoSubd -writeUVSets -writeColorSets -writeFaceSets -dataFormat ogawa -root {} -file "{}"'.format(
                obj,
                output_file
            )
            
            cmds.AbcExport(jobArg=export_command)
            exported_files.append(output_file)
            print("Exported: {}".format(output_file))
            
        except Exception as e:
            cmds.warning("Failed to export {}: {}".format(short_name, str(e)))
    
    # Summary message
    if exported_files:
        cmds.confirmDialog(
            title="Export Complete",
            message="Successfully exported {} static .abc file(s) to:\n{}".format(
                len(exported_files), 
                export_dir
            ),
            button="OK"
        )
    else:
        cmds.warning("No files were exported.")

# Run the function
export_selected_to_abc()
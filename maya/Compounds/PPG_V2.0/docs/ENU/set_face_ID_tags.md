# Set Faces ID Tags
Set the face tags base of the face ID.<br>
The resulting tags are numbers (the face ID) with an optional prefix.

## Inputs

### Mesh
The input geometry.

### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh for the cutting.<br>
You can use \* in the names as a wildcard.

### Face Indices
A list of numbers (uint) of faces to use for the cutting.

### Invert
After adding the faces from tag expressions and indices together this will invert the selection to all other faces of the mesh.
This flag is also helpful if there are not face tags in the object.

## Tag Prefix Postfix
### Tag Prefix
Prefix for the new tag.<br>

### Tag Postfix
Postfix for the new tag.<br>

### Store as Reference
NOTE: A prefix is necessary to use this option.<br>
If this option in turned ON the points of the selected faces and their unique face tags are stored in the object for later use.<br>
The goal is to store information about the size and orientation of these faces for later use. The descendants of these faces can later access this information in the node "PPG_multi_cut".

## Tutorial

<br><br>

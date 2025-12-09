# Assign Material to Tags
Splits the selectd faces off the object and assigns a material reference.<br>
Outputs the new faces with material reference and the remaining rest object.

## Face Selection

### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh for the instancing.<br>
You can use \* in the names as a wildcard.

### Face Indices
A list of numbers (uint) of faces to use for the instancing.

### Invert
After adding the faces from tag expressions and indices together this will invert the selection to all other faces of the mesh.
This flag is also helpful if there are not face tags in the object.

## Material

### Material Name
Name of the material to reference.

## Output

### Faces with Material
Just the selected faces with that material reference.

### Remaining Faces
The rest of the object.


# Select Faces inside Mesh
Filters given faces by their position inside/outside of a mesh.

## Inputs

### Mesh
The input geometry.

### Select Mesh
The selection geometry.<br>
Faces are returned whose center is INSIDE the select mesh.


### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh for this operation.<br>
You can use \* in the names as a wildcard.

### Face Indices
A list of numbers (uint) of faces to use for this operation.

### Invert
After adding the faces from tag expressions and indices together this will invert the selection to all other faces of the mesh.
This flag is also helpful if there are not face tags in the object.


### Invert Output
Invert the output.

## Output

### Face Tag
 Assign this new face tag to the output faces.

## Tutorial
https://youtu.be/T8PXtWaS4GM
<br><br>

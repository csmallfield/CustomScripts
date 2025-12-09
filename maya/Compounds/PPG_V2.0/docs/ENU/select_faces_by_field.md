# Select Faces by Field
Select faces using a field.

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

## Selection

### Scalar Field
Plug in a scalar field.<br>
The field strength at the center of the face determins if the face is selected.

### Threshold
Min field strength to trigger.

### Invert Output
Invert the output.

## Output

### Face Tag
 Assign this new face tag to the output faces.

## Tutorial
https://youtu.be/T8PXtWaS4GM
<br><br>

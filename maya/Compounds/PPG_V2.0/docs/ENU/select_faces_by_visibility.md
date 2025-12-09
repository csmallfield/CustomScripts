# Select Faces by Normal
Filters given faces by their visibility from given viewpoints.

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

### Viewpoint
A single point or an array of points.<br>
Faces are selected if they can be "seen" from any of these viewpoints given the Goal Angle and the Tolerance Angle.

### Goal Angle
Looking for faces with this angle between the face normal and the vector *viewpoint-faceCenter*.
- ***0*** = Looking for faces normals that point at the viewpoint.
- ***180*** = Looking for faces normals that point in the opposite direction.

### Tolerance Angle
Tolerance for "Goal" in Euler degrees.
- ***0*** = Looking for normals that match EXACTLY the Goal Angle.
- ***90*** = All normals that are facing the viewpoint somehow.
- ***>90*** = Even those normals that point AWAY from the viewpoints.

### Front and Back Sides
Returns Also the opposite sides.

### Invert Output
Inverts the output.

## Output

### Face Tag
 Assign this new face tags to the output faces.

## Tutorial
https://youtu.be/T8PXtWaS4GM
<br><br>

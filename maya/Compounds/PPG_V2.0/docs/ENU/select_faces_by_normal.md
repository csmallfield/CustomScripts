# Select Faces by Normal
Filters given faces by their normal.

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

### Vector
The normal direction to look for.<br>
Measures the cosine of the angle between the face normal and the "Vector".

### Goal Angle
Looking for faces with this angle between the face normal and the vector above.
- ***0*** = Looking for face normals that point in the same direction as "Vector".
- ***45*** = Looking for face normals that are 45 degrees from "Vector".
- ***90*** = Looking for faces normals that are perpendicular (90 degrees) to "Vector".
- ***180*** = Looking for faces normals that point in the opposite direction.

### Tolerance Angle
Tolerance for "Goal" in Euler degrees.

### Front and Back Sides
Returns matches for +Goal and -Goal.

### Invert Output
Inverts the output.

## Output

### Face Tag
 Assign this new face tags to the output faces.

## Tutorial
https://youtu.be/T8PXtWaS4GM
<br><br>

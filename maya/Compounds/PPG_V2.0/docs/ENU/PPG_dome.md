# PPG Dome
Creates a multi segment extrude on selected faces.<br>
Lets you create domes or bulbous spires.

## Tutorial
https://youtu.be/QrLejJWs9CQ
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Settings

### Distance
Height of the dome.<br>
Accepts also an array with individual settings per source face.

### Subdivisions
Number of subdivisions.

### Rotation
Total rotation (degrees) of the subdivisions around the normal of the source face.<br>
Accepts also an array with individual settings per source face.

### Scale
This curve defines the profile of the dome.

### Move in X
### Move in Z
Move the subdivisions in two directions across the face.<br>
The directions are related to the selected edge of the face.<br>
A value of "1" moves all subdivisions to the respective side.

## Tags

Which tags to assign to the resulting polygons.<br>
HINT: face tags can be displayed using the PPG_diagnostic

### Inherit Source Tag
Adds the name of the source face to the resulting tag name.

### Face Tag
Name of all faces of the new dome.<br>
Hint: you could create a unique name for all source faces with "set_face_ID_tags" and end up with unique face tags for each dome.

## Output

### Merge Vertices
Merge vertices after the extrude.

### Tolerance
Tolerance.



## Tutorial
https://youtu.be/QrLejJWs9CQ
<br><br>

# PPG Arch
Builds an arch on every selected face (equiangular planar quads only).

## Tutorial
https://youtu.be/qBa-USPoIrc
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Settings

### Number of Points
This sets the number of points/faces for one half of the arch. The total number will always be an even number.

### Pointed
Turns the regular round arch into a pointed arch.<br>
Accepts also an array with individual settings per source face.

### Segment
Turns the arch into a segmental arch.<br>
Accepts also an array with individual settings per source face.

### Vertical Scale
Scales the arch vertically.<br>
Accepts also an array with individual settings per source face.<br><br>

### Extrude
Extrude the arch portal.

### Extrude Depth
Extrude depth for the arch portal.<br>
Accepts also an array with individual settings per source face.

### With Offset
Adds an offset on all four sides of the arch.<br>
Without the offset there will be some triangles around the arch.

### Relative
The offset values below are relative to the size of the source polygon.

### Horizontal Offset
Offset on both sides of the arch.

### Vertical Offset
Offset above and below the arch.

## Tags

Which tags to assign to the resulting polygons.<br>
HINT: face tags can be displayed using the PPG_diagnostic

### Inherit Source Tag
Adds the name of the source face to the resulting tag name.

### Arch Roof
Tag name for the faces above the arch.

### Arch Portal
Tag name for the arch "door".

### Arch Extrude
Tag name for the extrude sides if there is an extrude.

## Diagnostic
Position, size and color of an arrow that indicates the selected edge for every selected face.
The arrows can be turned on/off with the terminal switch on the node.




## Tutorial
https://youtu.be/qBa-USPoIrc
<br><br>

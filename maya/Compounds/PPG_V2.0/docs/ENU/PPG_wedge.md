# PPG Wedge
Creates a wedge from selected faces around their selected edges.

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Settings

### Degrees
Rotation of the face around the selected edge.<br>
Accepts also an array with individual settings per source face.

### Division
Number of divisions for the wedge.

## Tags

### Inherit Source Tags
Inherit the tag name of the face that this wedge is based on.

### Wedge Front
### Window
### Wedge Sides
New tags for the parts of the wedge.

## Output

### Merge Vertices
### Radius
After the transformation run a "Merge Vertices" operation.

## Diagnostic
The diagnostic display can be turned on/off with the terminal switch on the node.<br>

Set the position, size and color of an arrow that indicates the selected edge for every selected face.


## Tutorial

<br><br>

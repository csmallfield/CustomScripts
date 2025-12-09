# PPG Transform
Transforms selected faces or their selected edges.

## Tutorial
https://youtu.be/ziB6cBu8u6w
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Transform

### Transform Mode
Faces, Edges or Face Tag Groups.

- "Faces" will transform individual faces in their local space. The normal is the Y-axis, the selected edge is the Z-axis.
- "Edges" will transform only the selected edges in the local space of their respective face.
- "Face Tag Groups" will group faces with the same face tag and transform the whole group in GLOBAL space. You can set the pivot for each group by providing an array for "Pivot Position" and "Pivot Rotation".


### Pivot on Edge
Availabe for modes "Faces" and "Edges".<br>
Slide the pivot along the edges of the polygon. One unit equals one edge.<br>
Stops at the end of the last edge.

### Pivot in Center
Availabe for mode "Faces".<br>
Move the pivot towards the center of the polygon.<br><br>
Turn on the diagnostic display to see the pivots.<br>

### Pivot Position
### Pivot Rotation
Available for mode "Face Tag Groups".
Set the pivot position and rotation.<br>
If these ports are SINGLE values then the position is meant to be relative to the group's bounding box (0.5,0.5,0.5 is the center of the BB).<br>
The ports will also accept ARRAYS with individual settings for each face tag group.<br>

### Translate
### Rotate
### Scale
Transform settings for the selected faces/edges/groups.<br>
Accepts also an array with individual settings per face/edge/group.


## Output

### Merge Vertices
### Radius
After the transformation run a "Merge Vertices" operation.

## Diagnostic
The diagnostic display can be turned on/off with the terminal switch on the node.

### Selected Edge
Position, size and color of an arrow that indicates the selected edge for every selected face.

### Pivot
Display a pivot axis for placement and orientation.<br>


## Tutorial
https://youtu.be/ziB6cBu8u6w
<br><br>

# Get Face Info
Outputs information about the selected faces.

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## Face Selection

### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh for the transformation.<br>
You can use \* in the names as a wildcard.

### Face Indices
A list of numbers (uint) of faces to use for the transformation.

### Invert
After adding the faces from tag expressions and indices together this will invert the selection to all other faces of the mesh.
This flag is also helpful if there are not face tags in the object.


## Edge Selection
By procedurally selecting an edge of every face we can give the operation a sense of direction.

### Direction Method
There are three different methods:
+ In a direction seen from the center of the face
+ By edge length (longest/shortest)
+ By point index
+ Best alignment with the direction vector

### Direction Vector
This will select the edge that would lie in the direction of that vector seen from the center of the respective face.

### Point Index
Selects the edge starting at the specified point index

### Next Edge
Selects the NEXT edge instead the current one. The order of edges in counter clockwise.
This is basically a +1 operation.

### Opposite Edge
Selects the OPPOSITE edge instead the current one.
This is basically a +2 operation.<br>

If both flags „Next“ and „Opposite“ are checked this results in a +3 operation, or a „Previous Edge“ from the current one in a quad.<br>

A red arrow can be displayed close to the selected edge as a hint.
There are some settings for the red arrow in the section „Diagnostics“.

## Pivot

### Pivot Mode
Faces or Edges.<br>

- "Faces" will get the pivots of the faces in their local space. The normal is the Y-axis, the selected edge is the Z-axis.
- "Edges" will get the pivots of the edges in the local space of their respective face.


### Pivot on Edge
Slide the pivot along the edges of the polygon. One unit equals one edge.<br>
Stops at the end of the last edge.

### Pivot in Center
Availabe for mode "Faces".<br>
Move the pivot towards the center of the polygon.<br><br>
Turn on the diagnostic display to see the pivots.<br>

## Diagnostic
The diagnostic display can be turned on/off with the terminal switch on the node.

### Selected Edge
Position, size and color of an arrow that indicates the selected edge for every selected face.

### Pivot
Display a pivot axis for placement and orientation.<br>


## Tutorial

<br><br>

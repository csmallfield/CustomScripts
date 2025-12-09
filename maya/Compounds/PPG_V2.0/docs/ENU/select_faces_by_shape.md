# Select Faces by Shape
Filters given faces by their properties.

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
This flag is also helpful if there are no face tags in the object.

## Selection

## 1. Pass: Number of Edges
### Triangles
### Quads
### N-Sided
Filters the given faces by the number of edges.

## 2. Pass: Equal Angles and Edge Lengths

### Equiangular
Lets only those faces pass that have equal angles in all corners.

### Equilateral
Lets only those faces pass that have equal length of all edges.

## 3. Pass: Convexity

### Concave
Lets concave faces pass.

### Convex
Lets convex faces pass.

## 4. Pass: Planarity

### Planar
Lets planar faces pass.

### Non-Planar
Lets non-planar faces pass.

### Invert Output
Invert the output.

## Output
### Inherit Source Tag
Adds the name of the source face to the resulting tag name.

### Face Tag
Assign this new face tag to the output faces.

## Tutorial
https://youtu.be/T8PXtWaS4GM
<br><br>

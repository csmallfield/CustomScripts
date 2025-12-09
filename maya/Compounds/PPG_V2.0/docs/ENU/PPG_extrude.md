# PPG Multi Cut
Extrude selected faces.<br>
Many thanks to user "HeyUU" of the Bifrost Addicts community on Discord for this extrude in PPG1.0 and for some cool code in PPG2.0.

## Tutorial
https://youtu.be/BdvCPVC1TuA
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## Face Selection

### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh for the extrude.<br>
You can use \* in the names as a wildcard.

### Face Indices
A list of numbers (uint) of faces to use for the extrude.

### Invert
After adding the faces from tag expressions and indices together this will invert the selection to all other faces of the mesh.
This flag is also helpful if there are not face tags in the object.

## Geometry

### Extrude Depth
Depth for the extrusion.<br>
Accepts also an array with individual settings per `island`.<br><br>

The extrude depth can also be set with a property "extrude_depth" that can be a point_component, a face_component, or a face_vertex_component.

### Offset
Offset from the edges.<br>
Positive values make the extrude face smaller.

### Depth Vector Type
- `Point Normal`  simply moves the extruded points along the average point normal
- `Thickness` keeps the resulting faces parallel to the source faces

### Keep Faces Together
Keep neighboring faces together.

### Do Only Chip Off
Does not produce the side faces of the extrude.<br>
If you turn off "Delete Source Faces" you have a proper Chip-Off.

### Source Face Mode
What to do with the source faces:
- `Delete`
- `Keep`
- `Reverse`

## Tags

Which tags to assign to the resulting polygons.<br>
HINT: face tags can be displayed using the PPG_diagnostic

### Inherit Source Tag
Adds the name of the source face to the resulting tag name.

### Extrude Tag
New name for the extruded faces.

### Side Face Tag
Tag for the side faces.<br>

## Output

### Merge Vertices
Merge vertices after the operation.

### Tolerance
Tolerance.


## Tutorial
https://youtu.be/BdvCPVC1TuA
<br><br>

# PPG Multi Cut
Cuts selected quad polygons into strips with an odd/even pattern.

## Tutorial
https://youtu.be/X-6NRl1QD0Y
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Settings

### Mode
+ Double: An „Outer“ strip on both ends of the polygon.
+ Half: The „Outer“ strips at the ends are only half size.
+ Start/End: Just one „Outer“ at the specified end.
+ None: No „Outer“ strips at the ends.

### Outer Size
Sets the size of the „even“ strips.<br>
Accepts also an array with individual settings per source face.

### Inner Size
Sets the size of the „odd“ strips.<br>
Accepts also an array with individual settings per source face.

### Flexible
Sets which kind of strips is flexible in size.
+ Inner
+ Outer
+ Both
+ None

## Cut Settings

### Cutting Method
**Relative (Quads only)** is the easy and fast method.<br>
Only quads will be cut. The subdivisions happen on the selected edge and will be projected across the polygon to the opposite side. If the sides have different lengths the the subdivisions will refelct that.<br><br>
**Projection** is the newer and slower method.<br>
This method cuts any polygon - triangles, quads, n-sided - by projection the subdivisions onto them.<br>
The default orientation of the cuts is perpendicular to the selected edge, the default width is the total width of the polygon in the direction of the selected edge.

### Only selected Edge
Limits the width for the subdivisions to the length of the selected edge.<br>
No rotation is possible with this option, because this would confuse the measurement of the width.

### Fixed Orientation
Instead of the selected edge this will use a global "down" direction for cutting.<br>
Use "Rotale around Normal" to alter this direction.

### Rotate around Normal
Rotates the cuts around the normal of each respective polygon.

### Use Reference
This option lets you cut across several polygons and use a previous parent to set the width for the cuts.<br>
To set this up you need to use "set_face_ID_tags" with a prefix and the option "Store as Reference".<br>
**Example:** The faces 1, 5 and 7 are assigned the tags "Ref_1", Ref_5", and "Ref_7" ("Ref_" is the prefix in this case).<br>
Now keep subdividing, extruding, etc. the polygons 1, 5 and 7 with the option "Inherit Source Tags", so that all their "children" keep the name bit of "Ref_1" etc.<br>
Later, if you need to multi-cut those children in the space (width) of their parents, just mention the **Prefix** ("Ref_") in this field and the assignment of the children to their respective parents is done automatically.



## Fixed Subdivs

### Fixed Subdivs
Locks the number of subdivisions. The „Flexible“ strip type will compensate.

### Subdivs
Number of subdivisions if fixed.<br>
Accepts also an array with individual settings per source face.

## Tags

Which tags to assign to the resulting polygons.<br>
HINT: face tags can be displayed using the PPG_diagnostic

### Inherit Source Tag
Adds the name of the source face to the resulting tag name.

### Inner/Outer
Names for the respective strip types.

## Output

### Merge Vertices
Merge vertices after the operation.

### Tolerance
Tolerance.

## Diagnostic
Position, size and color of an arrow that indicates the selected edge for every selected face.
The arrows can be turned on/off with the terminal switch on the node.


## Tutorial
https://youtu.be/X-6NRl1QD0Y
<br><br>

# PPG Sequence Cut
Cuts selected quad polygons into strips with given patten of widths.

## Tutorial
https://youtu.be/vu3M4q-ZdX4
<br><br>Tutorial for PPG_multi_cut explaining the use of references:<br>
https://youtu.be/aJZP28DGG-8
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Settings

### Size Sequence
A comma-separated list of sizes (ratios) for subsequent cuts.<br>
This port will also accept an array of scalar values.

### Sequence Scale
A scaling factor for the above sequence.<br>
This factor makes it easier to specify simple ratios and then scale them up or down.<br>

### Flexible
A comma-separated (0-based) list of the elements that should be flexible.<br>
Flexible elements can change in size until a new subdivision with rigid elements is possible.<br>
An asterisk (\*) will act as a wildcard to make **all** elements flexible.<br>
A -1 addresses the **last** element in the sequence.<br>
Please note that flexible elements can **grow**, but will **not shrink** below their size given in the Size Sequence.

### Repeat
This will repeat the sequence, once all elements are present and there is space for another element.<br>
See `create_pattern` for the various modes.

### Endpiece
This will mirror the first piece to the very end of the resulting sequence.<br>
It is supposed to be a surrounding of all other elements.

### Inherit Source Tags
New elements will inherit the name of the source face as a prefix to their name.

### Tag Names
Comma-separated list of names for all elements in "Size Sequence".<br>
If this list is empty or does not contain enough names, numeric names will be created.<br>
Excess names will be ignored.

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

## Output

### Merge Vertices
Merge vertices after the operation.

### Tolerance
Tolerance.



## Diagnostic
Position, size and color of an arrow that indicates the selected edge for every selected face.
The arrows can be turned on/off with the terminal switch on the node.


## Tutorial
https://youtu.be/vu3M4q-ZdX4
<br><br>Tutorial for PPG_multi_cut explaining the use of references:<br>
https://youtu.be/aJZP28DGG-8
<br><br>

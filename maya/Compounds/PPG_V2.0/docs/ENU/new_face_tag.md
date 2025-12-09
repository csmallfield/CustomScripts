# New Face Tag
Set the face tag for a selection of faces.<br>
This is a combination of "get_faces_from_tags" and "set_face_tag".


## Inputs

### Object
The input geometry.

## Selection

### Tag Expression
A simple space separated list of face tag names to select faces of the input mesh.<br>
You can use \* in the names as a wildcard.<br>
A "!" at the start of a name means "except".

### Face IDs
An array of face numbers to add to the selection of "Tag Expression".

### Invert
Invert the combined selection of the expression and faceIDs.

## Output
 
### Face Tag
Name of the face tag to set.


## Tutorial

<br><br>

# Bulk Assign Material
Assigns material references to multiple face groups.<br>

## Inputs

### Mesh
The input geometry with face tags.<br>

### Assign Material
Fan-in string array input.<br><br>
Connect multiple string value nodes that contain a material assignment in the form:<br>
`face tag expression(s) : material_name`<br>
- `face tag expression` is a space separated list of face tags which may contain "\*" (asterisk) wildcards.<br>
- `material_name` is the name of a material in Maya.<br>

Each string can assign ONE material.<br>
Example:<br>
`*win* transp* face36 : glas` assigns the material `glas` to all faces that are matched by the expressions, which are:
- any tags that contain "win"
- any tags that start with "transp"
- the tag "face36"


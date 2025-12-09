# Get Maya Component Tags
Not supported in Bifrost 2.7.0.<br>
Get Maya component tags.

### Component Type
Faces or Points.<br>
Edges are not yet supported.

### Tag Expression
A simple space separated list of component tag names to select faces/points of the input mesh.<br>
You can use \* in the names as a wildcard.

### Multi Tag Separator
If a component is assigned multiple component tags then all of these names will be built into one string using this separator.<br>
A "\n" can be used by the print nodes to print multiple lines.

## Outputs

### Tag Names
A list of tag names that were found with the current "Tag Expression".

### Tags per Component
For each component there is a string with the component tag(s).<br>
None of the strings in this list should be empty.

### Component Indices
List of indices of components (faces or points) that were found with the current "Tag Expression".

## Tutorial

<br><br>

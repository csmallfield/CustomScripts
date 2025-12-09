# Pattern Rename
Sets PPG face tags for the provided face IDs.<br>
Creates a pattern of names from the list in 'Pattern'.

## Inputs

### Object
Input object

### Face IDs to Rename
An array of face IDs to rename.<br>
This can also be a 2-dimensional array. The IDs in each sub-array would get the same pattern name.<br>
See 'cluster_values' for an example.

### Inherit Source Tags
Adds the name of the source face to the resulting tag name.

### Pattern
A comma-separated list of tags names.<br>
If this string is empty then a numeric sequence will be built as the pattern sequence.<br>
If the original pattern list contains only ONE element, then this will be used as a prefix for the numeric sequence.

### Pattern Repeat
How to repeat the pattern
+ Loop: Repeat the pattern in the direction (see Pattern Align)
+ Bounce: Repeat the pattern forward-backward and skip the first/last element
+ Bounce+: Repeat the pattern forward-backward and REPEAT the first/last element
+ Fill: Fill the pattern once and then repeat the last/first element (depending on direction)
+ Stop: Fill the pattern once and then -1

### Pattern Align
Sets the direction of the pattern
+ Start: aligns the pattern left at the start
+ End: aligns the pattern at the END and fills the array towards the start.

### Mirror at Center
First fills the RIGHT/SECOND half of the resulting array (starting/ending at the center) and then mirrors it over to the LEFT.


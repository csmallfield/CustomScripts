# Create Pattern
Repeats a sequence in various ways.

### Sequence
A sequence of numbers/values that will be repeated. This can be a pattern by itself.

### Number of Elements
Length of the resulting array

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


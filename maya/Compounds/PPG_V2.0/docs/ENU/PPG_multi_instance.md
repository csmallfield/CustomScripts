# PPG Multi Instance
Replaces selected faces with a ROW of instance objects.

## Tutorial
https://youtu.be/peICR8uT5_M
<br><br>

## Inputs

### Mesh
The input geometry.

### Enable
Turns the node on and off.

## `Face Selection / Edge Selection`
See `get_face_info` for a detailed description of face/edge selection.

## Instance Selection

### Selection Mode
+ Sequential. just repeats all instance objects sequentially
+ Random: randomly pick instance objects
+ Pattern: uses the new pattern creator to pick instances


### Seed
Random seed.

## Position and Count

### Distance
Distance in Units for the instances.<br>
The size of the polygon defines the number of instances.<br>
Accepts also an array with individual settings per source face.

### Fixed Number of Instances
Ignore "Distance" and place a fixed number of instances on every polygon.

### Number of Instances
Fixed number of instances.

### Position 1
If the instances are placed along one direction of the polygon (see "Edge Selection") then this is the position in the other direction.<br>
0.5 is the center of the polygon.<br>
Accepts also an array with individual settings per source face.

### Side Space
How much space in units to leave at the end of the instance row.<br>
This makes the polygon shorter (longer if negative).<br>
Accepts also an array with individual settings per source face.

### Shift
If there is "Side Space" then this value determines the split between start and end.<br>
This will shift the instances back and forth.<br>
Has no effect if there is no "Side Space".<br>
Accepts also an array with individual settings per source face.

## Pattern
For the selection mode "Pattern".<br>
The node "create_patter" is used internally. You can use the node standalone to explore the different modes.<br>

### Pattern Sequence
If no array is provided this is just a sequence of numbers for all instance objects.<br>
You can provide your own base pattern.

### Pattern Repeat
+ Loop: just loops through the pattern sequence.
+ Bounce: repeats the pattern sequence forth-back-forth-...etc. by NOT repeating the first last element.
+ Bounce+: repeats the pattern sequence forth-back-forth-...etc. by REPEATING the first last element.
+ Fill: sets the pattern sequence only once and fills the rest with the last element.
+ Stop: sets the pattern sequence only once and leaves the rest blank.

### Pattern Align:
+ Start: the pattern sequence is aligned at the start of the output array (resulting instances) and then repeated.
+ End:  the pattern sequence is aligned at the END of the output array and then repeated towards the start of the array.

### Pattern Reverse
Reverse that pattern array (even if it is just the default sequence).

### Mirror at Center
The patterns is done for the second half of the output array and then mirrored to the first half.


## Randomize
Randomize the transformations of the instances.

## Diagnostic
The diagnostic display can be turned on/off with the terminal switch on the node.

### Selected Edge
Position, size and color of an arrow that indicates the selected edge for every selected face.

### Pivot
Display a pivot axis for placement and orientation.<br>


## Tutorial
https://youtu.be/peICR8uT5_M
<br><br>

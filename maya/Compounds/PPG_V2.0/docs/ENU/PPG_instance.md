# PPG Instance
Replaces selected faces with instance objects.<br>
The instance objects are scaled and oriented according to the respective face.

## Tutorial
https://youtu.be/8443cA3KVqY
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
Sequential or random.

### Probability Curve
Play with the curve to ias the probability.

### Seed
Random seed.

## Instance Orientation

### Pre Rotation
Rotate instance object before any other processing.<br>
This will help get the instance objects in the correct orientation for the local axis of the faces (which depends on the selected edge).<br>
To quickly find the required values, set all three values to 0 and start at X to achieve an improvement in the position. Next, try to improve the position with the Y rotation. Always proceed in steps of 90 degrees. An interactive setting makes it easier to understand the changes made.

## Pivot

### Pivot on Edge
When `Pivot ìn Center` is 0 then this value will place the pivot on the border of the respective polygon.<br>
The range 0 to 1 stands for the first (selected) edge. The range 0 to -1 is the LAST edge of the polygon (clockwise from the selected edge).

### Pivot in Center
The range 0 to 1 blends betwee the pivot on the edge and the pivot in the center of the polygon.

## Transform Instances

### Auto Scale
Scale the instances so that they fit the sice of the respective polygon.

### Scale Uniform 
Scale the instances uniformly until they fit the size of the respective polygon.

### Translation
### Rotation
### Scale Relative
Relative Transforms.<br>
Accepts also an array with individual settings per source face.

### Add Scale in Units
Scales the instance so that it grows/shrinks in absolute units.<br>
A setting of <1, 0, 0> would grow the instance by 1 unit in X.<br>
Accepts also an array with individual settings per source face.

## Output

### Keep Instance Face Tags
The face tags of the instance objects will not be overwritten with a random tag name.

### Delete Source Faces
In case you still need the source faces.



## Diagnostic
The diagnostic display can be turned on/off with the terminal switch on the node.

### Selected Edge
Position, size and color of an arrow that indicates the selected edge for every selected face.

### Pivot
Display a pivot axis for placement and orientation.<br>



## Tutorial
https://youtu.be/8443cA3KVqY
<br><br>

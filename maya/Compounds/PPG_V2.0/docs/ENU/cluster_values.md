# Cluster Values
Lets you build groups of values that are similar.<br>
Example: 
- Face IDs need to be grouped together based on the Y position of the face centers.
- The Face IDs are fed into 'Values to Cluster'.
- The Y component of the according face centers is fed into 'Cluster Value'
- All Face IDs whos Y position is within the tolerance are grouped and output as a 2-dimensional array.

## Inputs

### Values to Cluster
Array that you want to divide into groups.<br>
This can be any type.

### Cluster Value
Array of scalar values, same order as 'Values to Cluster'.<br>
Values within 'Tolerance' will be grouped together.
	
### Tolerance
Tolerance

## Outputs

### Clustered Values
2-dimensional array of all members of 'Values to Cluster'.<br>
Such a 2-dimensional array can be processed in a loop and also used with the node 'pattern_rename'.

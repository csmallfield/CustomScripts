# PPG Diagnostic
Diagnostic display for PPG specific face tags.

## Inputs

### Mesh
The input geometry.

## Soften Harden Edges

### Enable Soften Harden
Enable.

### Angle
Angle for Soften/Harden.

## Color Tags
These settings create random colors for all PPG specific face tags.<br>
IMPORTANT: To create per-face colors the polygons are detached and assigned different shaders. For the final geometry you should turn colors OFF.


### Enable
Enable colors.

### Hue Range
360 means the whole color range.

### Hue Offset
Shift a smaller color range.

### Hue Random Seed
Random seed.

### Saturation Base
Base saturation.

### Sat Random
Max random amount added on top of base.

### Sat Random Seed
Random seed.

### Brightness
Brightness of all colors.

### Default Tag Color
The color of the "Default" face tag ("--").<br>
All random colors will be a color, i.e. not grey.

## Face Tag Names
Display the names of the face tags in 3D on the polygons.

## Face Tag Selection
Select which face tags to display.

### Tag Expression
Filter the tag names to display only specific ones or to exclude some.<br>
Default is "*" to display ALL face tags.<br>
A "!" at the start of the tag name means to exclude that tag.

### Face IDs
An array of face IDs.

### Invert
Invert the output of the face selection.

## Tag Names
Settings to format the tag display.

### Offset along Normal
Moves the label along the respective face normal.

### Line Color
Text Color.

### Offset
Additional Transformation.

### Rotation
Additional Rotation.

### Scale
Size of the label.

### Max Labels
Max number of labels to display.<br>
Set this higher if you need to see more labels.

## Information
What to display.

### Show Face Tag
Show the name of the tag.

### Show face ID
Show the number of that face.



## Tutorial

<br><br>

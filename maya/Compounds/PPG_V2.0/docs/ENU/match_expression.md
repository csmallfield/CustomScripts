Checks whether a string name matches the `expression` input.<br>
This is useful for filtering property names using wildcards.<br><br>
Some example expressions:
+ To match:
+ all strings use: `*`
+ strings that start with `"point_"` OR end with `"index"` use: `point_* *index`
+ all strings AND NOT those that end with `"normal"` use: `* !*normal`
+ strings that contain `"point"` use: `*point*`

The expressions are separated with SPACE.<br>
To include a space character in the expression use `\_` (backslash SPACE).

## Inputs

### String
The string to test with the expression(s)

### Expression
The expression(s) to test the string against. 

### Match Case
Match the case of the letters.

## Outputs

### matches
Set to true if the property_expression matches the property_name. 
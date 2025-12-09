# Bifrost Reference Part 5: Core Math, Arrays, Transforms & Utilities

## CORE::MATH - Basic Math Operations

**add** - Adds values
- Inputs: values (multiple)
- Outputs: sum

**subtract** - Subtracts values
- Inputs: minuend, subtrahend
- Outputs: difference

**multiply** - Multiplies values
- Inputs: values (multiple)
- Outputs: product

**divide** - Divides values
- Inputs: dividend, divisor
- Outputs: quotient

**negate** - Negates value (multiplies by -1)
- Inputs: value
- Outputs: negated_value

**absolute_value** - Absolute value
- Inputs: value
- Outputs: abs_value

**power** - Raises to power
- Inputs: base, exponent
- Outputs: result

**power_of_two** - Raises 2 to power
- Inputs: exponent
- Outputs: result (2^exponent)

**two_to_power_of** - Same as power_of_two
- Inputs: exponent
- Outputs: result

**square_root** - Square root
- Inputs: value
- Outputs: sqrt_value

**cube_root** - Cube root
- Inputs: value
- Outputs: cbrt_value

**exponential** - e^x
- Inputs: x
- Outputs: exp_x

**log_base_e** - Natural logarithm (ln)
- Inputs: value
- Outputs: ln_value

**log_base_ten** - Base-10 logarithm
- Inputs: value
- Outputs: log10_value

**log_base_two** - Base-2 logarithm
- Inputs: value
- Outputs: log2_value

**modulo** - Modulo operation
- Inputs: dividend, divisor
- Outputs: remainder

**remainder** - Floating-point remainder
- Inputs: dividend, divisor
- Outputs: remainder

**one_over** - Reciprocal (1/x)
- Inputs: value
- Outputs: reciprocal

**half_of** - Divides by 2
- Inputs: value
- Outputs: value/2

**twice_of** - Multiplies by 2
- Inputs: value
- Outputs: value*2

**increment** - Adds 1
- Inputs: value
- Outputs: value+1

**decrement** - Subtracts 1
- Inputs: value
- Outputs: value-1

## CORE::MATH - Rounding & Clamping

**round_to_nearest** - Rounds to nearest integer
- Inputs: value
- Outputs: rounded_value

**round_to_floor** - Rounds down
- Inputs: value
- Outputs: floor_value

**round_to_ceiling** - Rounds up
- Inputs: value
- Outputs: ceil_value

**truncate** - Truncates decimal part
- Inputs: value
- Outputs: truncated_value

**split_fraction** - Splits into integer and fractional parts
- Inputs: value
- Outputs: integer_part, fractional_part

**clamp** - Clamps value to range
- Inputs: value, min, max
- Outputs: clamped_value

**min** - Minimum of values
- Inputs: values (multiple)
- Outputs: min_value

**max** - Maximum of values
- Inputs: values (multiple)
- Outputs: max_value

**within_bounds** - Checks if value is within range
- Inputs: value, min, max
- Outputs: is_within (bool)

**copy_sign** - Copies sign from one value to another
- Inputs: magnitude, sign_source
- Outputs: result (magnitude with sign)

## CORE::MATH - Trigonometry

**sin** - Sine
- Inputs: angle_radians
- Outputs: sin_value

**cos** - Cosine
- Inputs: angle_radians
- Outputs: cos_value

**tan** - Tangent
- Inputs: angle_radians
- Outputs: tan_value

**asin** - Arcsine
- Inputs: value
- Outputs: angle_radians

**acos** - Arccosine
- Inputs: value
- Outputs: angle_radians

**atan** - Arctangent
- Inputs: value
- Outputs: angle_radians

**atan_2D** - Two-argument arctangent (atan2)
- Inputs: y, x
- Outputs: angle_radians

**sin_hyperbolic** - Hyperbolic sine
- Inputs: value
- Outputs: sinh_value

**cos_hyperbolic** - Hyperbolic cosine
- Inputs: value
- Outputs: cosh_value

**tan_hyperbolic** - Hyperbolic tangent
- Inputs: value
- Outputs: tanh_value

**asin_hyperbolic** - Inverse hyperbolic sine
- Inputs: value
- Outputs: asinh_value

**acos_hyperbolic** - Inverse hyperbolic cosine
- Inputs: value
- Outputs: acosh_value

**atan_hyperbolic** - Inverse hyperbolic tangent
- Inputs: value
- Outputs: atanh_value

## CORE::MATH - Vector Operations

**length** - Vector magnitude/length
- Inputs: vector (float2/float3/float4)
- Outputs: length (float)

**length_squared** - Squared length (avoids sqrt)
- Inputs: vector
- Outputs: length_squared

**normalize** - Normalizes vector to unit length
- Inputs: vector
- Outputs: normalized_vector

**direction_and_length** - Gets direction and length separately
- Inputs: vector
- Outputs: direction (normalized), length

**dot** - Dot product
- Inputs: vector_a, vector_b
- Outputs: dot_product (float)

**cross** - Cross product (3D only)
- Inputs: vector_a (float3), vector_b (float3)
- Outputs: cross_product (float3)

**distance** - Distance between two points
- Inputs: point_a, point_b
- Outputs: distance (float)

**project_vector** - Projects vector onto another
- Inputs: vector, target_direction
- Outputs: projected_vector

**find_orthogonal_vectors** - Finds two vectors perpendicular to input
- Inputs: vector (float3)
- Outputs: perpendicular_a (float3), perpendicular_b (float3)

## CORE::MATH - Interpolation

**lerp** - Linear interpolation
- Inputs: value_a, value_b, blend (0-1)
- Outputs: interpolated_value

**linear_interpolate** - Same as lerp
- Inputs: value_a, value_b, blend
- Outputs: result

**linear_interpolate_normalized** - Lerp with input range normalization
- Inputs: value_a, value_b, input_value, input_min, input_max
- Outputs: result

**change_range** - Remaps value from one range to another
- Inputs: value, old_min, old_max, new_min, new_max
- Outputs: remapped_value

**linear_interpolate_array** - Interpolates array values by index
- Inputs: array, index (float - can be fractional)
- Outputs: interpolated_value

**get_from_interpolated_array** - Gets interpolated value from array
- Inputs: array, normalized_index (0-1)
- Outputs: value

**index_to_fraction** - Converts array index to normalized position
- Inputs: index (int), array_size (int)
- Outputs: fraction (0-1)

## CORE::MATH - Matrix Operations

**matrix_multiply** - Multiplies matrices
- Inputs: matrix_a (float4x4), matrix_b (float4x4)
- Outputs: result (float4x4)

**transpose_matrix** - Transposes matrix
- Inputs: matrix (float4x4)
- Outputs: transposed_matrix

**inverse_matrix** - Inverts matrix
- Inputs: matrix (float4x4)
- Outputs: inverse_matrix

**matrix_determinant** - Computes determinant
- Inputs: matrix (float4x4)
- Outputs: determinant (float)

**get_member** - Gets matrix element
- Inputs: matrix, row (int), column (int)
- Outputs: value (float)

**matrix_is_identity** - Checks if matrix is identity
- Inputs: matrix
- Outputs: is_identity (bool)

**matrix_is_orthonormal** - Checks if matrix is orthonormal
- Inputs: matrix
- Outputs: is_orthonormal (bool)

**matrix_is_singular** - Checks if matrix is singular (non-invertible)
- Inputs: matrix
- Outputs: is_singular (bool)

**set_matrix_translation** - Sets translation component
- Inputs: matrix, translation (float3)
- Outputs: matrix

## CORE::MATH - Quaternion Operations

**axis_angle_to_quaternion** - Converts axis-angle to quaternion
- Inputs: axis (float3), angle_radians (float)
- Outputs: quaternion (float4)

**quaternion_to_axis_angle** - Converts quaternion to axis-angle
- Inputs: quaternion (float4)
- Outputs: axis (float3), angle_radians (float)

**euler_to_quaternion** - Converts Euler angles to quaternion
- Inputs: euler_angles (float3), rotation_order (string)
- Outputs: quaternion (float4)

**quaternion_to_euler** - Converts quaternion to Euler angles
- Inputs: quaternion (float4), rotation_order (string)
- Outputs: euler_angles (float3)

**euler_to_rotation_vector** - Converts Euler to rotation vector (axis*angle)
- Inputs: euler_angles (float3), rotation_order (string)
- Outputs: rotation_vector (float3)

**rotation_vector_to_quaternion** - Converts rotation vector to quaternion
- Inputs: rotation_vector (float3)
- Outputs: quaternion (float4)

**quaternion_to_rotation_vector** - Converts quaternion to rotation vector
- Inputs: quaternion (float4)
- Outputs: rotation_vector (float3)

**matrix_to_quaternion** - Extracts quaternion from matrix
- Inputs: matrix (float4x4)
- Outputs: quaternion (float4)

**quaternion_to_matrix** - Converts quaternion to rotation matrix
- Inputs: quaternion (float4)
- Outputs: matrix (float4x4)

**multiply_quaternions** - Multiplies quaternions (combines rotations)
- Inputs: quaternion_a, quaternion_b
- Outputs: result_quaternion

**quaternion_conjugate** - Conjugates quaternion (inverse rotation)
- Inputs: quaternion
- Outputs: conjugate_quaternion

**quaternion_invert** - Inverts quaternion
- Inputs: quaternion
- Outputs: inverse_quaternion

**quaternion_slerp** - Spherical linear interpolation of quaternions
- Inputs: quaternion_a, quaternion_b, blend (0-1)
- Outputs: interpolated_quaternion

**rotate_by_quaternion** - Rotates vector by quaternion
- Inputs: vector (float3), quaternion (float4)
- Outputs: rotated_vector (float3)

**rotation_between_vectors** - Computes quaternion rotating from one vector to another
- Inputs: from_vector (float3), to_vector (float3)
- Outputs: quaternion (float4)

## CORE::MATH - Transform/SRT Operations

**SRT_to_matrix** - Converts Scale/Rotation/Translation to matrix
- Inputs: scale (float3), rotation (float4 quaternion), translation (float3)
- Outputs: matrix (float4x4)

**matrix_to_SRT** - Decomposes matrix into SRT
- Inputs: matrix (float4x4)
- Outputs: scale (float3), rotation (float4 quaternion), translation (float3)

**normal_and_tangent_to_orientation** - Computes orientation from normal and tangent
- Inputs: normal (float3), tangent (float3)
- Outputs: orientation (float4 quaternion)

**angle_around_axis** - Computes angle of rotation around axis
- Inputs: vector (float3), axis (float3)
- Outputs: angle_radians (float)

**transform_vector** - Transforms vector by matrix
- Inputs: vector (float3), matrix (float4x4)
- Outputs: transformed_vector

**transform_vector_as_position** - Transforms as point (includes translation)
- Inputs: position (float3), matrix (float4x4)
- Outputs: transformed_position

**transform_vector_as_direction** - Transforms as direction (no translation)
- Inputs: direction (float3), matrix (float4x4)
- Outputs: transformed_direction

**transform_vector_as_normal** - Transforms as normal (uses inverse transpose)
- Inputs: normal (float3), matrix (float4x4)
- Outputs: transformed_normal

**rotate_vector_by_matrix** - Rotates vector by rotation matrix
- Inputs: vector (float3), rotation_matrix (float4x4)
- Outputs: rotated_vector

**transform_to_rotation_matrix** - Extracts rotation part of transform
- Inputs: transform_matrix (float4x4)
- Outputs: rotation_matrix (float4x4)

**rotation_around_position_to_matrix** - Creates rotation matrix around point
- Inputs: rotation (float4 quaternion), pivot (float3)
- Outputs: matrix (float4x4)

**interpolate_transform_matrix** - Interpolates between transforms
- Inputs: matrix_a, matrix_b, blend (0-1)
- Outputs: interpolated_matrix

## CORE::TRANSFORM - Transform Management

**compute_transform** - Computes transform from SRT
- Inputs: scale (float3), rotation (float4), translation (float3)
- Outputs: transform

**update_transform** - Updates existing transform
- Inputs: transform, scale, rotation, translation
- Outputs: updated_transform

**compute_transform_chain** - Computes chain of transforms
- Inputs: transforms (array), parent_indices (int[])
- Outputs: world_transforms (array)

**update_transform_chain** - Updates transform hierarchy
- Inputs: transforms (array), parent_indices
- Outputs: world_transforms

**compute_transform_tree** - Computes tree hierarchy of transforms
- Inputs: local_transforms (array), tree_structure
- Outputs: world_transforms

**update_transform_tree** - Updates transform tree
- Inputs: transform_tree
- Outputs: updated_tree

**access_transform_matrices** - Gets matrices from transform
- Inputs: transform
- Outputs: local_matrix, world_matrix

**interpret_auto_port_as_transform** - Converts various inputs to transform
- Inputs: value (auto - matrix, SRT, etc)
- Outputs: transform

**to_double4x4** - Converts transform to double-precision matrix
- Inputs: transform
- Outputs: matrix (double4x4)

**graph_space** - Gets graph coordinate space transform
- Inputs: none
- Outputs: graph_space_transform

## CORE::ARRAY - Array Operations

**build_array** - Creates array from individual values
- Inputs: values (multiple)
- Outputs: array

**empty_array** - Creates empty array
- Inputs: type
- Outputs: empty_array

**array_size** - Gets array length
- Inputs: array
- Outputs: size (uint)

**array_is_empty** - Checks if array is empty
- Inputs: array
- Outputs: is_empty (bool)

**array_bounds** - Gets array size bounds
- Inputs: array
- Outputs: min_index (0), max_index (size-1)

**get_from_array** - Gets element from array
- Inputs: array, index (int)
- Outputs: value

**set_in_array** - Sets element in array
- Inputs: array, index (int), value
- Outputs: array

**first_in_array** - Gets first element
- Inputs: array
- Outputs: first_value

**last_in_array** - Gets last element
- Inputs: array
- Outputs: last_value

**slice_array** - Extracts subarray
- Inputs: array, start_index (int), end_index (int)
- Outputs: subarray

**small_slice** - Gets small slice (optimized for small arrays)
- Inputs: array, start_index, count
- Outputs: slice

**resize_array** - Resizes array
- Inputs: array, new_size (int), fill_value
- Outputs: resized_array

**sequence_array** - Creates sequence array
- Inputs: start (int), end (int), step (int)
- Outputs: sequence (int[])

**reverse_array** - Reverses array order
- Inputs: array
- Outputs: reversed_array

**flatten_nested_array** - Flattens nested array structure
- Inputs: nested_array
- Outputs: flat_array

**merge_any_arrays** - Merges multiple arrays
- Inputs: arrays (multiple)
- Outputs: merged_array

**intersect_arrays** - Gets intersection of arrays
- Inputs: array_a, array_b
- Outputs: intersection

**get_array_indices** - Gets all valid indices
- Inputs: array
- Outputs: indices (uint[])

**cumulative_sum_array** - Computes cumulative sum
- Inputs: array (numeric)
- Outputs: cumulative_sums

**prefix_sum** - Same as cumulative_sum_array
- Inputs: array
- Outputs: prefix_sums

**sum_array** - Sums all array elements
- Inputs: array (numeric)
- Outputs: sum

## CORE::ARRAY - Array Searching

**find_in_array** - Finds first occurrence of value
- Inputs: array, value
- Outputs: index (int), found (bool)

**reverse_find_in_array** - Finds last occurrence
- Inputs: array, value
- Outputs: index (int), found (bool)

**find_in_sorted_array** - Binary search in sorted array
- Inputs: sorted_array, value
- Outputs: index (int), found (bool)

**find_all_in_array** - Finds all occurrences
- Inputs: array, value
- Outputs: indices (int[])

**find_all_true_in_array** - Finds all true elements
- Inputs: bool_array
- Outputs: indices (int[])

**any_true_in_array** - Checks if any element is true
- Inputs: bool_array
- Outputs: any_true (bool)

**all_true_in_array** - Checks if all elements are true
- Inputs: bool_array
- Outputs: all_true (bool)

**filter_array** - Filters array by boolean mask
- Inputs: array, mask (bool[])
- Outputs: filtered_array

**remove_from_array** - Removes elements by indices
- Inputs: array, indices (int[])
- Outputs: array

## CORE::ARRAY - Array Sorting

**sort_array** - Sorts array
- Inputs: array, ascending (bool)
- Outputs: sorted_array

**sort_array_with_indices** - Sorts and returns original indices
- Inputs: array, ascending
- Outputs: sorted_array, sort_indices

**sort_array_and_remove_duplicates** - Sorts and removes duplicates
- Inputs: array
- Outputs: sorted_unique_array

**shuffle_array** - Randomly shuffles array
- Inputs: array, seed (int)
- Outputs: shuffled_array

## CORE::LOGIC - Logic Operations

**and** - Logical AND
- Inputs: a (bool), b (bool)
- Outputs: result (bool)

**or** - Logical OR
- Inputs: a (bool), b (bool)
- Outputs: result (bool)

**xor** - Logical XOR
- Inputs: a (bool), b (bool)
- Outputs: result (bool)

**not** - Logical NOT
- Inputs: value (bool)
- Outputs: result (bool)

**equal** - Equality test
- Inputs: a, b
- Outputs: equal (bool)

**not_equal** - Inequality test
- Inputs: a, b
- Outputs: not_equal (bool)

**greater** - Greater than test
- Inputs: a, b
- Outputs: is_greater (bool)

**less** - Less than test
- Inputs: a, b
- Outputs: is_less (bool)

**greater_or_equal** - Greater or equal test
- Inputs: a, b
- Outputs: result (bool)

**less_or_equal** - Less or equal test
- Inputs: a, b
- Outputs: result (bool)

**almost_equal** - Approximate equality (with epsilon)
- Inputs: a, b, epsilon (float)
- Outputs: almost_equal (bool)

**if** - Conditional branch
- Inputs: condition (bool), value_if_true, value_if_false
- Outputs: result

**members_if** - Per-element conditional
- Inputs: condition (bool[]), values_if_true, values_if_false
- Outputs: results

**all_members_true** - Tests if all array elements are true
- Inputs: bool_array
- Outputs: all_true (bool)

**any_members_true** - Tests if any array element is true
- Inputs: bool_array
- Outputs: any_true (bool)

**members_equal** - Per-element equality test
- Inputs: array_a, array_b
- Outputs: equal_mask (bool[])

**members_not_equal** - Per-element inequality
- Inputs: array_a, array_b
- Outputs: not_equal_mask (bool[])

**members_greater** - Per-element greater than
- Inputs: array_a, array_b
- Outputs: greater_mask (bool[])

**members_less** - Per-element less than
- Inputs: array_a, array_b
- Outputs: less_mask (bool[])

**members_greater_or_equal** - Per-element greater or equal
- Inputs: array_a, array_b
- Outputs: mask (bool[])

**members_less_or_equal** - Per-element less or equal
- Inputs: array_a, array_b
- Outputs: mask (bool[])

## CORE::BITWISE - Bitwise Operations

**bitwise_and** - Bitwise AND
- Inputs: a (int), b (int)
- Outputs: result (int)

**bitwise_or** - Bitwise OR
- Inputs: a (int), b (int)
- Outputs: result (int)

**bitwise_xor** - Bitwise XOR
- Inputs: a (int), b (int)
- Outputs: result (int)

**bitwise_not** - Bitwise NOT
- Inputs: value (int)
- Outputs: result (int)

**bitwise_shift_left** - Left bit shift
- Inputs: value (int), shift_amount (int)
- Outputs: result (int)

**bitwise_shift_right** - Right bit shift
- Inputs: value (int), shift_amount (int)
- Outputs: result (int)

**bitwise_shift_left_circular** - Circular left shift
- Inputs: value (int), shift_amount (int)
- Outputs: result (int)

**bitwise_shift_right_circular** - Circular right shift
- Inputs: value (int), shift_amount (int)
- Outputs: result (int)

## CORE::CONSTANTS - Mathematical Constants

**zero** - Returns 0
- Inputs: none
- Outputs: 0

**one** - Returns 1
- Inputs: none
- Outputs: 1

**identity** - Returns identity matrix
- Inputs: none
- Outputs: identity_matrix (float4x4)

**pi** - Returns π (3.14159...)
- Inputs: none
- Outputs: pi

**tau** - Returns τ (2π = 6.28318...)
- Inputs: none
- Outputs: tau

**e** - Returns e (2.71828...)
- Inputs: none
- Outputs: e

**golden_ratio** - Returns φ (1.61803...)
- Inputs: none
- Outputs: phi

**numeric_max** - Returns maximum representable value for type
- Inputs: type
- Outputs: max_value

**numeric_min** - Returns minimum representable value for type
- Inputs: type
- Outputs: min_value

**numeric_small** - Returns smallest positive value for type (epsilon)
- Inputs: type
- Outputs: epsilon

**default_value** - Returns default value for type
- Inputs: type
- Outputs: default_value

## CORE::RANDOMIZATION - Random Number Generation

**random_value** - Generates random value
- Inputs: min (float), max (float), seed (int)
- Outputs: random_value

**random_value_array** - Generates random array
- Inputs: count (int), min, max, seed
- Outputs: random_values

**randomize_direction** - Generates random unit vector
- Inputs: seed (int)
- Outputs: direction (float3)

**randomize_direction_array** - Generates random direction array
- Inputs: count (int), seed (int)
- Outputs: directions (float3[])

**fractal_noise** - Fractal noise value
- Inputs: position (float3), octaves (int), amplitude (float), frequency (float)
- Outputs: noise_value

**fractal_turbulence** - Fractal turbulence value
- Inputs: position (float3), octaves, amplitude, frequency
- Outputs: turbulence_value

**hash_float** - Hash float to pseudo-random value
- Inputs: value (float), seed (int)
- Outputs: hashed_value

## CORE::STRING - String Operations

**build_string** - Concatenates strings
- Inputs: strings (multiple)
- Outputs: concatenated_string

**string_empty** - Checks if string is empty
- Inputs: string
- Outputs: is_empty (bool)

**string_length** - Gets string length
- Inputs: string
- Outputs: length (int)

**string_join** - Joins array of strings with separator
- Inputs: strings (array), separator (string)
- Outputs: joined_string

**split_string** - Splits string by delimiter
- Inputs: string, delimiter (string)
- Outputs: parts (string[])

**slice_string** - Extracts substring
- Inputs: string, start (int), end (int)
- Outputs: substring

**get_from_string** - Gets character at index
- Inputs: string, index (int)
- Outputs: character (string)

**set_in_string** - Sets character at index
- Inputs: string, index (int), character (string)
- Outputs: string

**string_reverse** - Reverses string
- Inputs: string
- Outputs: reversed_string

**string_find** - Finds substring
- Inputs: string, search_string
- Outputs: index (int), found (bool)

**string_replace** - Replaces substring
- Inputs: string, search_string, replacement
- Outputs: string

**string_starts_with** - Checks if string starts with prefix
- Inputs: string, prefix
- Outputs: starts_with (bool)

**string_ends_with** - Checks if string ends with suffix
- Inputs: string, suffix
- Outputs: ends_with (bool)

**string_upper** - Converts to uppercase
- Inputs: string
- Outputs: uppercase_string

**string_lower** - Converts to lowercase
- Inputs: string
- Outputs: lowercase_string

**string_strip** - Removes leading/trailing whitespace
- Inputs: string
- Outputs: stripped_string

**string_regex_search** - Regex pattern search
- Inputs: string, pattern (regex string)
- Outputs: matches (string[])

**string_to_array** - Converts string to character array
- Inputs: string
- Outputs: characters (string[])

**number_to_string** - Converts number to string
- Inputs: number
- Outputs: string

**string_to_int** - Converts string to integer
- Inputs: string
- Outputs: integer (int)

**string_to_float** - Converts string to float
- Inputs: string
- Outputs: float_value (float)

## CORE::CONVERSION - Type Conversions

**scalar_to_vector2** - Creates float2 from scalar
- Inputs: x (float), y (float)
- Outputs: vector (float2)

**scalar_to_vector3** - Creates float3 from scalars
- Inputs: x, y, z
- Outputs: vector (float3)

**scalar_to_vector4** - Creates float4 from scalars
- Inputs: x, y, z, w
- Outputs: vector (float4)

**vector2_to_scalar** - Extracts components from float2
- Inputs: vector (float2)
- Outputs: x, y

**vector3_to_scalar** - Extracts components from float3
- Inputs: vector (float3)
- Outputs: x, y, z

**vector4_to_scalar** - Extracts components from float4
- Inputs: vector (float4)
- Outputs: x, y, z, w

**vector3_to_vector4** - Extends float3 to float4
- Inputs: vector (float3), w (float)
- Outputs: vector (float4)

**vector4_to_vector3** - Truncates float4 to float3
- Inputs: vector (float4)
- Outputs: vector (float3)

**to_type_any** - Converts to Any type
- Inputs: value
- Outputs: any_value

**from_type_any** - Converts from Any type
- Inputs: any_value, target_type
- Outputs: value

**promote** - Promotes value to compatible type
- Inputs: value, target_type
- Outputs: promoted_value

## CORE::TIME - Time & Animation

**time** - Gets current time
- Inputs: none
- Outputs: time (float seconds)

**timeline_info** - Gets timeline information
- Inputs: none
- Outputs: current_frame, start_frame, end_frame, fps

**evaluate_fcurve** - Evaluates animation curve at time
- Inputs: fcurve, time (float)
- Outputs: value (float)

## CORE::GRAPH - Graph Context

**graph_name** - Gets current graph name
- Inputs: none
- Outputs: name (string)

**node_path** - Gets current node path
- Inputs: none
- Outputs: path (string)

**pass** - Pass-through node (does nothing)
- Inputs: value (any)
- Outputs: value (unchanged)

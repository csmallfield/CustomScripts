# Bifrost Reference Part 6: Rigging, Specialized Systems & Diagnostics

## RIGGING::SKELETON - Skeleton Structure

**construct_skeleton** - Creates skeleton from joint data
- Inputs: joint_names (string[]), parent_indices (int[]), joint_transforms
- Outputs: skeleton

**create_skeleton_from_paths** - Creates skeleton from path strings
- Inputs: joint_paths (string[]), transforms
- Outputs: skeleton

**create_skeleton_from_modules** - Creates skeleton from rig modules
- Inputs: modules (array)
- Outputs: skeleton

**get_skeleton_structure** - Gets skeleton topology
- Inputs: skeleton
- Outputs: joint_names, parent_indices, joint_count

**get_joint_transform_matrices** - Gets all joint matrices
- Inputs: skeleton
- Outputs: local_matrices, world_matrices

**validate_skeleton** - Validates skeleton structure
- Inputs: skeleton
- Outputs: is_valid (bool)

**set_joint_pivot_matrix** - Sets joint pivot transform
- Inputs: skeleton, joint_index (int), pivot_matrix
- Outputs: skeleton

**set_joint_operator_matrix** - Sets joint operator transform
- Inputs: skeleton, joint_index (int), operator_matrix
- Outputs: skeleton

**transform_joints** - Transforms all joints
- Inputs: skeleton, transform_matrix
- Outputs: skeleton

**update_joint_transform_matrices** - Updates joint world transforms
- Inputs: skeleton
- Outputs: skeleton

**update_joint_position** - Updates joint positions
- Inputs: skeleton
- Outputs: skeleton

**update_joint_length** - Computes joint bone lengths
- Inputs: skeleton
- Outputs: skeleton

**update_joint_depth** - Computes hierarchy depth of joints
- Inputs: skeleton
- Outputs: skeleton

**update_joint_path** - Updates joint path strings
- Inputs: skeleton
- Outputs: skeleton

**update_joint_chain_index** - Assigns chain index to joints
- Inputs: skeleton
- Outputs: skeleton

**update_chain_joint_indices** - Updates indices within each chain
- Inputs: skeleton
- Outputs: skeleton

**update_joint_children_indices** - Updates child joint lists
- Inputs: skeleton
- Outputs: skeleton

## RIGGING::SOLVER - IK & Constraint Solvers

**solve_limb_IK** - Two-bone IK solver (arm/leg)
- Inputs: start_joint, mid_joint, end_joint, target_position (float3), pole_vector (float3)
- Outputs: start_rotation (float4), mid_rotation (float4)

**aim_matrix** - Aims transform at target
- Inputs: source_position (float3), target_position (float3), aim_axis (float3), up_axis (float3)
- Outputs: aim_matrix (float4x4)

**parent_matrix** - Parents transform to another
- Inputs: local_transform, parent_transform
- Outputs: world_transform

**blend_matrix** - Blends between transforms
- Inputs: matrix_a, matrix_b, blend (0-1)
- Outputs: blended_matrix

**pick_matrix** - Selects transform from array
- Inputs: matrices (array), index (int)
- Outputs: selected_matrix

**align_matrix_chain** - Aligns chain of transforms
- Inputs: matrices (array), alignment_mode (string)
- Outputs: aligned_matrices

**interpolate_matrix_chain** - Interpolates chain of transforms
- Inputs: matrices (array), blend_values (float[])
- Outputs: interpolated_matrices

**resample_matrix_chain** - Resamples chain to different count
- Inputs: matrices (array), new_count (int)
- Outputs: resampled_matrices

**offset_matrix_chain** - Offsets chain of transforms
- Inputs: matrices (array), offset (float4x4)
- Outputs: offset_matrices

**scale_matrix_chain** - Scales chain of transforms
- Inputs: matrices (array), scale (float or float3)
- Outputs: scaled_matrices

**transform_matrix_chain** - Transforms entire chain
- Inputs: matrices (array), transform (float4x4)
- Outputs: transformed_matrices

## RIGGING::SOLVER::UTILS - Solver Utilities

**calculate_pole_target** - Calculates pole vector for IK
- Inputs: start_position, mid_position, end_position, pole_offset (float)
- Outputs: pole_position (float3)

**enabled_with_weight** - Enables with blend weight
- Inputs: enable (bool), weight (0-1)
- Outputs: effective_weight

**equivalent_weight** - Converts enable/weight to single value
- Inputs: enable (bool), weight (float)
- Outputs: final_weight

## RIGGING::CONVERTERS - Skeleton Conversion

**skeleton_to_points** - Converts skeleton joints to points
- Inputs: skeleton
- Outputs: points

**skeleton_to_strands** - Converts skeleton chains to strands
- Inputs: skeleton
- Outputs: strands

**points_to_skeleton** - Converts points to skeleton structure
- Inputs: points, parent_indices (int[])
- Outputs: skeleton

**strands_to_skeleton** - Converts strands to skeleton
- Inputs: strands
- Outputs: skeleton

## RIGGING::MODULE - Rig Module System

**template_module** - Creates template rig module
- Inputs: module_type (string), parameters
- Outputs: module

**root_module** - Creates root module (pelvis/COG)
- Inputs: position (float3), parameters
- Outputs: module

**spine_module** - Creates spine module
- Inputs: joint_count (int), start_position, end_position
- Outputs: module

**arm_module** - Creates arm module (shoulder/elbow/wrist)
- Inputs: shoulder_position, elbow_position, wrist_position, side (string: "left"/"right")
- Outputs: module

**leg_module** - Creates leg module (hip/knee/ankle)
- Inputs: hip_position, knee_position, ankle_position, side (string)
- Outputs: module

**variable_fk_module** - Creates FK chain with variable joint count
- Inputs: positions (float3[]), orientations (float4[])
- Outputs: module

**aim_module** - Creates aim constraint module
- Inputs: source_position, target_position
- Outputs: module

## RIGGING::MODULE::SETUP - Module Configuration

**define_control** - Defines rig control
- Inputs: name (string), control_shape, transform
- Outputs: control_definition

**define_joint** - Defines joint in module
- Inputs: name (string), parent (string), transform
- Outputs: joint_definition

**define_attribute** - Defines custom attribute
- Inputs: name (string), type (string), default_value
- Outputs: attribute_definition

**set_definitions** - Sets module definitions
- Inputs: module, controls, joints, attributes
- Outputs: module

**find_pin** - Finds connection pin on module
- Inputs: module, pin_name (string)
- Outputs: pin

**find_all_pins** - Gets all pins on module
- Inputs: module
- Outputs: pins (array)

**find_parent** - Finds parent module
- Inputs: module
- Outputs: parent_module

## RIGGING::MODULE::ANIMATION - Animation Controls

**find_attribute** - Finds attribute by name
- Inputs: module, attribute_name (string)
- Outputs: attribute

**find_all_attributes** - Gets all attributes
- Inputs: module
- Outputs: attributes (array)

**find_transform** - Finds transform control
- Inputs: module, control_name (string)
- Outputs: transform

**find_all_transforms** - Gets all transform controls
- Inputs: module
- Outputs: transforms (array)

**find_upstream_transform** - Finds upstream transform in hierarchy
- Inputs: module, transform_name (string)
- Outputs: transform

**find_all_upstream_transforms** - Gets all upstream transforms
- Inputs: module
- Outputs: transforms (array)

**set_transform_update_settings** - Sets transform update mode
- Inputs: transform, update_mode (string)
- Outputs: transform

**set_update_settings** - Sets module update settings
- Inputs: module, settings
- Outputs: module

## DIAGNOSTIC::DISPLAY - Visualization Scopes

**point_scope** - Visualizes points
- Inputs: points, color (float3), size (float)
- Outputs: visualization

**mesh_scope** - Visualizes mesh
- Inputs: mesh, color, wireframe (bool)
- Outputs: visualization

**volume_scope** - Visualizes volume
- Inputs: volume, iso_value (float), color
- Outputs: visualization

**scalar_field_scope** - Visualizes scalar field
- Inputs: field, bounds, resolution
- Outputs: visualization

**vector_field_scope** - Visualizes vector field
- Inputs: vector_field, bounds, resolution, scale (float)
- Outputs: visualization

**influence_scope** - Visualizes influence/force
- Inputs: influence, test_positions (float3[])
- Outputs: visualization

**location_scope** - Visualizes surface locations
- Inputs: locations
- Outputs: visualization

**particle_collision_scope** - Visualizes collision geometry
- Inputs: collider
- Outputs: visualization

**tag_scope** - Visualizes component tags
- Inputs: geometry, tag_expression (string)
- Outputs: visualization

**skeleton_scope** - Visualizes skeleton
- Inputs: skeleton, joint_size (float)
- Outputs: visualization

**transform_scope** - Visualizes transform axes
- Inputs: transform, scale (float)
- Outputs: visualization

**assign_diagnostic_material** - Assigns debug material to geometry
- Inputs: geometry, material_type (string)
- Outputs: geometry

## DIAGNOSTIC::IO - Debug Output

**dump_object** - Dumps object data to console/file
- Inputs: object, filepath (optional string)
- Outputs: dump_string

**log_message** - Logs message to console
- Inputs: message (string), level (string: "info"/"warning"/"error")
- Outputs: none

## DIAGNOSTIC::PROFILING - Performance Profiling

**profiler_start** - Starts profiling section
- Inputs: section_name (string)
- Outputs: profiler_token

**profiler_end** - Ends profiling section
- Inputs: profiler_token
- Outputs: elapsed_time (float ms)

## MACHINE_LEARNING - Neural Network Operations

**layer_linear** - Fully connected layer
- Inputs: input_tensor, weights, biases
- Outputs: output_tensor

**activation_ReLU** - ReLU activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_sigmoid** - Sigmoid activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_tanh** - Tanh activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_soft_max** - Softmax activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_ELU** - ELU activation
- Inputs: tensor, alpha (float)
- Outputs: activated_tensor

**activation_leaky_ReLU** - Leaky ReLU activation
- Inputs: tensor, negative_slope (float)
- Outputs: activated_tensor

**activation_PReLU** - Parametric ReLU activation
- Inputs: tensor, parameters
- Outputs: activated_tensor

**activation_SELU** - SELU activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_CELU** - CELU activation
- Inputs: tensor, alpha
- Outputs: activated_tensor

**activation_hard_sigmoid** - Hard sigmoid activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_hard_swish** - Hard swish activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_hard_tanh** - Hard tanh activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_mish** - Mish activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_soft_plus** - Soft plus activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_soft_sign** - Soft sign activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_soft_shrink** - Soft shrink activation
- Inputs: tensor, lambda (float)
- Outputs: activated_tensor

**activation_hard_shrink** - Hard shrink activation
- Inputs: tensor, lambda
- Outputs: activated_tensor

**activation_tanh_shrink** - Tanh shrink activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_threshold** - Threshold activation
- Inputs: tensor, threshold (float), value (float)
- Outputs: activated_tensor

**activation_log_sigmoid** - Log sigmoid activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_soft_min** - Soft min activation
- Inputs: tensor
- Outputs: activated_tensor

**activation_ReLU6** - ReLU6 activation (clamps to 6)
- Inputs: tensor
- Outputs: activated_tensor

**activation_RReLU** - Randomized ReLU
- Inputs: tensor, lower (float), upper (float)
- Outputs: activated_tensor

**z_score_normalize** - Z-score normalization
- Inputs: data, mean (float), std_dev (float)
- Outputs: normalized_data

**z_score_denormalize** - Reverses z-score normalization
- Inputs: normalized_data, mean, std_dev
- Outputs: data

## WEDGING - Parameter Wedging

**wedge_parameter** - Creates wedge parameter
- Inputs: name (string), values (array)
- Outputs: wedge_param

**wedge_index** - Gets current wedge index
- Inputs: none
- Outputs: index (int)

**applied_wedge_index** - Gets applied wedge index
- Inputs: wedge_param
- Outputs: index (int)

**applied_wedge_parameter** - Gets current wedge value
- Inputs: wedge_param
- Outputs: value

**wedge_filename** - Generates filename with wedge index
- Inputs: base_filename (string), wedge_index (int)
- Outputs: filename (string)

**wedge_cache** - Caches wedge computation
- Inputs: data (any), wedge_param
- Outputs: cached_data

## SCATTER::RANDOMIZATION - Advanced Scatter Utilities

**build_alias_table** - Builds alias table for weighted random selection
- Inputs: weights (float[])
- Outputs: alias_table

**sample_alias_table** - Samples from alias table
- Inputs: alias_table, random_value (0-1)
- Outputs: selected_index (int)

**randomize_geo_property** - Randomizes geometry property
- Inputs: geometry, property_name (string), min_value, max_value, seed (int)
- Outputs: geometry

## SCATTER::MESH - Mesh Utilities for Scatter

**compute_mesh_surface_area** - Computes total mesh surface area
- Inputs: mesh
- Outputs: surface_area (float)

## SCATTER::INSTANCES - Instance Utilities

**flatten_instance_selection** - Flattens procedural instance selection
- Inputs: procedural_instances
- Outputs: instances (with resolved selection)

## SCATTER::PROPERTIES - Point to Transform Conversion

**points_to_transforms** - Converts point cloud to transform matrices
- Inputs: points
- Outputs: transforms (float4x4[])

## SIMULATION::NUCLEUS - Legacy Nucleus Solver

**nucleus_collide_points_with_mesh** - Collides points with mesh (legacy)
- Inputs: points, mesh, friction (float), bounce (float)
- Outputs: points

**nucleus_points_to_mesh** - Converts particles to mesh surface (legacy)
- Inputs: points, mesh_resolution (int)
- Outputs: mesh

## CORE::SET - Set Operations

**string_set** - Creates set from string array (removes duplicates)
- Inputs: strings (string[])
- Outputs: unique_strings (string[])

**set_union** - Union of two sets
- Inputs: set_a, set_b
- Outputs: union_set

**set_intersection** - Intersection of two sets
- Inputs: set_a, set_b
- Outputs: intersection_set

**set_difference** - Difference of two sets (A - B)
- Inputs: set_a, set_b
- Outputs: difference_set

**get_set_members** - Gets all members of set
- Inputs: set
- Outputs: members (array)

**set_has_member** - Checks if set contains element
- Inputs: set, element
- Outputs: has_member (bool)

## CORE::FCURVE - Animation Curve Evaluation

**evaluate_fcurve** - Evaluates animation curve
- Inputs: fcurve, time (float)
- Outputs: value (float)

## CORE::INTERNAL - Internal Utility Nodes

**force_eval** - Forces evaluation of input (for side effects)
- Inputs: value (any)
- Outputs: value (unchanged)

**sleep** - Sleeps for duration (debugging/testing)
- Inputs: duration_ms (float)
- Outputs: none

## FILE::WRITE - State Writing

**write_state** - Writes simulation state to disk
- Inputs: data (any), filepath (string), frame (float)
- Outputs: success (bool)

## CORE::OBJECT::INTERNAL - Internal Object Management

**add_required_free_memory** - Adds to required free memory counter
- Inputs: bytes (uint)
- Outputs: none

**set_required_free_memory** - Sets required free memory
- Inputs: bytes (uint)
- Outputs: none

**subtract_required_free_memory** - Subtracts from required memory
- Inputs: bytes (uint)
- Outputs: none

**enable_copies_tracking** - Enables object copy tracking
- Inputs: none
- Outputs: none

**disable_copies_tracking** - Disables copy tracking
- Inputs: none
- Outputs: none

**number_of_copies** - Gets copy count
- Inputs: none
- Outputs: count (uint)

**number_of_active_copies** - Gets active copy count
- Inputs: none
- Outputs: count (uint)

**number_of_active_named_copies** - Gets named copy count
- Inputs: none
- Outputs: count (uint)

**clear_number_of_copies** - Clears copy counter
- Inputs: none
- Outputs: none

**print_number_of_copies** - Prints copy statistics
- Inputs: none
- Outputs: none

**flush_geometry_allocations** - Flushes geometry memory allocations
- Inputs: none
- Outputs: none

## NOTES ON NODE USAGE

### Common Patterns:
1. **Mesh Construction**: construct_mesh → update_mesh_normals → validate_mesh
2. **Point Scattering**: scatter_points → randomize_point_scale/rotation → create_instances
3. **Volume Creation**: mesh_to_level_set → offset_level_set → volume_to_mesh
4. **Simulation Setup**: source_* → simulate_* → set_*_properties
5. **IK Solving**: calculate_pole_target → solve_limb_IK → blend_matrix
6. **File I/O**: read_Alembic/OpenVDB → process → write_Alembic/OpenVDB

### Important Notes:
- Many nodes work on arrays and auto-vectorize over elements
- Properties are accessed by string name - use exact property names
- Transform hierarchy uses parent indices (int array, -1 = root)
- Most simulation nodes require proper time stepping and caching
- Fields are lazily evaluated - only computed where sampled
- Volumes use sparse tile structure - only active voxels stored

### Performance Tips:
- Use accelerators (build_closest_accelerator) for repeated queries
- Batch operations when possible (array inputs)
- Cache expensive computations with memory_cache
- Use appropriate voxel size for volumes (smaller = slower)
- Profile with profiler_start/profiler_end nodes

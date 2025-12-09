# Bifrost Complete Node Reference - Quick Index

## Document Organization

This reference is split into 6 parts for easier navigation:

1. **Part 1: Core Geometry & Mesh Operations** - Basic geometry creation, mesh manipulation, properties
2. **Part 2: Modeling & Deformation** - Primitives, mesh editing, points, strands, instances
3. **Part 3: Fields, Volumes & Simulation** - Field creation, volume operations, influences
4. **Part 4: Particles, Fluids, Rigid Bodies & Rendering** - All simulation types, file I/O, materials
5. **Part 5: Core Math, Arrays, Transforms & Utilities** - Math ops, array handling, transforms
6. **Part 6: Rigging, Specialized Systems & Diagnostics** - Skeletons, IK, ML, profiling

## Quick Category Reference

### CORE SYSTEMS
- **Math Operations**: add, multiply, sin, cos, sqrt, power, clamp, min, max, lerp
- **Arrays**: build_array, get_from_array, slice_array, sort_array, filter_array
- **Logic**: if, and, or, not, equal, greater, less
- **Strings**: build_string, split_string, string_find, string_replace
- **Transforms**: SRT_to_matrix, matrix_to_SRT, compute_transform, transform_vector
- **Quaternions**: euler_to_quaternion, quaternion_slerp, multiply_quaternions
- **Randomization**: random_value, fractal_noise, randomize_direction

### GEOMETRY OPERATIONS
- **Mesh Construction**: construct_mesh, get_mesh_structure, validate_mesh
- **Mesh Editing**: triangulate_mesh, smooth_mesh, subdivide_mesh, extrude_faces
- **Points**: construct_points, get_points_structure, filter_points
- **Strands**: construct_strands, resample_strands, update_strands_tangents
- **Properties**: get_geo_property, set_geo_property, copy_properties
- **Queries**: build_closest_accelerator, get_closest_point, sample_property
- **Tags**: set_component_tag, resolve_tag_expression
- **Instances**: geo_instance, procedural_instance, set_instance_geometry

### MODELING OPERATIONS
- **Primitives**: create_mesh_cube, create_mesh_sphere, create_mesh_plane
- **Boolean Ops**: boolean_meshes, fracture_mesh, voronoi_fracture_mesh
- **UV Operations**: create_UVs_from_projection_planes, layout_UVs
- **Point Operations**: scatter_points, duplicate_points, cull_overlapping_points
- **Transformations**: transform_points, rotate_points, scale_points, displace_points
- **Randomization**: randomize_point_translation, randomize_point_rotation
- **Strand Editing**: create_strands_along_normals, smooth_strands, delete_strands
- **Instances**: create_instances, bake_instanced_geometry

### FIELDS & VOLUMES
- **Field Creation**: scalar_field, vector_field, position_field, sphere_field
- **Noise Fields**: fractal_noise_field, curl_noise_field, simplex_noise_field
- **Field Operations**: gradient_field, curl_field, smooth_field, warp_field
- **Volume Creation**: create_empty_volume, mesh_to_volume, points_to_volume
- **Volume Editing**: resample_volume, offset_level_set, smooth_voxel_property
- **Volume Operations**: coarsen_refine, rebuild_level_set, invert_level_set
- **Meshing**: volume_to_mesh, contour_surface_nets

### SIMULATION SYSTEMS
- **Particles**: simulate_particles, source_particles, particle_solver_settings
- **Aero (Smoke/Fire)**: simulate_aero, source_air, source_fuel, aero_solver_settings
- **Liquids (FLIP)**: simulate_liquid, source_liquid, liquid_solver_settings
- **MPM (Sand/Snow)**: simulate_mpm, source_mpm_sand, source_mpm_snow
- **Rigid Bodies**: simulate_rigid_bodies, create_rigid_bodies, constrain_in_radius
- **Ocean**: create_spectral_waves, simulate_dynamic_wave, displace_by_wave
- **Influences**: gravity_influence, wind_influence, turbulence_influence, collider
- **Utilities**: memory_cache, file_cache, compute_velocity, should_simulate

### FILE I/O
- **Alembic**: read_Alembic, write_Alembic
- **OpenVDB**: read_OpenVDB, write_OpenVDB, read_OpenVDB_points
- **Bifrost Native**: read_Bifrost_object, write_Bifrost_object
- **Images**: read_texture, write_texture, sample_texture
- **NumPy**: read_NumPy, write_NumPy, query_NumPy
- **Other Formats**: read_PDC, read_Field3d

### RENDERING
- **Materials**: assign_material, standard_surface_mat, constant_surface_mat
- **Arnold Volume**: Arnold_standard_volume_mat, set_Arnold_volume_settings
- **Arnold Mesh**: set_Arnold_mesh_settings, set_Arnold_points_settings
- **Viewport**: set_viewport_volume_settings
- **Motion Blur**: set_motion_blur_mode
- **Output**: final_mode

### RIGGING SYSTEMS
- **Skeleton**: construct_skeleton, create_skeleton_from_paths, validate_skeleton
- **IK Solvers**: solve_limb_IK, aim_matrix, blend_matrix
- **Modules**: root_module, spine_module, arm_module, leg_module
- **Converters**: skeleton_to_points, skeleton_to_strands, points_to_skeleton

### DIAGNOSTICS & DEBUGGING
- **Visualization**: point_scope, mesh_scope, volume_scope, field_scope
- **Debug Output**: dump_object, log_message
- **Profiling**: profiler_start, profiler_end

### SPECIALIZED SYSTEMS
- **Machine Learning**: layer_linear, activation_ReLU, activation_sigmoid
- **Wedging**: wedge_parameter, wedge_index, applied_wedge_parameter
- **Set Operations**: set_union, set_intersection, set_difference
- **Scatter Utilities**: build_alias_table, sample_alias_table

## Common Workflows

### Basic Mesh Workflow
```
1. construct_mesh (or create_mesh_*)
2. update_mesh_normals
3. set_geo_property (for custom properties)
4. validate_mesh
5. assign_material
6. final_mode
```

### Point Scattering & Instancing
```
1. scatter_points (on surface)
2. randomize_point_scale / randomize_point_rotation
3. create_instances (with instance geometry)
4. final_mode
```

### Volume Creation & Meshing
```
1. mesh_to_level_set (or points_to_volume)
2. offset_level_set / smooth_level_set_property
3. volume_to_mesh
4. update_mesh_normals
5. final_mode
```

### Particle Simulation
```
1. source_particles (emitter)
2. particle_solver_settings
3. Add influences (gravity_influence, wind_influence, etc.)
4. simulate_particles
5. memory_cache / file_cache
6. final_mode
```

### Smoke/Fire Simulation
```
1. source_air / source_fuel
2. aero_solver_settings
3. Add influences (buoyancy, turbulence, etc.)
4. simulate_aero
5. Arnold_standard_volume_mat
6. final_mode
```

### Liquid Simulation
```
1. source_liquid (emitter)
2. liquid_solver_settings
3. create_static_collider (for collision objects)
4. simulate_liquid
5. Extract surface mesh
6. file_cache
7. final_mode
```

### Field-Based Deformation
```
1. Create field (fractal_noise_field, sphere_field, etc.)
2. sample_field (at point positions)
3. Use sampled values to modify positions/properties
4. set_point_position
5. final_mode
```

### Rigging Setup
```
1. create_skeleton_from_paths
2. Add modules (spine_module, arm_module, etc.)
3. solve_limb_IK (for IK chains)
4. blend_matrix (for FK/IK blending)
5. transform_joints
6. skeleton_to_strands (for visualization)
```

## Data Type Reference

### Common Types
- **float**: Single floating-point number
- **float2**: 2D vector (UV coordinates)
- **float3**: 3D vector (position, direction, color RGB)
- **float4**: 4D vector (quaternion, color RGBA)
- **float4x4**: 4x4 matrix (transform)
- **int/uint**: Integer (signed/unsigned)
- **bool**: Boolean true/false
- **string**: Text string
- **any**: Generic type (auto-converts)

### Geometry Types
- **mesh**: Polygon mesh with faces
- **points**: Point cloud
- **strands**: Curve/strand geometry (hair, fur)
- **volume**: Sparse voxel volume
- **skeleton**: Hierarchical joint structure
- **instances**: Instance references
- **field**: Lazily-evaluated spatial function

### Arrays
- Arrays indicated by [] suffix: float[], float3[], uint[]
- Arrays are dynamic and can be resized
- Index from 0 to (size-1)
- Use array operations for efficiency

## Property Naming Conventions

### Standard Properties
- **point_position**: Point positions (float3[])
- **point_normal**: Point normals (float3[])
- **point_velocity**: Point velocities (float3[])
- **point_size**: Point size/radius (float[])
- **point_id**: Point IDs (uint[])
- **point_orientation**: Point orientation (float4[] quaternions)

### Mesh Properties
- **face_offset**: Face vertex offsets (uint[])
- **face_vertex**: Face vertex indices (uint[])
- **face_normal**: Face normals (float3[])
- **face_center**: Face centers (float3[])
- **face_vertex_uv**: UV indices (uint[])
- **uv_list**: UV coordinates (float2[])

### Strand Properties
- **point_offset**: Strand point offsets (uint[])
- **strand_size**: Strand width (float[])
- **point_tangent**: Tangent vectors (float3[])
- **point_strand_index**: Strand ID per point (uint[])

### Volume Properties
- **voxel_signed_distance**: Signed distance field (float[])
- **voxel_fog_density**: Fog density (float[])
- **voxel_velocity**: Velocity field (float3[])
- **voxel_temperature**: Temperature field (float[])

### Simulation Properties
- **particle_age**: Particle age (float[])
- **particle_mass**: Particle mass (float[])
- **particle_state**: Particle state flags (uint[])
- **velocity**: Velocity (float3[])
- **angular_velocity**: Angular velocity (float3[])

## Performance Considerations

### Optimization Tips
1. **Use accelerators** for repeated spatial queries (build_closest_accelerator)
2. **Batch operations** - operate on arrays rather than individual elements
3. **Cache expensive results** - use memory_cache or file_cache
4. **Choose appropriate resolution** - voxel size for volumes, point density for particles
5. **Filter early** - remove unnecessary geometry before heavy operations
6. **Profile** - use profiler_start/profiler_end to identify bottlenecks

### Memory Management
- Volumes use sparse storage - only active voxels consume memory
- Large arrays can be memory-intensive - filter/cull when possible
- Instance geometry is memory-efficient (shared geometry)
- Simulation caches grow with frame count - manage cache size

### GPU Acceleration
- Many volume operations are GPU-accelerated
- Simulation solvers can use GPU (check solver settings)
- Rendering uses GPU for viewport/Arnold

## Common Gotchas

1. **Face winding order matters** - CCW = front-facing
2. **Array indices are 0-based** - first element is index 0
3. **Quaternions use (x,y,z,w) format** - w is scalar component
4. **Level sets use signed distance** - negative = inside, positive = outside
5. **Properties are strings** - typos will create new properties instead of error
6. **Transform hierarchy needs parent indices** - use -1 for root
7. **Time step affects simulation stability** - smaller = more stable but slower
8. **Fields are lazy** - not computed until sampled
9. **Some nodes modify input** - others return new geometry
10. **File paths need proper formatting** - use forward slashes or proper escaping

## Namespace Organization

Bifrost nodes use :: namespace separation:
- **Core::Math** - Math operations
- **Core::Array** - Array operations  
- **Core::Logic** - Logic operations
- **Core::String** - String operations
- **Core::Transform** - Transform operations
- **Geometry::Mesh** - Mesh operations
- **Geometry::Points** - Point operations
- **Geometry::Strands** - Strand operations
- **Geometry::Properties** - Property management
- **Geometry::Query** - Spatial queries
- **Geometry::Volume** - Volume operations
- **Modeling::Primitive** - Primitive creation
- **Modeling::Mesh** - Mesh editing
- **Modeling::Points** - Point editing
- **Simulation::Particles** - Particle simulation
- **Simulation::Aero** - Smoke/fire simulation
- **Simulation::Liquids** - Liquid simulation
- **Simulation::MPM** - Material point method
- **Simulation::RigidBodies** - Rigid body dynamics
- **Simulation::Ocean** - Ocean/wave simulation
- **Simulation::Influence** - Forces/influences
- **File::Geometry** - Geometry file I/O
- **File::Image** - Image file I/O
- **Rendering::Materials** - Material assignment
- **Rendering::Arnold** - Arnold renderer settings
- **Rigging::Skeleton** - Skeleton operations
- **Rigging::Solver** - IK/constraint solvers
- **Diagnostic::Display** - Visualization scopes

## Version Notes

This reference covers Bifrost nodes as of the documentation provided. Node availability and functionality may vary by Maya/Bifrost version. Always check the specific version documentation for your installation.

## Additional Resources

For detailed parameter descriptions, see the individual part documents:
- bifrost_ref_01_core_geometry.md
- bifrost_ref_02_modeling.md
- bifrost_ref_03_fields_volumes.md
- bifrost_ref_04_simulation_rendering.md
- bifrost_ref_05_core_math_arrays.md
- bifrost_ref_06_rigging_specialized.md

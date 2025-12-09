# Bifrost Reference Part 3: Fields, Volumes & Simulation

## CORE::FIELDS - Field Creation & Operations

**scalar_field** - Creates scalar field from constant or function
- Inputs: value (float or function)
- Outputs: field

**vector_field** - Creates vector field from constant or function
- Inputs: value (float3 or function)
- Outputs: field

**position_field** - Creates field that returns query position
- Inputs: none
- Outputs: field (returns position at query point)

**to_field** - Converts value/array to field
- Inputs: value (any)
- Outputs: field

**to_vector_field** - Converts to vector field
- Inputs: value (float3 or float)
- Outputs: vector_field

**sample_field** - Samples field at positions
- Inputs: field, positions (float3[])
- Outputs: values (array)

**sample_field_with_proxies** - Samples with proxy property evaluation
- Inputs: field, positions (float3[]), geometry (for properties)
- Outputs: values (array)

**field_is_empty** - Checks if field is empty
- Inputs: field
- Outputs: is_empty (bool)

**switch_fields** - Selects field based on condition
- Inputs: condition (bool or field), field_true, field_false
- Outputs: field

**mask_field** - Masks field with boolean field
- Inputs: field, mask_field
- Outputs: field (masked)

## CORE::FIELDS - Field Shapes

**sphere_field** - Creates spherical field
- Inputs: center (float3), radius (float), falloff (float)
- Outputs: field

**plane_field** - Creates planar field
- Inputs: origin (float3), normal (float3), falloff (float)
- Outputs: field

**superquadric_shape_field** - Creates superquadric shape field
- Inputs: center (float3), scale (float3), exponents (float2)
- Outputs: field

**near_point_field** - Creates field based on distance to points
- Inputs: points, max_distance (float)
- Outputs: field

**closest_point_field** - Creates field that returns closest point info
- Inputs: geometry
- Outputs: field (returns closest point data)

**voxel_field** - Creates field from voxel volume
- Inputs: volume
- Outputs: field

**voxel_proxy_field** - Creates proxy field for voxel data
- Inputs: volume, property_name (string)
- Outputs: field

**property_proxy_field** - Creates proxy field for geometry properties
- Inputs: geometry, property_name (string)
- Outputs: field

## CORE::FIELDS - Noise & Procedural Fields

**fractal_noise_field** - Fractal noise field (fBm)
- Inputs: octaves (int), amplitude (float), frequency (float), lacunarity (float)
- Outputs: field

**fractal_turbulence_field** - Turbulence noise field
- Inputs: octaves (int), amplitude (float), frequency (float), lacunarity (float)
- Outputs: field

**fractal_block_noise_field** - Block/cellular noise
- Inputs: octaves (int), amplitude (float), frequency (float)
- Outputs: field

**fractal_disturbance_field** - Disturbance pattern
- Inputs: octaves (int), amplitude (float), frequency (float)
- Outputs: field

**curl_noise_field** - Curl noise (divergence-free)
- Inputs: octaves (int), amplitude (float), frequency (float)
- Outputs: vector_field

**simplex_noise_field** - Simplex noise
- Inputs: amplitude (float), frequency (float)
- Outputs: field

## CORE::FIELDS - Field Transformations

**transform_field** - Transforms field by matrix
- Inputs: field, transform (float4x4)
- Outputs: field

**translate_field** - Translates field
- Inputs: field, translation (float3)
- Outputs: field

**rotate_field** - Rotates field
- Inputs: field, rotation (float4 quaternion), pivot (float3)
- Outputs: field

**scale_field** - Scales field
- Inputs: field, scale (float or float3), pivot (float3)
- Outputs: field

**warp_field** - Warps field using displacement field
- Inputs: field, displacement_field (vector), strength (float)
- Outputs: field

**advect_field** - Advects field along vector field
- Inputs: field, velocity_field (vector), time_step (float)
- Outputs: field

## CORE::FIELDS - Field Operations

**gradient_field** - Computes gradient (spatial derivative)
- Inputs: field
- Outputs: vector_field (gradient)

**curl_field** - Computes curl
- Inputs: vector_field
- Outputs: vector_field (curl)

**divergence_field** - Computes divergence
- Inputs: vector_field
- Outputs: scalar_field (divergence)

**smooth_field** - Smooths field
- Inputs: field, iterations (int), strength (float)
- Outputs: field

**fcurve_field** - Remaps field using animation curve
- Inputs: field, fcurve
- Outputs: field

## GEOMETRY::VOLUME - Volume Creation

**create_empty_volume** - Creates empty volume
- Inputs: voxel_size (float), bounds (optional)
- Outputs: volume

**field_to_volume** - Converts field to volume
- Inputs: field, voxel_size (float), bounds
- Outputs: volume

**mesh_to_volume** - Converts mesh to signed distance field volume
- Inputs: mesh, voxel_size (float), bandwidth (float)
- Outputs: volume

**mesh_to_level_set** - Converts mesh to level set
- Inputs: mesh, voxel_size (float), bandwidth (float)
- Outputs: volume

**points_to_volume** - Converts points to fog volume
- Inputs: points, voxel_size (float), radius (float)
- Outputs: volume

**points_to_level_set** - Converts points to level set
- Inputs: points, voxel_size (float), radius (float)
- Outputs: volume

## GEOMETRY::VOLUME - Volume Properties

**get_voxel_position** - Gets voxel center positions
- Inputs: volume
- Outputs: positions (float3[])

**get_filtered_voxel_position** - Gets positions of active voxels only
- Inputs: volume
- Outputs: positions (float3[])

**get_voxel_signed_distance** - Gets signed distance values
- Inputs: volume
- Outputs: distances (float[])

**set_voxel_signed_distance** - Sets signed distance values
- Inputs: volume, distances (float[])
- Outputs: volume

**get_voxel_fog_density** - Gets fog density values
- Inputs: volume
- Outputs: densities (float[])

**set_voxel_fog_density** - Sets fog density values
- Inputs: volume, densities (float[])
- Outputs: volume

**get_voxel_velocity** - Gets velocity values
- Inputs: volume
- Outputs: velocities (float3[])

**set_voxel_velocity** - Sets velocity values
- Inputs: volume, velocities (float3[])
- Outputs: volume

## GEOMETRY::VOLUME - Volume Operations

**resample_volume** - Resamples volume to new resolution
- Inputs: volume, voxel_size (float)
- Outputs: volume

**coarsen_refine** - Adaptively coarsens/refines volume
- Inputs: volume, tolerance (float)
- Outputs: volume

**coarsen_voxel_property** - Coarsens specific property
- Inputs: volume, property_name (string), levels (int)
- Outputs: volume

**offset_level_set** - Offsets level set surface
- Inputs: volume, distance (float)
- Outputs: volume

**rebuild_level_set** - Rebuilds level set to fix artifacts
- Inputs: volume
- Outputs: volume

**resize_level_set** - Changes level set bandwidth
- Inputs: volume, new_bandwidth (float)
- Outputs: volume

**invert_level_set** - Inverts inside/outside
- Inputs: volume
- Outputs: volume

**close_holes_in_level_set** - Fills holes in level set
- Inputs: volume, max_hole_size (float)
- Outputs: volume

**smooth_level_set_property** - Smooths level set values
- Inputs: volume, iterations (int), strength (float)
- Outputs: volume

**smooth_voxel_property** - Smooths voxel property
- Inputs: volume, property_name (string), iterations (int)
- Outputs: volume

**sharpen_voxel_property** - Sharpens voxel property
- Inputs: volume, property_name (string), iterations (int)
- Outputs: volume

**remap_property** - Remaps voxel values
- Inputs: volume, property_name (string), input_range (float2), output_range (float2)
- Outputs: volume

**grade_volume** - Adjusts volume values (levels adjustment)
- Inputs: volume, black_point (float), white_point (float), gamma (float)
- Outputs: volume

**analyze_volume** - Computes volume statistics
- Inputs: volume
- Outputs: voxel_count, active_voxel_count, min_value, max_value, total_value

**get_volume_tile_info** - Gets tile tree structure info
- Inputs: volume
- Outputs: tile_info (structure)

**volume_bounds** - Gets volume bounding box
- Inputs: volume
- Outputs: min_position (float3), max_position (float3)

**update_voxel_position** - Updates voxel world positions after transform
- Inputs: volume
- Outputs: volume

**splat_points_into_volume** - Splats point values into volume
- Inputs: volume, points, property_name (string), accumulation_mode (string)
- Outputs: volume

## GEOMETRY::VOLUME - Level Set Operations

**fog_density_to_level_set** - Converts fog to level set
- Inputs: volume, iso_value (float)
- Outputs: volume

**level_set_to_fog_density** - Converts level set to fog
- Inputs: volume
- Outputs: volume

**points_to_liquid_surface** - Creates liquid surface from particles
- Inputs: points, voxel_size (float), radius (float)
- Outputs: volume (level set)

## GEOMETRY::VOLUME - Meshing

**volume_to_mesh** - Converts volume to mesh
- Inputs: volume, iso_value (float), adaptivity (float)
- Outputs: mesh

**contour_surface_nets** - Surface nets contouring
- Inputs: volume, iso_value (float)
- Outputs: mesh

**contour_dual_marching_cubes** - Dual marching cubes
- Inputs: volume, iso_value (float)
- Outputs: mesh

## SIMULATION::COMMON - Simulation Utilities

**should_simulate** - Checks if simulation should run
- Inputs: enable (bool), frame (float)
- Outputs: should_run (bool)

**compute_on_frame** - Triggers computation on specific frame
- Inputs: frame (float), trigger_frame (float)
- Outputs: trigger (bool)

**set_initial_state** - Sets initial simulation state
- Inputs: geometry, use_initial_state (bool)
- Outputs: geometry

**memory_cache** - Caches data in memory
- Inputs: data (any), frame (float)
- Outputs: data

**file_cache** - Caches data to disk
- Inputs: data (any), filepath (string), frame (float)
- Outputs: data

**compute_velocity** - Computes velocity from position history
- Inputs: current_position (float3), previous_position (float3), time_step (float)
- Outputs: velocity (float3)

**compute_point_velocities** - Computes velocities for point cloud
- Inputs: current_geometry, previous_geometry, time_step (float)
- Outputs: velocity (float3[])

**collider** - Creates collision object
- Inputs: geometry, type (string: "static"/"animated")
- Outputs: collider

**generate_pulse** - Generates timed pulse signal
- Inputs: start_frame (float), duration (float), current_frame (float)
- Outputs: pulse_value (float)

**source_color_property** - Sets color property for simulation source
- Inputs: geometry, color (float3 or field)
- Outputs: geometry

**vary_source_property** - Adds variation to source property
- Inputs: geometry, property_name (string), variation (float), seed (int)
- Outputs: geometry

## SIMULATION::INFLUENCE - Force & Influence Types

**gravity_influence** - Gravity force
- Inputs: magnitude (float), direction (float3)
- Outputs: influence

**drag_influence** - Drag/friction force
- Inputs: magnitude (float)
- Outputs: influence

**wind_influence** - Wind force
- Inputs: direction (float3), magnitude (float), turbulence (float)
- Outputs: influence

**vortex_influence** - Vortex/tornado force
- Inputs: axis (float3), magnitude (float), falloff (float)
- Outputs: influence

**turbulence_influence** - Turbulence noise force
- Inputs: magnitude (float), frequency (float), octaves (int)
- Outputs: influence

**attract_repulse_influence** - Point attractor/repulsor
- Inputs: position (float3), magnitude (float), mode (string: "attract"/"repulse")
- Outputs: influence

**radial_influence** - Radial push/pull force
- Inputs: center (float3), magnitude (float)
- Outputs: influence

**volume_influence** - Volume-based force
- Inputs: volume, property (string), magnitude (float)
- Outputs: influence

**vdb_influence** - VDB volume influence
- Inputs: volume, magnitude (float)
- Outputs: influence

**collide_field_influence** - Collision with field
- Inputs: field, collision_offset (float)
- Outputs: influence

**mask_influence** - Masks other influences
- Inputs: mask (field or bool[]), magnitude (float)
- Outputs: influence

**kill_influence** - Kills/removes particles
- Inputs: kill_field or kill_threshold
- Outputs: influence

**kill_plane_influence** - Kills particles crossing plane
- Inputs: plane_origin (float3), plane_normal (float3)
- Outputs: influence

**dissipation_influence** - Dissipates/fades values
- Inputs: rate (float)
- Outputs: influence

**buoyancy_influence** - Buoyancy force
- Inputs: magnitude (float), reference_density (float)
- Outputs: influence

**ground_plane_influence** - Ground plane collision
- Inputs: height (float), friction (float), bounce (float)
- Outputs: influence

**boundary_drag_influence** - Drag at boundaries
- Inputs: magnitude (float)
- Outputs: influence

**guiding_influence** - Guides towards target
- Inputs: target_velocity (field), strength (float)
- Outputs: influence

**dilate_influence** - Dilates values
- Inputs: rate (float)
- Outputs: influence

**clamp_influence** - Clamps values to range
- Inputs: min_value (float), max_value (float)
- Outputs: influence

**modifier_influence** - Modifies property values
- Inputs: property_name (string), operation (string), value (float or field)
- Outputs: influence

**modulate_influence** - Modulates influence by field
- Inputs: base_influence, modulation_field, amount (float)
- Outputs: influence

**influence_set_property** - Sets property value
- Inputs: property_name (string), value (float or field)
- Outputs: influence

**influence_set_orientation** - Sets orientation
- Inputs: orientation (float4 or field)
- Outputs: influence

**influence_set_spin** - Sets angular velocity
- Inputs: spin (float3 or field)
- Outputs: influence

## SIMULATION::INFLUENCE - Aero-Specific

**aero_einstein_influence** - Einstein drag model
- Inputs: drag_coefficient (float)
- Outputs: influence

**aero_pyroclastic_influence** - Pyroclastic effects
- Inputs: buoyancy (float), temperature_dissipation (float)
- Outputs: influence

**aero_erode_density_influence** - Density erosion
- Inputs: erosion_rate (float)
- Outputs: influence

**aero_noise_transport_influence** - Noise-based transport
- Inputs: noise_amplitude (float), noise_frequency (float)
- Outputs: influence

**fractal_disturbance_influence** - Fractal disturbance force
- Inputs: amplitude (float), frequency (float), octaves (int)
- Outputs: influence

**foam_advect_influence** - Foam advection
- Inputs: velocity_field
- Outputs: influence

# Bifrost Reference Part 4: Particles, Fluids, Rigid Bodies & Rendering

## SIMULATION::PARTICLES - Particle Simulation

**simulate_particles** - Main particle simulation solver
- Inputs: geometry, influences (array), solver_settings, time_step (float)
- Outputs: particles

**source_particles** - Emits particles
- Inputs: emitter_geometry, emission_rate (float or field), emission_type (string)
- Outputs: particles

**source_particle_rotations** - Sets initial rotation for emitted particles
- Inputs: particles, rotation (float4 or field), angular_velocity (float3 or field)
- Outputs: particles

**source_foam** - Emits foam particles
- Inputs: liquid_simulation, foam_rate (float)
- Outputs: foam_particles

**basic_particles_graph** - Complete particle setup template
- Inputs: emitter, influences
- Outputs: particles

**particle_solver_settings** - Particle solver configuration
- Inputs: gravity (float3), drag (float), time_scale (float)
- Outputs: settings

**get_particle_solver_settings** - Gets current solver settings
- Inputs: particles
- Outputs: settings

**get_particle_solver_properties** - Gets solver state properties
- Inputs: particles
- Outputs: time, frame, time_step

**set_particles** - Sets particle state
- Inputs: particles, property_updates
- Outputs: particles

**get_particles** - Gets particle state
- Inputs: particles
- Outputs: point_position, point_velocity, other properties

**filter_particles** - Filters particles by mask/tag
- Inputs: particles, mask (bool[]) or tag_expression (string)
- Outputs: particles

**property_kill_points** - Removes particles based on property
- Inputs: particles, property_name (string), threshold (float), comparison (string)
- Outputs: particles

**get_normalized_age** - Gets particle age normalized to lifespan
- Inputs: particles
- Outputs: normalized_age (float[])

**set_particle_property_from_age** - Sets property based on age
- Inputs: particles, property_name (string), ramp (curve)
- Outputs: particles

**set_orientation_value** - Sets particle orientation
- Inputs: particles, orientation (float4 or float4[])
- Outputs: particles

**set_spin_value** - Sets particle angular velocity
- Inputs: particles, spin (float3 or float3[])
- Outputs: particles

**create_particle_trails** - Creates trails from particle motion
- Inputs: particles, trail_length (int)
- Outputs: strands

**preserve_foam_volume_settings** - Foam volume preservation settings
- Inputs: enable (bool), target_volume (float)
- Outputs: settings

## SIMULATION::AERO - Smoke/Fire Simulation

**simulate_aero** - Main smoke/fire solver
- Inputs: volume, influences (array), solver_settings, time_step (float)
- Outputs: volume

**source_air** - Emits air/smoke
- Inputs: emitter_geometry, density (float or field), temperature (float or field)
- Outputs: volume_update

**source_fuel** - Emits fuel for combustion
- Inputs: emitter_geometry, fuel_amount (float or field)
- Outputs: volume_update

**basic_aero_graph** - Complete smoke setup template
- Inputs: emitters, influences
- Outputs: volume

**basic_combustion_graph** - Complete fire setup template
- Inputs: emitters, influences
- Outputs: volume

**aero_solver_settings** - Smoke solver configuration
- Inputs: voxel_size (float), gravity (float3), time_scale (float)
- Outputs: settings

**aero_combustion_settings** - Fire/combustion settings
- Inputs: ignition_temperature (float), burn_rate (float), expansion (float)
- Outputs: settings

**aero_adaptivity_settings** - Adaptive resolution settings
- Inputs: enable (bool), min_voxel_size (float), max_voxel_size (float)
- Outputs: settings

**aero_refinement_settings** - Refinement control
- Inputs: refine_threshold (float), coarsen_threshold (float)
- Outputs: settings

**aero_uvw_settings** - Texture coordinate settings
- Inputs: mode (string), scale (float3)
- Outputs: settings

**post_refine_aero** - Post-process after simulation
- Inputs: volume
- Outputs: volume

**condense_water_vapor** - Condenses vapor to liquid
- Inputs: volume, condensation_rate (float)
- Outputs: volume

**aero_color_post_process** - Color processing for render
- Inputs: volume, color_mapping
- Outputs: volume

## SIMULATION::LIQUIDS - Liquid Simulation (FLIP)

**simulate_liquid** - Main liquid solver
- Inputs: particles, influences (array), solver_settings, colliders
- Outputs: particles, surface_mesh

**source_liquid** - Emits liquid particles
- Inputs: emitter_geometry, emission_rate (float)
- Outputs: particles

**basic_liquid_graph** - Complete liquid setup template
- Inputs: emitters, colliders
- Outputs: particles, mesh

**liquid_solver_settings** - Liquid solver configuration
- Inputs: particle_separation (float), surface_tension (float), viscosity (float)
- Outputs: settings

**liquid_scope** - Liquid simulation scope/container
- Inputs: particles, influences
- Outputs: scoped_simulation

**guided_liquid_settings** - Guided simulation settings (for directing liquid flow)
- Inputs: guide_strength (float), guide_velocity_field
- Outputs: settings

**guided_liquid_alpha_field** - Creates alpha blend field for guiding
- Inputs: geometry, falloff (float)
- Outputs: alpha_field

**liquid_guide_waves** - Guides liquid with wave motion
- Inputs: particles, wave_height (float), wave_frequency (float)
- Outputs: particles

**liquid_guide_spectral_waves** - Guides with ocean spectrum waves
- Inputs: particles, spectrum_settings
- Outputs: particles

**simulate_particle_foam** - Simulates foam particles from liquid
- Inputs: liquid_particles, foam_settings
- Outputs: foam_particles

**get_points_from_tile_tree** - Extracts points from tiled structure
- Inputs: tile_tree
- Outputs: points

## SIMULATION::MPM - Material Point Method (Sand/Snow/etc)

**simulate_mpm** - Main MPM solver
- Inputs: particles, influences (array), solver_settings
- Outputs: particles

**source_mpm_sand** - Creates sand material
- Inputs: emitter_geometry, density (float)
- Outputs: mpm_particles

**source_mpm_snow** - Creates snow material
- Inputs: emitter_geometry, density (float)
- Outputs: mpm_particles

**source_mpm_fluid** - Creates MPM fluid
- Inputs: emitter_geometry, density (float)
- Outputs: mpm_particles

**source_mpm_rubber** - Creates elastic rubber material
- Inputs: emitter_geometry, youngs_modulus (float), poissons_ratio (float)
- Outputs: mpm_particles

**source_mpm_gel** - Creates gel/soft body material
- Inputs: emitter_geometry, stiffness (float)
- Outputs: mpm_particles

**make_mpm_cloth** - Creates cloth from mesh
- Inputs: mesh, density (float), stiffness (float)
- Outputs: mpm_particles

**make_mpm_shell** - Creates thin shell structure
- Inputs: mesh, thickness (float), material_properties
- Outputs: mpm_particles

**make_mpm_fiber** - Creates fiber material
- Inputs: strands, fiber_properties
- Outputs: mpm_particles

**constrain_mpm** - Constrains MPM particles
- Inputs: mpm_particles, constraint_geometry
- Outputs: mpm_particles

**mpm_solver_settings** - MPM solver configuration
- Inputs: particle_spacing (float), material_type (string), time_scale (float)
- Outputs: settings

**mpm_snow_scope** - Snow-specific simulation scope
- Inputs: particles, temperature (float)
- Outputs: scoped_simulation

**split_points_by_material** - Splits MPM particles by material type
- Inputs: mpm_particles
- Outputs: particles_by_material (array)

## SIMULATION::RIGID_BODIES - Rigid Body Dynamics

**simulate_rigid_bodies** - Main rigid body solver
- Inputs: rigid_bodies, constraints (array), solver_settings
- Outputs: rigid_bodies

**create_rigid_bodies** - Creates rigid bodies from geometry
- Inputs: geometry, density (float), collision_shape (string)
- Outputs: rigid_bodies

**create_rigid_box** - Creates box rigid body
- Inputs: size (float3), density (float)
- Outputs: rigid_body

**create_rigid_sphere** - Creates sphere rigid body
- Inputs: radius (float), density (float)
- Outputs: rigid_body

**create_rigid_capsule** - Creates capsule rigid body
- Inputs: radius (float), height (float), density (float)
- Outputs: rigid_body

**create_rigid_cylinder** - Creates cylinder rigid body
- Inputs: radius (float), height (float), density (float)
- Outputs: rigid_body

**create_static_collider** - Creates non-moving collision object
- Inputs: geometry, collision_shape (string)
- Outputs: collider

**create_animated_collider** - Creates keyframe-animated collision object
- Inputs: geometry, velocity (float3)
- Outputs: collider

**basic_rigid_body_graph** - Complete rigid body setup
- Inputs: geometry, constraints
- Outputs: rigid_bodies

**basic_rigid_body_instance_graph** - Instanced rigid body setup
- Inputs: points, instance_geometry
- Outputs: instances (simulated)

**rigid_body_solver_settings** - Rigid body solver config
- Inputs: gravity (float3), iterations (int), time_scale (float)
- Outputs: settings

**set_rigid_properties** - Sets rigid body properties
- Inputs: rigid_bodies, mass (float), friction (float), restitution (float)
- Outputs: rigid_bodies

**merge_rigid_bodies** - Merges multiple rigid body simulations
- Inputs: rigid_bodies_array
- Outputs: rigid_bodies

**rigid_body_instance** - Creates instanced rigid bodies
- Inputs: points, instance_rigid_body
- Outputs: instances

**constrain_in_radius** - Constrains bodies within radius
- Inputs: rigid_bodies, center (float3), radius (float)
- Outputs: constraints

**sample_and_constrain** - Samples and creates constraints
- Inputs: rigid_bodies, constraint_geometry
- Outputs: constraints

**constraint_scope** - Constraint definition scope
- Inputs: constraint_type (string), parameters
- Outputs: constraint

**constraint_strength_influence** - Modulates constraint strength
- Inputs: constraints, strength_field
- Outputs: constraints

**constraint_reconnect_influence** - Reconnects broken constraints
- Inputs: constraints, reconnect_threshold (float)
- Outputs: constraints

**constraint_id_mask_influence** - Masks constraints by ID
- Inputs: constraints, id_mask (bool[])
- Outputs: constraints

**convex_decomposition_scope** - Convex decomposition settings
- Inputs: max_hulls (int), resolution (int)
- Outputs: settings

## SIMULATION::OCEAN - Ocean/Wave Simulation

**create_spectral_waves** - Creates ocean spectrum waves
- Inputs: resolution (int), wave_height (float), wind_speed (float), wind_direction (float3)
- Outputs: wave_data

**simulate_dynamic_wave** - Simulates shallow water waves
- Inputs: wave_heightfield, influences (array), solver_settings
- Outputs: wave_heightfield

**source_dynamic_wave** - Emits dynamic wave sources
- Inputs: emitter_geometry, amplitude (float)
- Outputs: wave_update

**basic_dynamic_wave_graph** - Complete dynamic wave setup
- Inputs: emitters, influences
- Outputs: wave_heightfield

**compute_spectral_ocean_volume** - Creates volume from spectrum
- Inputs: wave_data, depth (float)
- Outputs: volume

**displace_by_wave** - Displaces geometry by wave
- Inputs: geometry, wave_data
- Outputs: geometry (displaced)

**sample_wave_data** - Samples wave at positions
- Inputs: wave_data, positions (float3[])
- Outputs: heights (float[]), velocities (float3[])

**sample_wave_property** - Samples specific wave property
- Inputs: wave_data, property_name (string), positions (float3[])
- Outputs: values (array)

**scale_wave_height** - Scales wave amplitude
- Inputs: wave_data, scale (float)
- Outputs: wave_data

**create_wave_map** - Creates wave influence map
- Inputs: geometry, resolution (int2)
- Outputs: wave_map

**create_geo_wave_map** - Creates geometric wave map
- Inputs: geometry
- Outputs: wave_map

**dynamic_wave_settings** - Dynamic wave solver settings
- Inputs: cell_size (float), damping (float), time_scale (float)
- Outputs: settings

**simulate_foam** - Simulates ocean foam
- Inputs: wave_data, foam_settings
- Outputs: foam_particles

**wave_set_foam** - Sets foam properties on waves
- Inputs: wave_data, foam_amount (float)
- Outputs: wave_data

**split_image_into_low_high_frequencies** - Frequency separation for waves
- Inputs: image, cutoff_frequency (float)
- Outputs: low_freq_image, high_freq_image

## FILE::GEOMETRY - File I/O

**read_Alembic** - Reads Alembic file
- Inputs: filepath (string), frame (float), object_path (string)
- Outputs: geometry

**write_Alembic** - Writes Alembic file
- Inputs: geometry, filepath (string), frame (float)
- Outputs: success (bool)

**read_OpenVDB** - Reads OpenVDB file
- Inputs: filepath (string), grid_name (string)
- Outputs: volume

**read_OpenVDB_volume** - Reads VDB volume
- Inputs: filepath (string), grid_name (string)
- Outputs: volume

**read_OpenVDB_points** - Reads VDB points
- Inputs: filepath (string)
- Outputs: points

**write_OpenVDB** - Writes OpenVDB file
- Inputs: volume, filepath (string), grid_name (string)
- Outputs: success (bool)

**write_OpenVDB_volume** - Writes VDB volume
- Inputs: volume, filepath (string), grid_name (string)
- Outputs: success (bool)

**write_OpenVDB_points** - Writes VDB points
- Inputs: points, filepath (string)
- Outputs: success (bool)

**read_Bifrost_object** - Reads native Bifrost file
- Inputs: filepath (string), frame (float)
- Outputs: geometry

**write_Bifrost_object** - Writes native Bifrost file
- Inputs: geometry, filepath (string), frame (float)
- Outputs: success (bool)

**read_Field3d** - Reads Field3D file
- Inputs: filepath (string), field_name (string)
- Outputs: volume

**write_Field3d** - Writes Field3D file
- Inputs: volume, filepath (string), field_name (string)
- Outputs: success (bool)

**read_PDC** - Reads Maya PDC particle cache
- Inputs: filepath (string), frame (float)
- Outputs: points

**write_PDC** - Writes Maya PDC cache
- Inputs: points, filepath (string), frame (float)
- Outputs: success (bool)

**read_bif_particles** - Reads Bifrost particle cache
- Inputs: filepath (string), frame (float)
- Outputs: particles

## FILE::IMAGE - Image/Texture I/O

**read_texture** - Reads image file as texture
- Inputs: filepath (string)
- Outputs: texture

**write_texture** - Writes texture to file
- Inputs: texture, filepath (string)
- Outputs: success (bool)

**read_image_data** - Reads raw image data
- Inputs: filepath (string)
- Outputs: image_data (array), width (int), height (int)

**construct_image** - Creates image from data array
- Inputs: pixel_data (array), width (int), height (int), channels (int)
- Outputs: image

**construct_texture** - Creates texture from image
- Inputs: image, settings
- Outputs: texture

**get_image_structure** - Gets image dimensions
- Inputs: image
- Outputs: width (int), height (int), channels (int)

**get_texture_structure** - Gets texture info
- Inputs: texture
- Outputs: width, height, channels, wrap_mode, filter_mode

**sample_texture** - Samples texture at UV coordinates
- Inputs: texture, uv_coords (float2[])
- Outputs: colors (float3[] or float4[])

**sample_texture_file** - Samples texture directly from file
- Inputs: filepath (string), uv_coords (float2[])
- Outputs: colors (array)

**set_texture_settings** - Sets texture wrap/filter modes
- Inputs: texture, wrap_mode (string), filter_mode (string)
- Outputs: texture

**is_an_image** - Checks if object is image
- Inputs: object
- Outputs: is_image (bool)

**is_a_texture** - Checks if object is texture
- Inputs: object
- Outputs: is_texture (bool)

**validate_image** - Validates image structure
- Inputs: image
- Outputs: is_valid (bool)

**validate_texture** - Validates texture
- Inputs: texture
- Outputs: is_valid (bool)

**texture_scope** - Texture scope for sampling
- Inputs: texture
- Outputs: scoped_texture

**create_texture_samples** - Creates UV sample locations
- Inputs: count (int), distribution (string)
- Outputs: uv_samples (float2[])

**accumulate_color_texture_samples** - Accumulates texture samples
- Inputs: samples (array), colors (array)
- Outputs: accumulated_texture

**bake_texture_samples** - Bakes samples to texture
- Inputs: samples, resolution (int2)
- Outputs: texture

## FILE::NUMPY - NumPy File I/O

**read_NumPy** - Reads .npy file
- Inputs: filepath (string)
- Outputs: array (any type)

**write_NumPy** - Writes .npy file
- Inputs: array (any), filepath (string)
- Outputs: success (bool)

**query_NumPy** - Queries .npy file info without loading
- Inputs: filepath (string)
- Outputs: shape (uint[]), dtype (string)

## FILE::PROJECT - Scene Info

**scene_info** - Gets Maya scene information
- Inputs: none
- Outputs: scene_name (string), fps (float), start_frame (float), end_frame (float)

## RENDERING::MATERIALS - Material Assignment

**assign_material** - Assigns material to geometry
- Inputs: geometry, material
- Outputs: geometry

**standard_surface_mat** - Creates standard surface shader
- Inputs: base_color (float3), metalness (float), roughness (float), specular (float)
- Outputs: material

**constant_surface_mat** - Creates constant/unlit shader
- Inputs: color (float3)
- Outputs: material

**get_materials** - Gets assigned materials
- Inputs: geometry
- Outputs: materials (array)

**set_geo_property_reference** - References geometry property in shader
- Inputs: material, shader_parameter (string), geo_property (string)
- Outputs: material

## RENDERING::ARNOLD - Arnold Renderer Settings

**Arnold_standard_volume_mat** - Arnold volume shader
- Inputs: density (float or field), scatter_color (float3), temperature (float)
- Outputs: material

**set_Arnold_volume_settings** - Sets Arnold volume render settings
- Inputs: volume, step_size (float), samples (int)
- Outputs: volume

**set_Arnold_mesh_settings** - Sets Arnold mesh settings
- Inputs: mesh, subdiv_type (string), subdiv_iterations (int)
- Outputs: mesh

**set_Arnold_points_settings** - Sets Arnold points settings
- Inputs: points, point_type (string: "sphere"/"disk"/etc), min_pixel_width (float)
- Outputs: points

**set_Arnold_strands_settings** - Sets Arnold strands settings
- Inputs: strands, mode (string), width (float)
- Outputs: strands

**set_Arnold_geo_settings** - Sets general Arnold geometry settings
- Inputs: geometry, visibility (int), matte (bool)
- Outputs: geometry

**Arnold_Alembic_instance** - Creates Arnold Alembic procedural
- Inputs: points, alembic_file (string), object_path (string)
- Outputs: instances

**Arnold_ray_bitmask** - Creates ray visibility bitmask
- Inputs: camera (bool), shadow (bool), diffuse (bool), specular (bool), reflection (bool)
- Outputs: bitmask (int)

## RENDERING::VIEWPORT - Viewport Display

**set_viewport_volume_settings** - Controls volume display in viewport
- Inputs: volume, density_scale (float), scatter_color (float3)
- Outputs: volume

## RENDERING::MOTION_BLUR - Motion Blur

**set_motion_blur_mode** - Sets motion blur calculation mode
- Inputs: geometry, mode (string: "off"/"velocity"/"deformation")
- Outputs: geometry

## RENDERING::TERMINALS - Output Nodes

**final_mode** - Terminal output node for render
- Inputs: geometry
- Outputs: (connects to Maya output)

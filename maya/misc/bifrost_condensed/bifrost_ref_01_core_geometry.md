# Bifrost Reference Part 1: Core Geometry & Mesh Operations

## GEOMETRY::MESH - Mesh Construction & Structure

**construct_mesh** - Creates mesh from point positions, face offsets, and face vertices
- Inputs: point_position (float3[]), face_offset (uint[]), face_vertex (uint[])
- Outputs: mesh

**get_mesh_structure** - Returns arrays describing mesh topology
- Inputs: mesh
- Outputs: point_position, face_offset, face_vertex, point_count, face_count, face_vertex_count

**get_mesh_UVs** - Gets UV texture coordinates
- Inputs: mesh
- Outputs: face_vertex_uv, uv_list, uvw_list

**set_mesh_UVs** - Sets UV texture coordinates
- Inputs: mesh, face_vertex_uv (uint[]), uv_list (float2[])
- Outputs: mesh

**triangulate_mesh** - Converts all faces to triangles
- Inputs: mesh
- Outputs: mesh

**validate_mesh** - Checks if mesh has valid structure
- Inputs: mesh
- Outputs: is_valid (bool)

**update_mesh_adjacency** - Computes point/face neighbor relationships
- Inputs: mesh
- Outputs: mesh (with adjacency data)

**update_mesh_normals** - Computes face and vertex normals
- Inputs: mesh
- Outputs: mesh (with normal properties)

**update_face_normals** - Computes face normals only
- Inputs: mesh
- Outputs: mesh

**update_face_vertex_normals** - Computes vertex normals with angle-based smoothing
- Inputs: mesh, max_angle_in_degrees
- Outputs: mesh

**smooth_mesh** - Applies Laplacian smoothing to mesh
- Inputs: mesh, iterations (int), strength (float)
- Outputs: mesh

**soften_harden_edges** - Controls edge smoothing by angle
- Inputs: mesh, max_smooth_angle
- Outputs: mesh

**compute_mesh_volume** - Calculates enclosed volume
- Inputs: mesh
- Outputs: volume (float)

**find_mesh_islands** - Identifies disconnected mesh components
- Inputs: mesh
- Outputs: island_id (per face), island_count

**update_face_centers** - Computes face centroid positions
- Inputs: mesh
- Outputs: mesh

**subdivide_mesh** - Catmull-Clark subdivision
- Inputs: mesh, levels (int)
- Outputs: mesh

**sqrt3_subdivide_mesh** - √3-subdivision scheme
- Inputs: mesh, levels (int)
- Outputs: mesh

## GEOMETRY::MESH - Face Operations

**faces_to_points** - Converts faces to point cloud at face centers
- Inputs: mesh, delete_geometry (bool)
- Outputs: points

**face_group_to_points** - Converts tagged faces to points
- Inputs: mesh, tag_expression (string)
- Outputs: points

**points_to_faces** - Converts points back to faces
- Inputs: points
- Outputs: mesh

## GEOMETRY::POINTS - Point Cloud Operations

**construct_points** - Creates point geometry from positions
- Inputs: point_position (float3[])
- Outputs: points

**get_points_structure** - Gets point data arrays
- Inputs: points
- Outputs: point_position, point_count

**get_bounding_box** - Computes axis-aligned bounding box
- Inputs: points
- Outputs: min_position (float3), max_position (float3)

**validate_points** - Checks if points structure is valid
- Inputs: points
- Outputs: is_valid (bool)

**filter_points** - Selects subset of points by tag/mask
- Inputs: points, mask (bool[]), tag_expression (string)
- Outputs: points

## GEOMETRY::PROPERTIES - Property Management

**get_geo_property** - Retrieves property array from geometry
- Inputs: geometry, property (string), type
- Outputs: data (array of specified type)

**set_geo_property** - Sets property array on geometry
- Inputs: geometry, property (string), data (array), target_component (string)
- Outputs: geometry

**get_geo_property_check** - Gets property with existence check
- Inputs: geometry, property (string), type
- Outputs: data (array), property_exists (bool)

**get_geo_property_or_default** - Gets property or returns default
- Inputs: geometry, property (string), default_value
- Outputs: data (array)

**erase_geo_properties** - Removes properties by name pattern
- Inputs: geometry, property_expression (string)
- Outputs: geometry

**copy_properties** - Copies properties between geometries
- Inputs: source_geometry, target_geometry, property_expression (string)
- Outputs: target_geometry

**set_geo_property_data** - Sets property from raw array
- Inputs: geometry, property (string), target_component (string), data_type, data (any[])
- Outputs: geometry

**append_to_geo_property** - Appends values to existing property
- Inputs: geometry, property (string), values (array), target_component
- Outputs: geometry

**remove_from_geo_property** - Removes values from property by indices
- Inputs: geometry, property (string), indices (uint[])
- Outputs: geometry

**get_geo_component_count** - Gets number of components (points/faces/etc)
- Inputs: geometry, component_type (string)
- Outputs: count (uint)

**get_geo_component_indices** - Gets indices of all components
- Inputs: geometry, component_type (string)
- Outputs: indices (uint[])

## GEOMETRY::PROPERTIES - Standard Properties

**get_point_position** - Gets point positions
- Inputs: geometry
- Outputs: point_position (float3[])

**set_point_position** - Sets point positions
- Inputs: geometry, point_position (float3[])
- Outputs: geometry

**get_point_normal** - Gets point normals
- Inputs: geometry
- Outputs: point_normal (float3[])

**set_point_normal** - Sets point normals
- Inputs: geometry, point_normal (float3[])
- Outputs: geometry

**get_point_velocity** - Gets point velocities
- Inputs: geometry
- Outputs: point_velocity (float3[])

**set_point_velocity** - Sets point velocities
- Inputs: geometry, point_velocity (float3[])
- Outputs: geometry

**set_point_shape** - Sets point size/radius
- Inputs: geometry, point_size (float or float[])
- Outputs: geometry

**get_point_count** - Gets number of points
- Inputs: geometry
- Outputs: point_count (uint)

## GEOMETRY::STRANDS - Strand/Curve Operations

**construct_strands** - Creates strand geometry from points and counts
- Inputs: point_position (float3[]), point_offset (uint[])
- Outputs: strands

**create_strands_from_counts** - Creates strands from point counts per strand
- Inputs: point_position (float3[]), strand_count (uint[])
- Outputs: strands

**get_strands_structure** - Gets strand topology arrays
- Inputs: strands
- Outputs: point_position, point_offset, strand_count, point_count

**resample_strands** - Resamples strands to uniform point count
- Inputs: strands, points_per_strand (int)
- Outputs: strands

**set_strands_shape** - Sets strand width/size
- Inputs: strands, strand_size (float or float[])
- Outputs: strands

**update_strands_tangents** - Computes tangent vectors along strands
- Inputs: strands
- Outputs: strands

**update_strands_basis** - Computes orientation frame along strands
- Inputs: strands
- Outputs: strands

**update_strands_length** - Computes length of each strand
- Inputs: strands
- Outputs: strands

**strands_basis_to_orientation** - Converts basis frame to quaternion orientation
- Inputs: strands
- Outputs: strands

**update_strands_point_neighbors** - Finds prev/next point on strand
- Inputs: strands
- Outputs: strands

**update_point_strand_index** - Assigns strand ID to each point
- Inputs: strands
- Outputs: strands

**validate_strands** - Checks if strand structure is valid
- Inputs: strands
- Outputs: is_valid (bool)

## GEOMETRY::TOPOLOGY - Topology Operations

**add_points** - Adds new points to existing geometry
- Inputs: geometry, point_position (float3[]), other properties
- Outputs: geometry

## GEOMETRY::QUERY - Spatial Queries

**build_closest_accelerator** - Creates spatial acceleration structure for closest point queries
- Inputs: geometry
- Outputs: accelerator

**build_raycast_accelerator** - Creates acceleration structure for raycasting
- Inputs: geometry
- Outputs: accelerator

**get_closest_point** - Finds closest point on geometry
- Inputs: geometry, query_position (float3)
- Outputs: closest_position (float3), distance (float)

**get_closest_locations** - Gets closest surface locations
- Inputs: geometry, query_positions (float3[])
- Outputs: locations, distances (float[])

**get_points_in_radius** - Finds all points within radius
- Inputs: geometry, center (float3), radius (float)
- Outputs: point_indices (uint[]), distances (float[])

**get_raycast_locations** - Performs ray intersection tests
- Inputs: geometry, ray_start (float3), ray_direction (float3)
- Outputs: locations, hit_distances (float[])

**sample_closest_accelerator** - Samples closest point using accelerator
- Inputs: accelerator, query_positions (float3[])
- Outputs: locations

**sample_raycast_accelerator** - Samples raycast using accelerator
- Inputs: accelerator, ray_starts (float3[]), ray_directions (float3[])
- Outputs: locations

**sample_property** - Samples property at surface locations
- Inputs: geometry, property (string), locations
- Outputs: sampled_values (array)

**sample_property_2D** - Samples property using 2D parametric coordinates
- Inputs: geometry, property (string), uv_coordinates (float2[])
- Outputs: sampled_values (array)

**generate_sample_locations** - Generates random sample locations on surface
- Inputs: geometry, count (int), seed (int)
- Outputs: locations

**location_is_valid** - Checks if location object is valid
- Inputs: location
- Outputs: is_valid (bool)

## GEOMETRY::TAGS - Component Tagging

**set_component_tag** - Tags components (points/faces) with boolean mask
- Inputs: geometry, tag (string), mask (bool[]), target_component (string)
- Outputs: geometry

**get_component_tag** - Gets tag mask for components
- Inputs: geometry, tag (string), target_component (string)
- Outputs: mask (bool[])

**resolve_tag_expression** - Evaluates tag expression to boolean mask
- Inputs: geometry, tag_expression (string), target_component (string)
- Outputs: mask (bool[])

**interpret_auto_port_as_component_tag** - Converts various inputs to tag mask
- Inputs: geometry, value (auto), target_component (string)
- Outputs: mask (bool[])

## GEOMETRY::INSTANCES - Instancing

**geo_instance** - Creates instances from point cloud
- Inputs: points, instance_geometry (geometry to instance)
- Outputs: instances

**compound_instance** - Creates hierarchical instance structure
- Inputs: instances[]
- Outputs: compound_instance

**procedural_instance** - Creates procedural instances with variation
- Inputs: points, instance_geometries[], selection_weights (float[])
- Outputs: instances

**selector_instance** - Selects instances based on property
- Inputs: points, instance_geometries[], selection_property (string)
- Outputs: instances

**set_instance_geometry** - Changes instance target geometry
- Inputs: instances, geometry
- Outputs: instances

**set_instance_shape** - Sets instance scale/rotation
- Inputs: instances, scale (float3), orientation (float4)
- Outputs: instances

**filter_instances** - Filters instances by tag/mask
- Inputs: instances, mask (bool[])
- Outputs: instances

**render_archive_instance** - Creates render archive instance (for Arnold/etc)
- Inputs: points, archive_path (string), object_path (string)
- Outputs: instances

## GEOMETRY::COMMON - Utility Functions

**get_geo_schema_type** - Gets geometry type (mesh/points/strands/volume)
- Inputs: geometry
- Outputs: schema_type (string)

**invalid_index** - Returns invalid index value
- Inputs: none
- Outputs: invalid_index (uint = 4294967295)

**switch_is_a** - Type-based switch routing
- Inputs: geometry, type_to_match (string)
- Outputs: is_match (bool)

**interpret_auto_port_as_scalar** - Converts various inputs to scalar
- Inputs: value (auto)
- Outputs: scalar_value (float)

**interpret_auto_port_as_vector** - Converts various inputs to vector
- Inputs: value (auto)
- Outputs: vector_value (float3)

**interpret_auto_port_as_color** - Converts various inputs to color
- Inputs: value (auto)
- Outputs: color_value (float3 or float4)

**interpret_auto_port_as_string** - Converts various inputs to string
- Inputs: value (auto)
- Outputs: string_value (string)

**compute_bounding_sphere** - Computes bounding sphere
- Inputs: geometry
- Outputs: center (float3), radius (float)

**compute_best_fit_transform** - Computes best-fit rigid transform between point sets
- Inputs: source_positions (float3[]), target_positions (float3[])
- Outputs: transform (float4x4)

**compute_best_fit_rotation** - Computes best-fit rotation between point sets
- Inputs: source_positions (float3[]), target_positions (float3[])
- Outputs: rotation (float4x4)

**access_offset_array** - Accesses elements from offset array structure
- Inputs: offset_array (uint[]), data_array (any[]), index (uint)
- Outputs: elements (array slice)

**filter_offset_array** - Filters offset array by mask
- Inputs: offset_array (uint[]), data_array (any[]), mask (bool[])
- Outputs: filtered_offset_array, filtered_data_array

**sample_any_array_by_weighted_sum** - Samples array using weighted interpolation
- Inputs: array (any[]), indices (uint[]), weights (float[])
- Outputs: interpolated_value

**match_property_expression** - Tests if property name matches expression
- Inputs: property_name (string), expression (string)
- Outputs: matches (bool)

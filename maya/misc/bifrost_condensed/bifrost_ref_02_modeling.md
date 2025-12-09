# Bifrost Reference Part 2: Modeling & Deformation

## MODELING::PRIMITIVE - Primitive Creation

**create_mesh_cube** - Creates box primitive
- Inputs: size (float3), divisions (int3)
- Outputs: mesh

**create_mesh_sphere** - Creates sphere primitive
- Inputs: radius (float), divisions_u (int), divisions_v (int)
- Outputs: mesh

**create_mesh_cylinder** - Creates cylinder primitive
- Inputs: radius (float), height (float), divisions_radial (int), divisions_height (int), divisions_cap (int)
- Outputs: mesh

**create_mesh_torus** - Creates torus primitive
- Inputs: major_radius (float), minor_radius (float), divisions_major (int), divisions_minor (int)
- Outputs: mesh

**create_mesh_capsule** - Creates capsule primitive
- Inputs: radius (float), height (float), divisions (int)
- Outputs: mesh

**create_mesh_plane** - Creates plane primitive
- Inputs: size (float2), divisions (int2)
- Outputs: mesh

## MODELING::MESH - Mesh Editing

**delete_faces** - Removes faces from mesh
- Inputs: mesh, mask (bool[]) or tag_expression (string)
- Outputs: mesh

**delete_mesh_points** - Removes unused points after face deletion
- Inputs: mesh, keep_points_with_properties (bool)
- Outputs: mesh

**delete_isolated_points** - Removes points not used by any face
- Inputs: mesh
- Outputs: mesh

**find_isolated_points** - Identifies points not used by faces
- Inputs: mesh
- Outputs: isolated_point_mask (bool[])

**filter_faces** - Selects faces by mask/tag
- Inputs: mesh, mask (bool[]), tag_expression (string)
- Outputs: mesh

**separate_mesh** - Splits mesh into separate components
- Inputs: mesh, separation_tag (string)
- Outputs: meshes (array of meshes)

**extrude_faces** - Extrudes selected faces
- Inputs: mesh, face_mask (bool[]), distance (float), scale (float)
- Outputs: mesh

**detach_faces** - Detaches faces by duplicating shared vertices
- Inputs: mesh, face_mask (bool[])
- Outputs: mesh

**disconnect_mesh_faces** - Disconnects all faces (splits shared vertices)
- Inputs: mesh
- Outputs: mesh

**reverse_face_orientations** - Flips face normals
- Inputs: mesh, face_mask (bool[])
- Outputs: mesh

**unify_face_orientations** - Makes face orientations consistent
- Inputs: mesh
- Outputs: mesh

**find_face_orientations** - Identifies consistently vs inconsistently oriented faces
- Inputs: mesh
- Outputs: consistent_mask (bool[])

**boolean_meshes** - Boolean operations (union/subtract/intersect)
- Inputs: mesh_a, mesh_b, operation (string: "union"/"subtract"/"intersect")
- Outputs: mesh

**fracture_mesh** - Fractures mesh using cutting planes
- Inputs: mesh, cutter_geometry, seed (int)
- Outputs: fractured_meshes (array)

**voronoi_fracture_mesh** - Fractures mesh using Voronoi cells
- Inputs: mesh, cell_points (float3[]), cell_count (int)
- Outputs: fractured_meshes (array)

**boolean_fracture_mesh** - Fractures using boolean operations
- Inputs: mesh, cutter_mesh
- Outputs: fractured_meshes (array)

**compute_convex_hull** - Creates convex hull
- Inputs: points or mesh
- Outputs: hull_mesh

**compute_voronoi_diagram** - Generates 3D Voronoi diagram
- Inputs: points, bounds (optional mesh)
- Outputs: voronoi_cells (meshes array)

**cluster_voronoi_shards** - Groups small Voronoi fragments
- Inputs: voronoi_shards (meshes[]), min_volume (float)
- Outputs: clustered_meshes (array)

## MODELING::MESH - UV Operations

**create_UVs_from_projection_planes** - Projects UVs from planes
- Inputs: mesh, projection_type (string: "planar"/"cylindrical"/"spherical")
- Outputs: mesh (with UVs)

**layout_UVs** - Unwraps and packs UVs
- Inputs: mesh, resolution (int), padding (float)
- Outputs: mesh (with laid out UVs)

**sample_mesh_UVs** - Samples UVs at surface locations
- Inputs: mesh, locations
- Outputs: uv_values (float2[])

## MODELING::POINTS - Point Operations

**scatter_points** - Scatters points on surface
- Inputs: mesh, density (float) or count (int), seed (int)
- Outputs: points

**scatter_points_blue_noise** - Scatters points with blue noise distribution
- Inputs: mesh, density (float) or count (int), min_radius (float), seed (int)
- Outputs: points

**duplicate_points** - Duplicates points N times
- Inputs: points, count (int)
- Outputs: points

**cull_overlapping_points** - Removes points within radius of each other
- Inputs: points, radius (float)
- Outputs: points

**delete_points_in_points** - Removes specified points
- Inputs: points, mask (bool[])
- Outputs: points

**cull_points** - Removes points by various criteria
- Inputs: points, mask (bool[]) or tag_expression (string)
- Outputs: points

**transform_points** - Applies transform matrix to points
- Inputs: points, transform (float4x4)
- Outputs: points

**translate_points** - Moves points by offset
- Inputs: points, translation (float3 or float3[])
- Outputs: points

**rotate_points** - Rotates points
- Inputs: points, rotation (quaternion or euler), pivot (float3)
- Outputs: points

**scale_points** - Scales points
- Inputs: points, scale (float or float3), pivot (float3)
- Outputs: points

**displace_points** - Displaces points along normals
- Inputs: points, distance (float or float[]), use_normal (bool)
- Outputs: points

**orient_points_by_geometry** - Aligns points to surface normals
- Inputs: points, target_geometry
- Outputs: points (with orientation)

**randomize_point_translation** - Adds random offset to positions
- Inputs: points, min_offset (float3), max_offset (float3), seed (int)
- Outputs: points

**randomize_point_rotation** - Adds random rotation
- Inputs: points, min_rotation (float3), max_rotation (float3), seed (int)
- Outputs: points

**randomize_point_scale** - Adds random scale variation
- Inputs: points, min_scale (float or float3), max_scale (float or float3), seed (int)
- Outputs: points

**randomize_selection** - Randomly selects subset of points
- Inputs: points, probability (float), seed (int)
- Outputs: selection_mask (bool[])

**randomize_selection_by_probabilities** - Randomly selects using per-point probabilities
- Inputs: points, probabilities (float[]), seed (int)
- Outputs: selection_mask (bool[])

## MODELING::STRANDS - Strand Editing

**create_arrow_strands** - Creates arrow-shaped strands (for vector visualization)
- Inputs: positions (float3[]), directions (float3[]), length (float)
- Outputs: strands

**create_strands_along_normals** - Creates strands extruded from surface
- Inputs: geometry, length (float), segments (int)
- Outputs: strands

**create_strands_around_strands** - Creates spiral strands around existing strands
- Inputs: strands, count (int), radius (float)
- Outputs: strands

**delete_strands** - Removes strands
- Inputs: strands, mask (bool[])
- Outputs: strands

**delete_strands_points** - Removes specific points from strands
- Inputs: strands, point_mask (bool[])
- Outputs: strands

**filter_strands** - Filters strands by mask/tag
- Inputs: strands, mask (bool[]) or tag_expression (string)
- Outputs: strands

**separate_strands** - Splits strands into separate components
- Inputs: strands, separation_tag (string)
- Outputs: strands_array (array)

**smooth_strands** - Smooths strand shapes
- Inputs: strands, iterations (int), strength (float)
- Outputs: strands

**set_strands_size_profile** - Sets varying width along strands
- Inputs: strands, size_profile (float[]), blend (float)
- Outputs: strands

**points_array_to_strand_trails** - Converts per-frame point arrays to motion trails
- Inputs: points_array (points[])
- Outputs: strands

## MODELING::COMMON - General Modeling

**merge_geometry** - Combines multiple geometries into one
- Inputs: geometries (array)
- Outputs: merged_geometry

**delete_points** - Generic point deletion
- Inputs: geometry, mask (bool[])
- Outputs: geometry

## MODELING::INSTANCES - Instancing Operations

**create_instances** - Creates instances from points
- Inputs: points, instance_geometry
- Outputs: instances

**bake_instanced_geometry** - Converts instances to real geometry
- Inputs: instances
- Outputs: baked_geometry (merged mesh/points)

**flatten_instance_selection** - Evaluates procedural instance selection
- Inputs: procedural_instances
- Outputs: instances (with resolved selection)

## MODELING::CONVERTERS - Geometry Conversion

**convert_to_volume** - Converts geometry to volume
- Inputs: geometry, voxel_size (float), bandwidth (float)
- Outputs: volume

## GEOMETRY::TAGS - Advanced Tagging

**tag_by_threshold** - Tags components above/below threshold
- Inputs: geometry, property (string), threshold (float), comparison (string)
- Outputs: geometry (with tag)

**tag_by_expression** - Tags using expression evaluation
- Inputs: geometry, expression (string), target_component (string)
- Outputs: geometry (with tag)

**tag_by_angle_between_vectors** - Tags based on angle test
- Inputs: geometry, vector_a_property (string), vector_b_property (string), angle_threshold (float)
- Outputs: geometry (with tag)

**tag_inside_geometry** - Tags components inside another geometry
- Inputs: geometry, test_geometry, target_component (string)
- Outputs: geometry (with tag)

**tag_randomly** - Randomly tags components
- Inputs: geometry, probability (float), seed (int), target_component (string)
- Outputs: geometry (with tag)

**tag_strand_ends** - Tags first/last points of strands
- Inputs: strands, tag_first (bool), tag_last (bool)
- Outputs: strands (with tag)

**convert_tag** - Converts tag from one component type to another
- Inputs: geometry, tag (string), source_component (string), target_component (string)
- Outputs: geometry

## GEOMETRY::TRANSFER - Property Transfer

**transfer_properties_by_indices** - Transfers properties using index mapping
- Inputs: source_geometry, target_geometry, indices (uint[]), property_expression (string)
- Outputs: target_geometry

**transfer_properties_by_2d_indices** - Transfers using 2D index pairs
- Inputs: source_geometry, target_geometry, indices_2d (uint2[]), property_expression (string)
- Outputs: target_geometry

**transfer_properties_by_weighted_sum** - Transfers using weighted interpolation
- Inputs: source_geometry, target_geometry, indices (uint[][]), weights (float[][]), property_expression
- Outputs: target_geometry

## MODELING::KNITS - Knit/Fabric Simulation

**create_stitch** - Creates knit stitch pattern
- Inputs: template, parameters
- Outputs: stitch_mesh

**create_stitch_template** - Creates stitch template definition
- Inputs: pattern_type (string)
- Outputs: template

**create_strands_from_stitch_mesh** - Converts stitch mesh to yarn strands
- Inputs: stitch_mesh
- Outputs: yarn_strands

**validate_stitch_mesh** - Validates stitch mesh structure
- Inputs: stitch_mesh
- Outputs: is_valid (bool)

**view_stitch_template** - Visualizes stitch template
- Inputs: template
- Outputs: visualization_mesh

## CORE::OBJECT - Object/Property Operations

**create_object_from_schema** - Creates object from schema definition
- Inputs: schema_name (string)
- Outputs: object

**get_property** - Gets property from object
- Inputs: object, property_name (string)
- Outputs: value

**set_property** - Sets property on object
- Inputs: object, property_name (string), value
- Outputs: object

**has_property** - Checks if object has property
- Inputs: object, property_name (string)
- Outputs: has_property (bool)

**erase_property** - Removes property from object
- Inputs: object, property_name (string)
- Outputs: object

**extract_property** - Extracts and removes property from object
- Inputs: object, property_name (string)
- Outputs: object, value

**get_property_keys** - Gets all property names
- Inputs: object
- Outputs: keys (string[])

**get_sub_object** - Gets nested sub-object
- Inputs: object, path (string)
- Outputs: sub_object

**set_sub_object** - Sets nested sub-object
- Inputs: object, path (string), sub_object
- Outputs: object

**is_a** - Checks if object is of specific type
- Inputs: object, type_name (string)
- Outputs: is_type (bool)

**is_empty** - Checks if object is empty
- Inputs: object
- Outputs: is_empty (bool)

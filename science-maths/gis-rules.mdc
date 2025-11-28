# GIS Rules and Guidelines

When working with Geographic Information Systems (GIS), follow these comprehensive rules to ensure accurate, reliable, and professional spatial data analysis and visualisation.

## Coordinate Reference Systems (CRS)

- **Always know your CRS.** Every spatial dataset must have a defined coordinate reference system. Never work with spatial data without understanding its CRS.
- **Document CRS information** for all datasets, including the EPSG code, datum, and projection method.
- **Reproject data explicitly** when combining datasets with different CRSs. Never assume coordinates are in the same system.
- **Choose appropriate CRSs** for your analysis:
  - Use local projected CRSs for regional analysis (e.g., UTM zones for local areas)
  - Use geographic CRSs (lat/lon) for global datasets or when storing original data
  - Use equal-area projections for area calculations
  - Use equidistant projections for distance measurements
- **Verify CRS transformations** by checking coordinates before and after reprojection.
- **Be aware of CRS limitations.** Some projections distort area, distance, or shape; choose based on your analysis needs.
- **Use EPSG codes** consistently to reference CRSs (e.g., EPSG:4326 for WGS84, EPSG:3857 for Web Mercator).
- **Check for CRS mismatches** when performing spatial operations; many tools require matching CRSs.

## Spatial Data Formats

- **Understand vector vs raster data** and choose the appropriate format for your use case:
  - Vector: Points, lines, polygons (shapefiles, GeoJSON, GeoPackage, KML)
  - Raster: Gridded data (GeoTIFF, NetCDF, ASCII Grid)
- **Prefer modern formats** over legacy ones:
  - Use GeoPackage instead of shapefiles when possible (single file, better data types, no 2GB limit)
  - Use GeoJSON for web applications and data exchange
  - Use GeoTIFF for raster data with proper georeferencing
- **Include metadata** with spatial data files. Document data source, collection date, CRS, and any processing steps.
- **Validate file integrity** before processing, especially for shapefiles (check all required files: .shp, .shx, .dbf, .prj).
- **Handle large datasets appropriately:**
  - Use spatial indexing for efficient queries
  - Consider tiling or chunking for very large rasters
  - Use database formats (PostGIS, SpatiaLite) for large vector datasets
- **Preserve coordinate precision** by using appropriate numeric types (avoid unnecessary rounding).

## Data Quality and Validation

- **Validate geometry integrity** before analysis:
  - Check for invalid geometries (self-intersections, holes, degenerate polygons)
  - Fix topology errors (gaps, overlaps, slivers)
  - Ensure polygons are closed and valid
- **Check for duplicate features** and decide whether to remove or merge them based on your use case.
- **Validate attribute data** separately from geometry; ensure data types match expectations.
- **Document data quality issues** and any assumptions made during cleaning.
- **Verify spatial relationships** match expectations (e.g., points fall within expected polygons).
- **Check for coordinate system errors** (e.g., lat/lon swapped, wrong hemisphere, incorrect units).
- **Validate extent and bounds** to ensure data falls within expected geographic area.
- **Handle null or empty geometries** explicitly; don't silently ignore them.

## Spatial Data Types and Operations

- **Understand fundamental spatial data types:**
  - Points: Single coordinates (locations, events)
  - Lines: Sequences of connected points (roads, rivers, boundaries)
  - Polygons: Closed areas (administrative boundaries, land parcels)
  - Multi-geometries: Collections of the above
- **Use appropriate spatial operations:**
  - Intersection: Find overlapping areas
  - Union: Combine geometries
  - Buffer: Create zones around features
  - Difference: Remove one geometry from another
  - Clip: Cut data to an extent
- **Consider topology** when performing spatial operations:
  - Adjacent polygons should share boundaries
  - Lines should connect at nodes
  - No gaps or overlaps in coverage
- **Handle edge cases** in spatial operations (empty results, disjoint geometries, boundary conditions).
- **Use spatial indexing** (R-tree, quadtree) for efficient spatial queries on large datasets.
- **Understand coordinate precision** and its impact on spatial operations (floating-point errors, snapping).

## Spatial Analysis Methods

- **Choose appropriate analysis methods** based on your question and data type:
  - Point pattern analysis: Nearest neighbour, kernel density, spatial autocorrelation
  - Network analysis: Shortest path, service areas, accessibility
  - Surface analysis: Slope, aspect, hillshade, viewshed
  - Overlay analysis: Intersection, union, identity operations
- **Consider spatial autocorrelation** in your analysis; nearby features are often similar (violates independence assumptions).
- **Account for edge effects** in spatial analysis, especially for density calculations and interpolation.
- **Use appropriate distance measures:**
  - Euclidean distance for projected coordinates
  - Great circle distance for geographic coordinates
  - Network distance for routing problems
- **Validate analysis results** against known patterns or ground truth when possible.
- **Document analysis parameters** (buffer distances, search radii, interpolation methods) for reproducibility.
- **Consider scale and resolution** in your analysis; results may vary at different scales.

## Raster Data Handling

- **Understand raster properties:**
  - Cell size (resolution)
  - Extent (spatial bounds)
  - NoData values
  - Data type (integer, float)
- **Handle NoData values explicitly** in raster calculations; don't assume they're zero.
- **Resample rasters carefully** when changing resolution; choose appropriate resampling method (nearest, bilinear, cubic).
- **Align raster grids** before performing raster operations; ensure cells align properly.
- **Use appropriate data types** for raster values to balance precision and storage:
  - Integer for categorical data
  - Float for continuous measurements
- **Consider memory usage** for large rasters; use tiling or chunking strategies.
- **Validate raster georeferencing** by checking corner coordinates and cell size.
- **Document raster metadata** including source, processing steps, and any transformations applied.

## Vector Data Handling

- **Maintain topology** when editing vector data to prevent gaps and overlaps.
- **Snap vertices** when creating or editing features to ensure connectivity.
- **Simplify geometries** when appropriate for visualisation, but preserve detail for analysis.
- **Handle multi-part geometries** correctly; understand when to split or merge features.
- **Validate attribute relationships** with geometry (e.g., area values match calculated geometry area).
- **Use appropriate geometry types** for your data (don't use polygons for point data).
- **Consider generalisation** for different map scales; detailed data may need simplification for small-scale maps.

## Spatial Queries and Filtering

- **Use spatial indexes** for efficient spatial queries on large datasets.
- **Combine spatial and attribute filters** when querying data.
- **Understand spatial predicate functions:**
  - Contains, Within, Intersects, Touches, Overlaps, Crosses, Disjoint
- **Test spatial queries** with known results to verify correctness.
- **Consider query performance** and optimise with appropriate indexes and filters.
- **Handle query edge cases** (boundary conditions, empty results, null geometries).

## Cartography and Visualisation

- **Choose appropriate symbology** for your data type and purpose:
  - Points: Size, colour, shape
  - Lines: Width, colour, pattern
  - Polygons: Fill colour, outline, pattern
- **Use colour thoughtfully:**
  - Sequential scales for ordered data
  - Diverging scales for data with meaningful centre
  - Qualitative scales for categorical data
  - Ensure accessibility (colour-blind friendly)
- **Include essential map elements:**
  - Title
  - Legend
  - Scale bar
  - North arrow (when orientation matters)
  - Data source and date
  - CRS information
- **Choose appropriate map projections** for visualisation based on your area of interest.
- **Avoid misleading visualisations:**
  - Don't use area-proportional symbols incorrectly
  - Don't truncate colour scales without indication
  - Don't use 3D when 2D would be clearer
- **Consider your audience** when choosing detail level and technical information to include.
- **Use consistent styling** across multiple maps in a series or report.
- **Label features appropriately** without cluttering the map; use label placement algorithms when needed.

## Geocoding and Address Matching

- **Understand geocoding limitations:**
  - Address formats vary by country
  - Not all addresses can be geocoded
  - Coordinates may be approximate
- **Validate geocoding results** by checking a sample against known locations.
- **Handle geocoding errors** and partial matches appropriately.
- **Document geocoding service** and parameters used (API, batch size, matching criteria).
- **Consider reverse geocoding** when you have coordinates but need addresses.
- **Respect rate limits** and terms of service for geocoding APIs.
- **Cache geocoding results** when possible to avoid redundant API calls.

## Spatial Databases

- **Use spatial databases** (PostGIS, SpatiaLite) for large or complex datasets:
  - Better performance for large datasets
  - Advanced spatial functions
  - Transaction support
  - Multi-user access
- **Create spatial indexes** on geometry columns for query performance.
- **Use appropriate geometry types** in database schemas (POINT, LINESTRING, POLYGON, etc.).
- **Validate geometries** when inserting into spatial databases.
- **Use spatial SQL functions** for efficient spatial queries and analysis.
- **Back up spatial databases** regularly, including both data and schema.
- **Document database schemas** including geometry columns, indexes, and spatial reference systems.

## Performance Optimisation

- **Use spatial indexes** for all spatial queries on large datasets.
- **Simplify geometries** for visualisation at small scales.
- **Tile or chunk large datasets** for processing and visualisation.
- **Use appropriate data formats** for your use case (vector vs raster, file vs database).
- **Profile spatial operations** to identify bottlenecks before optimising.
- **Consider caching** for expensive spatial calculations or web map tiles.
- **Use parallel processing** for independent spatial operations when possible.
- **Optimise attribute queries** separately from spatial queries when combining filters.

## Data Sources and Acquisition

- **Document data sources** including:
  - Origin and provider
  - Collection date and method
  - License and use restrictions
  - Data quality information
- **Verify data licenses** and usage rights before incorporating into projects.
- **Check data currency** and update schedules for time-sensitive analyses.
- **Validate downloaded data** against source documentation.
- **Handle different data formats** from various sources; standardise as needed.
- **Consider data costs** (API limits, licensing fees) when planning projects.
- **Back up original data** before processing or transformation.

## Spatial Statistics

- **Understand spatial autocorrelation** and its implications for statistical analysis.
- **Use appropriate spatial statistical methods:**
  - Spatial regression for spatially dependent data
  - Geographically weighted regression for local relationships
  - Spatial clustering analysis (e.g., Getis-Ord, Moran's I)
- **Account for spatial structure** in statistical models; don't ignore spatial dependencies.
- **Validate statistical assumptions** including spatial independence when required.
- **Report spatial statistics** with proper context and interpretation.
- **Consider multiple scales** in spatial statistical analysis; relationships may vary by scale.

## Web Mapping and Services

- **Use appropriate tile formats** for web maps (XYZ, TMS, WMTS).
- **Optimise data for web delivery:**
  - Simplify geometries
  - Reduce file sizes
  - Use appropriate formats (GeoJSON, TopoJSON, vector tiles)
- **Consider coordinate systems for web maps:**
  - Web Mercator (EPSG:3857) is standard but distorts area
  - Document when using non-standard CRSs
- **Handle projection on the fly** when serving data in different CRSs than the map.
- **Use caching strategies** for web map services to improve performance.
- **Implement proper error handling** for web map services and APIs.
- **Document API endpoints** and parameters for spatial web services.

## Version Control and Collaboration

- **Use version control** for GIS code and scripts, but be careful with large binary files.
- **Document processing workflows** so others can reproduce your analysis.
- **Share CRS and projection information** with all spatial data.
- **Use relative paths** in scripts to avoid hardcoded absolute paths.
- **Document environment setup** including GIS software versions and library dependencies.
- **Create reproducible workflows** that can be rerun on updated data.
- **Handle large spatial files** appropriately in version control (use Git LFS or external storage).

## Common GIS Tools and Libraries

### Python
- **GeoPandas:** Vector data manipulation and analysis
- **Rasterio:** Raster data I/O and processing
- **Shapely:** Geometric operations
- **Fiona:** Vector data I/O
- **PyProj:** Coordinate system transformations
- **Folium/Leaflet:** Interactive web maps
- **OSMnx:** OpenStreetMap data extraction

### R
- **sf:** Modern spatial data handling
- **raster:** Raster data manipulation
- **sp:** Legacy spatial data (being replaced by sf)
- **leaflet:** Interactive web maps
- **tmap:** Thematic mapping

### Desktop GIS
- **QGIS:** Open-source desktop GIS
- **ArcGIS:** Commercial GIS platform
- **GRASS GIS:** Advanced raster and vector analysis

### Web Mapping
- **Leaflet:** Lightweight web mapping library
- **OpenLayers:** Advanced web mapping framework
- **Mapbox GL JS:** Vector tile rendering
- **D3.js:** Custom map visualisations

## Error Handling and Validation

- **Validate input data** before processing (CRS, geometry validity, attribute types).
- **Handle errors gracefully** in spatial operations (empty results, invalid geometries, CRS mismatches).
- **Log spatial operations** for debugging and audit trails.
- **Test edge cases** (boundary conditions, empty datasets, null values).
- **Provide meaningful error messages** that help users understand and fix issues.
- **Validate output data** after processing to ensure operations completed correctly.

## Documentation and Metadata

- **Document all spatial data** with metadata including:
  - CRS and projection
  - Data source and collection date
  - Processing steps and transformations
  - Data quality information
  - Attribute definitions
- **Include CRS information** in all outputs and visualisations.
- **Document analysis methodology** including tools, parameters, and assumptions.
- **Create data dictionaries** for attribute fields with definitions and units.
- **Maintain processing logs** for complex workflows.
- **Document limitations** and known issues with datasets or analyses.

## Ethical and Legal Considerations

- **Respect data privacy** when working with location data:
  - Anonymise or aggregate sensitive locations
  - Consider re-identification risks
  - Follow data protection regulations
- **Understand licensing** and usage restrictions for spatial data.
- **Attribute data sources** appropriately in maps and publications.
- **Consider ethical implications** of spatial analysis, especially for vulnerable populations.
- **Respect terms of service** for geocoding APIs and data services.
- **Handle sensitive locations** (homes, protected areas) with appropriate care.

## Common Pitfalls to Avoid

- **Don't mix coordinate systems** without explicit transformation.
- **Don't ignore geometry validity** errors; fix them before analysis.
- **Don't assume data quality** without validation.
- **Don't use inappropriate projections** for your analysis type.
- **Don't ignore spatial autocorrelation** in statistical analysis.
- **Don't create misleading maps** with inappropriate symbology or scales.
- **Don't forget to document** CRS, data sources, and processing steps.
- **Don't use Web Mercator** for area calculations (it distorts area significantly).
- **Don't ignore edge effects** in spatial analysis.
- **Don't assume coordinates are in lat/lon** without verification.

## Best Practices Summary

- **Always know your CRS** and document it.
- **Validate geometry integrity** before analysis.
- **Choose appropriate data formats** for your use case.
- **Use spatial indexes** for performance.
- **Document everything:** data sources, processing steps, CRS, assumptions.
- **Test spatial operations** with known results.
- **Consider scale and resolution** in your analysis.
- **Handle errors and edge cases** explicitly.
- **Respect data licenses** and privacy concerns.
- **Create reproducible workflows** that others can follow.

---

**Remember:** GIS work requires attention to detail, especially regarding coordinate systems, data quality, and spatial relationships. The goal is accurate, reliable spatial analysis and visualisation. When in doubt, validate your data, document your process, and test your assumptions. Good GIS work is transparent, reproducible, and honest about limitations.


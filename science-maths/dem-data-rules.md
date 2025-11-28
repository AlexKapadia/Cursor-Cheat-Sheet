# DEM Data Rules and Guidelines

When working with Digital Elevation Model (DEM) data, follow these comprehensive rules to ensure accurate, reliable, and professional results.

## Understanding DEM Data

### DEM Fundamentals

- **Understand what DEM represents:** A DEM is a digital representation of the Earth's surface topography, typically stored as a raster grid where each cell contains an elevation value.
- **Know the difference between DEM, DTM, and DSM:**
  - **DEM:** Generic term for elevation models
  - **DTM (Digital Terrain Model):** Represents bare ground surface without vegetation or structures
  - **DSM (Digital Surface Model):** Includes all surface features (trees, buildings, etc.)
- **Understand coordinate systems:** DEMs use geographic (lat/lon) or projected coordinate systems. Always verify and document the CRS (Coordinate Reference System).
- **Know vertical datums:** Elevation values are relative to a vertical datum (e.g., NAVD88, EGM96, local sea level). Document which datum your DEM uses.
- **Understand resolution:** DEM resolution refers to ground sample distance (GSD) - the size of each pixel on the ground. Higher resolution means smaller pixel size and more detail.

### DEM Formats and Standards

- **Common formats:** GeoTIFF (.tif), ASCII Grid (.asc), BIL/BIP/BSQ, HDF, NetCDF, LAS/LAZ (for point clouds)
- **Prefer GeoTIFF** for most applications due to wide support and embedded georeferencing information.
- **Verify format compatibility** with your analysis tools before processing large datasets.
- **Check for compression:** Many DEM formats support compression (LZW, DEFLATE, etc.) which can significantly reduce file size.
- **Understand data types:** DEMs can be stored as integers (INT16, INT32) or floating-point (FLOAT32, FLOAT64). Choose appropriate precision for your needs.

## Data Acquisition and Sources

### Selecting Appropriate DEM Data

- **Match resolution to your analysis needs:** Higher resolution isn't always better - it increases file size and processing time. Choose resolution based on your study area and analysis requirements.
- **Consider data age and update frequency:** DEMs can become outdated due to natural processes (erosion, landslides) or human activities (mining, construction).
- **Verify data quality and accuracy:** Check metadata for vertical accuracy (RMSE, LE90) and horizontal accuracy.
- **Understand data collection methods:** DEMs can come from:
  - Satellite stereo imagery (SRTM, ASTER GDEM)
  - Airborne LiDAR
  - Photogrammetry
  - Radar interferometry
  - Ground surveys
- **Check coverage and gaps:** Verify that your study area is fully covered and check for data voids or areas of poor quality.

### Common DEM Sources

- **Global datasets:** SRTM (30m, 90m), ASTER GDEM (30m), ALOS World 3D (30m), NASADEM
- **Regional datasets:** USGS 3DEP (1m, 3m, 10m), EU-DEM, national mapping agencies
- **High-resolution commercial:** Often available from commercial providers or government agencies
- **Document data source and version** in all your work, including download date and any processing applied by the provider.

## Data Quality Assessment

### Initial Quality Checks

- **Inspect for data voids and NoData values:** Identify and document areas with missing elevation data.
- **Check for unrealistic values:** Look for extreme outliers that might indicate errors (e.g., negative values for areas above sea level, or impossibly high values).
- **Verify spatial extent:** Ensure the DEM covers your entire area of interest with adequate buffer.
- **Check coordinate system:** Verify the CRS matches your other datasets and is appropriate for your location.
- **Assess vertical accuracy:** Review metadata for stated accuracy metrics and validate against known control points if available.
- **Examine edge artifacts:** Check for discontinuities or artifacts at tile boundaries if working with mosaicked data.

### Statistical Analysis

- **Calculate basic statistics:** Mean, median, standard deviation, min, max, and percentiles.
- **Examine elevation distribution:** Create histograms to identify unusual patterns or bimodal distributions.
- **Check for systematic errors:** Look for patterns that might indicate systematic bias or processing artifacts.
- **Compare with reference data:** If available, compare your DEM with higher-accuracy reference data to assess quality.

## Data Preprocessing

### Handling NoData Values

- **Identify NoData values:** Different formats use different NoData indicators (-9999, -32768, NaN, etc.). Always check metadata.
- **Document NoData handling strategy:** Decide whether to fill voids, mask them, or exclude them from analysis.
- **Use appropriate interpolation methods** for filling voids:
  - **IDW (Inverse Distance Weighting):** Good for small gaps
  - **Kriging:** Better for larger areas with spatial correlation
  - **Spline interpolation:** Smooth results but can create artifacts
- **Avoid extrapolation beyond data boundaries:** Don't fill areas where you have no surrounding data.
- **Mask NoData areas** in final outputs rather than using interpolated values if accuracy is critical.

### Coordinate System Management

- **Always reproject to appropriate CRS:** Use a projected coordinate system (UTM, State Plane) for area and distance calculations, not geographic coordinates.
- **Choose CRS based on location:** Select a CRS that minimises distortion for your study area.
- **Maintain consistency:** Ensure all datasets use the same CRS before analysis.
- **Document all reprojections:** Record original and target CRSs, and any resampling methods used.
- **Use appropriate resampling:** Choose resampling method (nearest neighbour, bilinear, cubic) based on whether you're upsampling or downsampling.

### Mosaicking and Tiling

- **Handle edge matching:** When mosaicking tiles, ensure elevations match at boundaries or apply edge-matching algorithms.
- **Check for seam lines:** Visually inspect mosaicked DEMs for visible seams or discontinuities.
- **Consider overlap:** If tiles overlap, decide on strategy (average, first, last, or use highest quality source).
- **Document tile sources:** Keep track of which tiles come from which source or date.

## Common DEM Operations

### Slope Calculation

- **Choose appropriate algorithm:** Common methods include Horn's method, Zevenbergen-Thorne, and simple gradient.
- **Understand slope units:** Slope can be expressed as degrees (0-90°) or percent (0-100%+). Always specify which you're using.
- **Consider cell size:** Slope calculations are sensitive to DEM resolution. Higher resolution DEMs will show more detail but also more noise.
- **Handle edge effects:** Slope calculations at raster edges may be less reliable due to limited neighbourhood data.
- **Validate results:** Check that calculated slopes are reasonable for your terrain type.

### Aspect Calculation

- **Understand aspect values:** Aspect is typically measured in degrees (0-360°), where 0/360° is north, 90° is east, 180° is south, 270° is west.
- **Handle flat areas:** Flat areas (slope = 0) may have undefined or arbitrary aspect values. Decide how to handle these.
- **Consider aspect classification:** You may want to classify aspect into cardinal directions (N, NE, E, SE, S, SW, W, NW) for analysis.
- **Account for projection distortion:** Aspect calculations can be affected by coordinate system choice, especially in high-latitude areas.

### Hillshade Generation

- **Set appropriate sun angle:** Default is often 315° azimuth and 45° elevation, but adjust based on your location and visualization goals.
- **Use multiple hillshades:** Create hillshades with different sun angles and combine them for better visualization.
- **Consider vertical exaggeration:** Apply vertical exaggeration to hillshades when terrain relief is subtle.
- **Combine with other visualizations:** Overlay hillshades with other data (slope, aspect, elevation) for richer maps.

### Hydrological Analysis

- **Fill sinks before flow analysis:** DEMs often contain depressions (sinks) that need to be filled before calculating flow direction and accumulation.
- **Choose appropriate fill method:** Simple fill vs. selective fill (preserving real depressions like lakes).
- **Calculate flow direction:** Use D8 (single direction) or D-infinity (multiple directions) algorithms based on your needs.
- **Calculate flow accumulation:** Understand that this represents upstream contributing area, not actual flow volume.
- **Delineate watersheds:** Use flow accumulation and flow direction to identify watershed boundaries.
- **Extract stream networks:** Apply appropriate thresholds to flow accumulation to identify stream channels.

### Viewshed Analysis

- **Define observer points carefully:** Viewshed results are highly sensitive to observer location and height.
- **Set observer height:** Include observer height above ground (e.g., person, building, tower).
- **Set target height:** Specify height of target features if relevant.
- **Consider Earth's curvature:** For large areas, account for Earth's curvature in viewshed calculations.
- **Understand limitations:** Viewsheds assume straight-line visibility and don't account for atmospheric conditions.

### Terrain Ruggedness

- **Calculate appropriate indices:** TRI (Terrain Ruggedness Index), TPI (Topographic Position Index), or roughness measures.
- **Choose appropriate neighbourhood size:** The scale of analysis affects ruggedness calculations.
- **Interpret results in context:** Ruggedness values are relative and depend on your study area.

## Data Analysis Best Practices

### Scale Considerations

- **Match analysis scale to data resolution:** Don't perform analyses that require finer detail than your DEM resolution provides.
- **Consider multiple scales:** Some analyses benefit from multi-scale approaches (e.g., local vs. regional terrain characteristics).
- **Understand scale-dependent patterns:** Terrain features may appear or disappear at different scales.

### Statistical Analysis

- **Use appropriate statistics for elevation data:** Elevation data is continuous and spatial, so use spatial statistics when appropriate.
- **Account for spatial autocorrelation:** Elevation values are spatially correlated - nearby cells have similar values.
- **Use robust statistics:** Consider using median instead of mean for elevation statistics, as elevation distributions may be skewed.
- **Calculate elevation profiles:** Extract and analyse elevation profiles along transects for detailed terrain analysis.

### Change Detection

- **Use DEMs of difference (DoD):** Subtract one DEM from another to detect elevation changes.
- **Account for uncertainty:** DEMs have error, so small differences may not be significant. Use error propagation to determine significance thresholds.
- **Consider temporal factors:** Account for time between DEM acquisitions and natural processes that may have occurred.
- **Validate changes:** Ground-truth significant changes to verify they're real, not artifacts.

## Visualisation

### Elevation Visualisation

- **Choose appropriate colour schemes:** Use intuitive schemes (green to brown, blue to white) or scientific colour maps (viridis, plasma) that are colourblind-friendly.
- **Set meaningful break points:** Use natural breaks, quantiles, or standard deviations for classification, not arbitrary equal intervals.
- **Include legend and scale:** Always provide clear legends with units and scale bars.
- **Consider hillshading:** Combine elevation colours with hillshading for better terrain perception.
- **Use appropriate vertical exaggeration:** Apply vertical exaggeration when relief is subtle, but document it clearly.

### Map Composition

- **Include essential map elements:** Title, legend, scale bar, north arrow, coordinate system, data source, date.
- **Choose appropriate scale:** Ensure map scale is appropriate for the level of detail in your DEM.
- **Use insets for context:** Include location maps or overviews for regional context.
- **Maintain visual hierarchy:** Make important information stand out while keeping supporting elements visible but not distracting.

### 3D Visualisation

- **Use 3D when it adds value:** 3D visualisations can be powerful but also misleading. Use when terrain understanding benefits from 3D perspective.
- **Set appropriate viewing angle:** Choose angles that best show the features of interest.
- **Apply vertical exaggeration carefully:** Document any vertical exaggeration used.
- **Consider animation:** Fly-throughs or rotating views can help understand complex terrain.

## Tools and Libraries

### Python Ecosystem

- **Rasterio:** Primary library for reading/writing raster data, including GeoTIFF DEMs.
- **GDAL/OGR:** Low-level library for geospatial data operations. Rasterio and other tools build on GDAL.
- **NumPy:** Essential for array operations on DEM data.
- **SciPy:** Useful for interpolation, filtering, and advanced operations.
- **WhiteboxTools/Whitebox Python:** Comprehensive terrain analysis tools.
- **RichDEM:** High-performance DEM analysis library.
- **PySAL:** Spatial analysis library with terrain analysis capabilities.
- **Matplotlib/Plotly:** For visualisation and plotting.
- **GeoPandas:** For vector operations alongside raster data.

### GIS Software

- **QGIS:** Free, open-source GIS with extensive DEM analysis plugins (SAGA, GRASS).
- **ArcGIS/ArcGIS Pro:** Commercial GIS with comprehensive terrain analysis tools.
- **SAGA GIS:** Specialised in terrain analysis with many algorithms.
- **GRASS GIS:** Powerful open-source GIS with extensive terrain analysis modules.

### Command-Line Tools

- **GDAL command-line tools:** `gdalwarp`, `gdal_translate`, `gdalinfo`, `gdal_calc.py`
- **WhiteboxTools:** Command-line terrain analysis toolkit.
- **PDAL:** Point cloud data processing (for LiDAR-derived DEMs).

## Performance and Efficiency

### Memory Management

- **Use tiling/chunking for large datasets:** Process large DEMs in tiles to avoid memory issues.
- **Consider data types:** Use appropriate precision (INT16 vs FLOAT32) to reduce memory usage.
- **Use compression:** Compress DEM files to reduce storage and I/O time, but consider trade-off with processing speed.
- **Process in blocks:** Read and process data in blocks rather than loading entire raster into memory.

### Computational Efficiency

- **Use vectorised operations:** Leverage NumPy vectorisation instead of loops when possible.
- **Consider parallel processing:** Many DEM operations can be parallelised across tiles or cores.
- **Use appropriate algorithms:** Some algorithms have faster alternatives (e.g., D8 vs D-infinity for flow direction).
- **Profile before optimising:** Identify actual bottlenecks before optimising code.

### Data Storage

- **Use appropriate file formats:** GeoTIFF with compression for most cases, but consider alternatives for specific needs.
- **Organise data logically:** Use consistent naming conventions and directory structures.
- **Maintain metadata:** Keep metadata files (XML, JSON) with DEMs documenting source, processing, and characteristics.
- **Version control outputs:** Keep track of different versions of processed DEMs with clear naming.

## Error Handling and Validation

### Common Errors

- **Coordinate system mismatches:** Always verify CRS before combining datasets.
- **Unit confusion:** Confusing metres, feet, or degrees in elevation values or cell sizes.
- **NoData handling:** Forgetting to handle NoData values properly, leading to incorrect calculations.
- **Edge effects:** Not accounting for reduced reliability at raster edges.
- **Resolution mismatches:** Combining DEMs of different resolutions without appropriate resampling.

### Validation Strategies

- **Compare with known elevations:** Validate against surveyed control points or higher-accuracy DEMs.
- **Check for logical consistency:** Elevation values should make sense for the location (e.g., not negative for areas above sea level).
- **Visual inspection:** Always visually inspect DEMs and derived products for obvious errors.
- **Statistical validation:** Compare statistics with expected values for the terrain type.
- **Cross-validation:** Compare results from different methods or tools when possible.

## Documentation Requirements

### Metadata Documentation

- **Document data source:** Origin, provider, acquisition date, version.
- **Record processing steps:** Document all transformations, reprojections, and analyses applied.
- **Specify coordinate systems:** Original and final CRSs, including vertical datum.
- **Note data quality:** Accuracy metrics, known issues, limitations.
- **Record parameters:** Document all parameters used in analyses (e.g., slope algorithm, fill method, threshold values).

### Code Documentation

- **Comment complex operations:** Explain terrain analysis algorithms and why specific methods were chosen.
- **Document assumptions:** Note any assumptions made about the data or analysis.
- **Include units:** Always specify units for elevation, slope, area, and other measurements.
- **Version control:** Use version control for analysis scripts and document changes.

### Reporting

- **Include methodology:** Explain how DEMs were processed and analysed.
- **Show intermediate steps:** Include visualisations of key processing steps when relevant.
- **Report uncertainty:** Acknowledge DEM accuracy limitations and how they affect results.
- **Provide context:** Explain results in the context of the study area and research questions.

## Ethical and Legal Considerations

### Data Usage Rights

- **Respect licensing:** Understand and comply with DEM data licensing (public domain, open data, commercial restrictions).
- **Attribute sources:** Always credit DEM data sources in publications and products.
- **Check usage restrictions:** Some high-resolution DEMs have restrictions on redistribution or commercial use.

### Accuracy and Liability

- **Acknowledge limitations:** Be transparent about DEM accuracy and limitations in applications.
- **Consider liability:** For critical applications (engineering, safety), use appropriate quality DEMs and validate results.
- **Document assumptions:** Clearly state assumptions about data quality and suitability for specific uses.

## Common Pitfalls to Avoid

- **Don't ignore coordinate systems:** Always verify and document CRSs - this is a common source of errors.
- **Don't mix vertical datums:** Combining DEMs with different vertical datums without conversion causes errors.
- **Don't assume uniform quality:** DEM quality can vary across a dataset - check for areas of poor quality.
- **Don't over-interpret low-resolution data:** Don't extract features smaller than the DEM resolution can support.
- **Don't ignore NoData values:** NoData cells can propagate through calculations and cause errors.
- **Don't use inappropriate algorithms:** Choose terrain analysis algorithms appropriate for your data and goals.
- **Don't forget edge effects:** Results at raster edges are often less reliable.
- **Don't confuse correlation with causation:** Terrain characteristics may correlate with other factors but not necessarily cause them.
- **Don't ignore temporal changes:** DEMs represent a snapshot in time - terrain changes over time.
- **Don't skip validation:** Always validate DEM processing results against known data or visual inspection.

## Specific Use Cases

### Flood Modelling

- **Use appropriate resolution:** Higher resolution needed for detailed flood modelling.
- **Fill sinks carefully:** Decide whether to fill or preserve natural depressions.
- **Account for structures:** Consider whether DSM (with buildings) or DTM (bare earth) is more appropriate.
- **Validate against historical floods:** Compare model results with known flood extents when available.

### Landslide Analysis

- **Use high-resolution data:** Landslides often require high-resolution DEMs to detect.
- **Calculate multiple terrain indices:** Combine slope, curvature, and other indices for landslide susceptibility.
- **Consider temporal changes:** Use DEMs of difference to detect landslide activity.
- **Account for vegetation:** DTM may be more appropriate than DSM for landslide analysis.

### Solar Radiation Modelling

- **Account for slope and aspect:** Solar radiation is highly dependent on terrain orientation.
- **Consider shadows:** Use viewshed or shadow analysis to identify shaded areas.
- **Use appropriate time periods:** Model solar radiation for relevant time periods (daily, seasonal, annual).
- **Include atmospheric factors:** Consider atmospheric transmittance in addition to terrain effects.

### Erosion and Sediment Transport

- **Use appropriate temporal resolution:** Erosion processes may require multiple DEMs over time.
- **Calculate flow paths:** Use hydrological analysis to identify sediment transport pathways.
- **Consider connectivity:** Analyse how different parts of the landscape are connected hydrologically.
- **Validate with field data:** Compare model results with observed erosion patterns.

## Advanced Techniques

### DEM Fusion

- **Combine multiple DEM sources:** Merge DEMs from different sources to improve coverage or quality.
- **Weight by quality:** When combining DEMs, weight by their relative accuracy.
- **Handle overlaps:** Develop strategies for areas where multiple DEMs overlap.
- **Validate fused products:** Check that fused DEMs are better than individual sources.

### Machine Learning Applications

- **DEM as input:** Use DEM and derived products (slope, aspect) as features in ML models.
- **Terrain classification:** Use ML to classify terrain types based on DEM characteristics.
- **Quality assessment:** Use ML to identify and flag poor-quality areas in DEMs.
- **Gap filling:** Use ML techniques to intelligently fill data voids.

### Uncertainty Analysis

- **Propagate errors:** Understand how DEM errors propagate through terrain analysis.
- **Quantify uncertainty:** Use error models to quantify uncertainty in derived products.
- **Report confidence:** Include uncertainty estimates in analysis results.
- **Consider error sources:** Account for errors from data collection, processing, and analysis.

---

**Remember:** Working with DEM data requires attention to detail, understanding of spatial data principles, and careful validation. Always document your work, verify results, and acknowledge limitations. The goal is to extract meaningful terrain information while maintaining scientific rigour and transparency about data quality and processing methods.


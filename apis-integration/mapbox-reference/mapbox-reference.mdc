# Mapbox development reference guide

## Overview

Mapbox provides mapping, geocoding, routing, and location services. This guide covers implementation patterns, APIs, and proven approaches for working with Mapbox across web and mobile platforms.

## Authentication and setup

### Access tokens

Mapbox uses access tokens for authentication. Get your token from the [Mapbox account page](https://account.mapbox.com/access-tokens/).

**Token types:**
- **Public token (pk.)**: Use in client-side applications. Restrict to specific URLs in account settings.
- **Secret token (sk.)**: Use only on the server. Never expose in client-side code.

**Security:**
- Store tokens in environment variables, never commit to version control.
- Use URL restrictions for public tokens.
- Rotate tokens if exposed.

### Environment setup

```javascript
// .env file
MAPBOX_ACCESS_TOKEN=pk.your_public_token_here
MAPBOX_SECRET_TOKEN=sk.your_secret_token_here
```

## Mapbox GL JS (web)

### Installation

```bash
npm install mapbox-gl
```

Or via CDN:
```html
<script src='https://api.mapbox.com/mapbox-gl-js/v3.0.0/mapbox-gl.js'></script>
<link href='https://api.mapbox.com/mapbox-gl-js/v3.0.0/mapbox-gl.css' rel='stylesheet' />
```

### Basic map initialization

```javascript
import mapboxgl from 'mapbox-gl';

mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN;

const map = new mapboxgl.Map({
  container: 'map', // HTML element ID
  style: 'mapbox://styles/mapbox/streets-v12', // Style URL
  center: [-74.5, 40], // [longitude, latitude]
  zoom: 9
});

map.on('load', () => {
  // Map is ready for interaction
  console.log('Map loaded');
});
```

### Common map options

```javascript
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v12',
  center: [-74.5, 40],
  zoom: 9,
  pitch: 45, // 3D tilt (0-60)
  bearing: -17.6, // Rotation in degrees
  minZoom: 0,
  maxZoom: 22,
  maxBounds: [[-180, -85], [180, 85]], // Restrict panning
  antialias: true, // Smooth rendering
  preserveDrawingBuffer: true, // For screenshots
  attributionControl: true,
  logoPosition: 'bottom-right'
});
```

### Adding markers

```javascript
// Simple marker
const marker = new mapboxgl.Marker()
  .setLngLat([-74.5, 40])
  .addTo(map);

// Custom marker with HTML
const el = document.createElement('div');
el.className = 'custom-marker';
el.style.backgroundImage = 'url(marker-icon.png)';
el.style.width = '30px';
el.style.height = '30px';

const marker = new mapboxgl.Marker(el)
  .setLngLat([-74.5, 40])
  .setPopup(new mapboxgl.Popup().setHTML('<h3>Location</h3><p>Details</p>'))
  .addTo(map);

// Marker with popup
marker.togglePopup();
```

### Adding popups

```javascript
// Standalone popup
const popup = new mapboxgl.Popup({ closeOnClick: false })
  .setLngLat([-74.5, 40])
  .setHTML('<h3>Title</h3><p>Content</p>')
  .addTo(map);

// Popup on click
map.on('click', (e) => {
  new mapboxgl.Popup()
    .setLngLat(e.lngLat)
    .setHTML(`<p>Clicked at: ${e.lngLat.lng}, ${e.lngLat.lat}</p>`)
    .addTo(map);
});
```

### Drawing shapes and lines

```javascript
// Add GeoJSON source
map.addSource('route', {
  type: 'geojson',
  data: {
    type: 'Feature',
    geometry: {
      type: 'LineString',
      coordinates: [[-74.5, 40], [-74.6, 40.1]]
    }
  }
});

// Add layer
map.addLayer({
  id: 'route',
  type: 'line',
  source: 'route',
  layout: {
    'line-join': 'round',
    'line-cap': 'round'
  },
  paint: {
    'line-color': '#3887be',
    'line-width': 5,
    'line-opacity': 0.75
  }
});

// Add polygon
map.addSource('area', {
  type: 'geojson',
  data: {
    type: 'Feature',
    geometry: {
      type: 'Polygon',
      coordinates: [[
        [-74.5, 40],
        [-74.6, 40],
        [-74.6, 40.1],
        [-74.5, 40.1],
        [-74.5, 40]
      ]]
    }
  }
});

map.addLayer({
  id: 'area',
  type: 'fill',
  source: 'area',
  paint: {
    'fill-color': '#088',
    'fill-opacity': 0.3
  }
});

map.addLayer({
  id: 'area-outline',
  type: 'line',
  source: 'area',
  paint: {
    'line-color': '#088',
    'line-width': 2
  }
});
```

### Clustering markers

```javascript
map.addSource('points', {
  type: 'geojson',
  data: {
    type: 'FeatureCollection',
    features: [
      // Array of point features
    ]
  },
  cluster: true,
  clusterMaxZoom: 14,
  clusterRadius: 50
});

map.addLayer({
  id: 'clusters',
  type: 'circle',
  source: 'points',
  filter: ['has', 'point_count'],
  paint: {
    'circle-color': [
      'step',
      ['get', 'point_count'],
      '#51bbd6',
      100,
      '#f1f075',
      750,
      '#f28cb1'
    ],
    'circle-radius': [
      'step',
      ['get', 'point_count'],
      20,
      100,
      30,
      750,
      40
    ]
  }
});

map.addLayer({
  id: 'cluster-count',
  type: 'symbol',
  source: 'points',
  filter: ['has', 'point_count'],
  layout: {
    'text-field': '{point_count_abbreviated}',
    'text-font': ['DIN Offc Pro Medium', 'Arial Unicode MS Bold'],
    'text-size': 12
  }
});

map.addLayer({
  id: 'unclustered-point',
  type: 'circle',
  source: 'points',
  filter: ['!', ['has', 'point_count']],
  paint: {
    'circle-color': '#11b4da',
    'circle-radius': 4,
    'circle-stroke-width': 1,
    'circle-stroke-color': '#fff'
  }
});

// Click handler for clusters
map.on('click', 'clusters', (e) => {
  const features = map.queryRenderedFeatures(e.point, {
    layers: ['clusters']
  });
  const clusterId = features[0].properties.cluster_id;
  map.getSource('points').getClusterExpansionZoom(
    clusterId,
    (err, zoom) => {
      if (err) return;
      map.easeTo({
        center: features[0].geometry.coordinates,
        zoom: zoom
      });
    }
  );
});
```

### 3D buildings and terrain

```javascript
// Add 3D terrain
map.addSource('mapbox-dem', {
  type: 'raster-dem',
  url: 'mapbox://mapbox.mapbox-terrain-dem-v1',
  tileSize: 256,
  maxzoom: 14
});

map.setTerrain({ source: 'mapbox-dem', exaggeration: 1.5 });

// Add 3D buildings
map.addLayer({
  id: '3d-buildings',
  source: 'composite',
  'source-layer': 'building',
  filter: ['==', 'extrude', 'true'],
  type: 'fill-extrusion',
  minzoom: 14,
  paint: {
    'fill-extrusion-color': '#aaa',
    'fill-extrusion-height': [
      'interpolate',
      ['linear'],
      ['zoom'],
      15,
      0,
      15.05,
      ['get', 'height']
    ],
    'fill-extrusion-base': [
      'interpolate',
      ['linear'],
      ['zoom'],
      15,
      0,
      15.05,
      ['get', 'min_height']
    ],
    'fill-extrusion-opacity': 0.6
  }
});
```

### Heatmaps

```javascript
map.addSource('heatmap-data', {
  type: 'geojson',
  data: {
    type: 'FeatureCollection',
    features: [
      // Array of point features with intensity property
    ]
  }
});

map.addLayer({
  id: 'heatmap',
  type: 'heatmap',
  source: 'heatmap-data',
  maxzoom: 9,
  paint: {
    'heatmap-weight': [
      'interpolate',
      ['linear'],
      ['get', 'intensity'],
      0, 0,
      6, 1
    ],
    'heatmap-intensity': [
      'interpolate',
      ['linear'],
      ['zoom'],
      0, 1,
      9, 3
    ],
    'heatmap-color': [
      'interpolate',
      ['linear'],
      ['heatmap-density'],
      0, 'rgba(33,102,172,0)',
      0.2, 'rgb(103,169,207)',
      0.4, 'rgb(209,229,240)',
      0.6, 'rgb(253,219,199)',
      0.8, 'rgb(239,138,98)',
      1, 'rgb(178,24,43)'
    ],
    'heatmap-radius': [
      'interpolate',
      ['linear'],
      ['zoom'],
      0, 2,
      9, 20
    ],
    'heatmap-opacity': [
      'interpolate',
      ['linear'],
      ['zoom'],
      7, 1,
      9, 0
    ]
  }
});
```

### Event handling

```javascript
// Map events
map.on('load', () => { /* map loaded */ });
map.on('click', (e) => { /* clicked at e.lngLat */ });
map.on('mousemove', (e) => { /* mouse moved */ });
map.on('moveend', () => { /* pan/zoom ended */ });
map.on('zoomend', () => { /* zoom ended */ });

// Layer events
map.on('click', 'layer-id', (e) => {
  const features = map.queryRenderedFeatures(e.point, {
    layers: ['layer-id']
  });
  // Handle feature click
});

// Remove event listener
map.off('click', handler);
```

### Camera controls

```javascript
// Fly to location
map.flyTo({
  center: [-74.5, 40],
  zoom: 15,
  duration: 2000,
  essential: true // Animation can be interrupted
});

// Ease to location
map.easeTo({
  center: [-74.5, 40],
  zoom: 15,
  duration: 1000
});

// Jump to location
map.jumpTo({
  center: [-74.5, 40],
  zoom: 15
});

// Fit bounds
map.fitBounds([
  [-74.5, 40], // Southwest
  [-74.4, 40.1] // Northeast
], {
  padding: 50,
  duration: 1000
});
```

### Custom styles

```javascript
// Use custom style
const map = new mapboxgl.Map({
  container: 'map',
  style: {
    version: 8,
    sources: {
      'mapbox-streets': {
        type: 'vector',
        url: 'mapbox://mapbox.mapbox-streets-v8'
      }
    },
    layers: [
      // Define layers
    ]
  }
});

// Or use style URL from Mapbox Studio
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/your-username/your-style-id'
});
```

## Mapbox Geocoding API

### Forward geocoding (address to coordinates)

```javascript
async function geocodeAddress(query) {
  const response = await fetch(
    `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(query)}.json?` +
    `access_token=${mapboxgl.accessToken}&` +
    `limit=5&` +
    `proximity=-74.5,40`
  );
  const data = await response.json();
  return data.features;
}

// Usage
const results = await geocodeAddress('1600 Pennsylvania Ave NW, Washington, DC');
results.forEach(feature => {
  console.log(feature.place_name, feature.center);
});
```

### Reverse geocoding (coordinates to address)

```javascript
async function reverseGeocode(lng, lat) {
  const response = await fetch(
    `https://api.mapbox.com/geocoding/v5/mapbox.places/${lng},${lat}.json?` +
    `access_token=${mapboxgl.accessToken}`
  );
  const data = await response.json();
  return data.features[0];
}

// Usage
const result = await reverseGeocode(-77.0369, 38.9072);
console.log(result.place_name);
```

### Geocoding with autocomplete

```javascript
// Using Mapbox Geocoder control
import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder';
import '@mapbox/mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css';

const geocoder = new MapboxGeocoder({
  accessToken: mapboxgl.accessToken,
  mapboxgl: mapboxgl,
  marker: true,
  placeholder: 'Search for places',
  proximity: {
    longitude: -74.5,
    latitude: 40
  },
  countries: 'us,ca', // Restrict to countries
  types: 'address,poi' // Restrict to types
});

map.addControl(geocoder);

geocoder.on('result', (e) => {
  console.log('Selected:', e.result);
});
```

## Mapbox Directions API

### Get directions

```javascript
async function getDirections(start, end, profile = 'driving') {
  const coordinates = `${start[0]},${start[1]};${end[0]},${end[1]}`;
  const response = await fetch(
    `https://api.mapbox.com/directions/v5/mapbox/${profile}/${coordinates}?` +
    `access_token=${mapboxgl.accessToken}&` +
    `geometries=geojson&` +
    `overview=full&` +
    `steps=true`
  );
  const data = await response.json();
  return data;
}

// Usage
const route = await getDirections(
  [-74.5, 40],
  [-74.6, 40.1],
  'driving' // or 'walking', 'cycling', 'driving-traffic'
);

// Add route to map
map.addSource('route', {
  type: 'geojson',
  data: {
    type: 'Feature',
    geometry: route.routes[0].geometry
  }
});

map.addLayer({
  id: 'route',
  type: 'line',
  source: 'route',
  paint: {
    'line-color': '#3887be',
    'line-width': 5
  }
});
```

### Directions with waypoints

```javascript
async function getDirectionsWithWaypoints(waypoints, profile = 'driving') {
  const coordinates = waypoints.map(wp => `${wp[0]},${wp[1]}`).join(';');
  const response = await fetch(
    `https://api.mapbox.com/directions/v5/mapbox/${profile}/${coordinates}?` +
    `access_token=${mapboxgl.accessToken}&` +
    `geometries=geojson&` +
    `overview=full&` +
    `steps=true`
  );
  return await response.json();
}
```

### Using Mapbox Directions control

```javascript
import MapboxDirections from '@mapbox/mapbox-gl-directions';
import '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions.css';

const directions = new MapboxDirections({
  accessToken: mapboxgl.accessToken,
  unit: 'metric',
  profile: 'mapbox/driving',
  alternatives: true,
  geometries: 'geojson',
  controls: {
    inputs: true,
    instructions: true,
    profileSwitcher: true
  }
});

map.addControl(directions, 'top-left');

directions.on('route', (e) => {
  console.log('Route calculated:', e.route);
});
```

## Mapbox mobile SDKs

### React Native (react-native-mapbox-gl)

```bash
npm install @rnmapbox/maps
```

```javascript
import Mapbox from '@rnmapbox/maps';

Mapbox.setAccessToken(process.env.MAPBOX_ACCESS_TOKEN);

function MapScreen() {
  return (
    <Mapbox.MapView
      style={{ flex: 1 }}
      styleURL={Mapbox.StyleURL.Street}
    >
      <Mapbox.Camera
        zoomLevel={10}
        centerCoordinate={[-74.5, 40]}
      />
      <Mapbox.PointAnnotation
        id="marker"
        coordinate={[-74.5, 40]}
      >
        <View style={{ backgroundColor: 'red', width: 20, height: 20 }} />
      </Mapbox.PointAnnotation>
    </Mapbox.MapView>
  );
}
```

### iOS (Swift)

```swift
import MapboxMaps

let mapView = MapView(frame: view.bounds)
mapView.mapboxMap.onNext(.mapLoaded) { _ in
    // Map loaded
}

// Add marker
let point = Point(CLLocationCoordinate2D(latitude: 40, longitude: -74.5))
try! mapView.mapboxMap.addLayer(
    self.createMarkerLayer(id: "marker", sourceId: "marker-source")
)
```

### Android (Kotlin)

```kotlin
import com.mapbox.maps.MapView
import com.mapbox.maps.MapboxMap

val mapView = findViewById<MapView>(R.id.mapView)
val mapboxMap = mapView.getMapboxMap()

mapboxMap.loadStyleUri(Style.MAPBOX_STREETS)

// Add marker
val point = Point.fromLngLat(-74.5, 40.0)
val source = GeoJsonSource("marker-source")
    .geometry(point)
mapboxMap.getStyle()?.addSource(source)
```

## Data visualization patterns

### Choropleth maps

```javascript
// Load GeoJSON data
map.addSource('states', {
  type: 'geojson',
  data: 'https://example.com/states.geojson'
});

map.addLayer({
  id: 'states-fill',
  type: 'fill',
  source: 'states',
  paint: {
    'fill-color': [
      'interpolate',
      ['linear'],
      ['get', 'population'],
      0, '#f7f7f7',
      100000, '#d9d9d9',
      500000, '#969696',
      1000000, '#525252',
      5000000, '#000000'
    ],
    'fill-opacity': 0.7
  }
});

map.addLayer({
  id: 'states-outline',
  type: 'line',
  source: 'states',
  paint: {
    'line-color': '#fff',
    'line-width': 1
  }
});
```

### Symbol layers with data-driven styling

```javascript
map.addSource('points', {
  type: 'geojson',
  data: {
    type: 'FeatureCollection',
    features: [
      {
        type: 'Feature',
        properties: { category: 'restaurant', rating: 4.5 },
        geometry: { type: 'Point', coordinates: [-74.5, 40] }
      }
    ]
  }
});

map.addLayer({
  id: 'points',
  type: 'circle',
  source: 'points',
  paint: {
    'circle-radius': [
      'interpolate',
      ['linear'],
      ['get', 'rating'],
      1, 5,
      5, 20
    ],
    'circle-color': [
      'match',
      ['get', 'category'],
      'restaurant', '#ff0000',
      'hotel', '#0000ff',
      '#888888'
    ]
  }
});
```

## Performance optimization

### Vector tiles

Use vector tiles instead of GeoJSON for large datasets:

```javascript
map.addSource('buildings', {
  type: 'vector',
  url: 'mapbox://mapbox.buildings'
});

map.addLayer({
  id: 'buildings',
  source: 'buildings',
  'source-layer': 'building',
  type: 'fill',
  paint: {
    'fill-color': '#aaa'
  }
});
```

### Lazy loading and viewport queries

```javascript
// Only load data in current viewport
map.on('moveend', () => {
  const bounds = map.getBounds();
  loadDataInBounds(bounds);
});

async function loadDataInBounds(bounds) {
  const response = await fetch(
    `/api/data?` +
    `sw=${bounds.getSouthWest().lng},${bounds.getSouthWest().lat}&` +
    `ne=${bounds.getNorthEast().lng},${bounds.getNorthEast().lat}`
  );
  const data = await response.json();
  map.getSource('points').setData(data);
}
```

### Debouncing map events

```javascript
import { debounce } from 'lodash';

const debouncedHandler = debounce((e) => {
  // Handle event
}, 300);

map.on('move', debouncedHandler);
```

### Reducing layer complexity

- Use `minzoom` and `maxzoom` to show layers only at appropriate zoom levels
- Simplify geometries for lower zoom levels
- Use data-driven styling instead of multiple layers when possible

## Common patterns and solutions

### Drawing tools

```javascript
import MapboxDraw from '@mapbox/mapbox-gl-draw';
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';

const draw = new MapboxDraw({
  displayControlsDefault: false,
  controls: {
    point: true,
    line_string: true,
    polygon: true,
    trash: true
  }
});

map.addControl(draw);

map.on('draw.create', (e) => {
  const feature = e.features[0];
  console.log('Created:', feature);
});

map.on('draw.update', (e) => {
  console.log('Updated:', e.features);
});
```

### Measuring distance

```javascript
function calculateDistance(coord1, coord2) {
  const R = 6371e3; // Earth radius in metres
  const φ1 = coord1[1] * Math.PI / 180;
  const φ2 = coord2[1] * Math.PI / 180;
  const Δφ = (coord2[1] - coord1[1]) * Math.PI / 180;
  const Δλ = (coord2[0] - coord1[0]) * Math.PI / 180;

  const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
            Math.cos(φ1) * Math.cos(φ2) *
            Math.sin(Δλ/2) * Math.sin(Δλ/2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

  return R * c; // Distance in metres
}
```

### Snapping to roads

```javascript
async function snapToRoads(coordinates) {
  const coords = coordinates.map(c => `${c[0]},${c[1]}`).join(';');
  const response = await fetch(
    `https://api.mapbox.com/matching/v5/mapbox/driving/${coords}?` +
    `access_token=${mapboxgl.accessToken}&` +
    `geometries=geojson`
  );
  const data = await response.json();
  return data.matchings[0].geometry;
}
```

### Isolines (isochrones)

```javascript
async function getIsochrone(center, profile = 'driving', minutes = 15) {
  const response = await fetch(
    `https://api.mapbox.com/isochrone/v1/mapbox/${profile}/${center[0]},${center[1]}?` +
    `access_token=${mapboxgl.accessToken}&` +
    `contours_minutes=${minutes}&` +
    `polygons=true&` +
    `denoise=1&` +
    `generalize=200`
  );
  const data = await response.json();
  return data;
}
```

### Traffic data

```javascript
// Add traffic layer
map.addLayer({
  id: 'traffic',
  type: 'line',
  source: {
    type: 'vector',
    url: 'mapbox://mapbox.mapbox-traffic-v1'
  },
  'source-layer': 'traffic',
  paint: {
    'line-width': 2,
    'line-color': [
      'interpolate',
      ['linear'],
      ['get', 'congestion'],
      'low', '#00ff00',
      'moderate', '#ffff00',
      'heavy', '#ff0000',
      'severe', '#800000'
    ]
  }
});
```

## Error handling

```javascript
map.on('error', (e) => {
  console.error('Map error:', e.error);
  // Handle error
});

// API error handling
async function safeGeocode(query) {
  try {
    const response = await fetch(/* ... */);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Geocoding error:', error);
    return null;
  }
}
```

## Best practices

### Security

- Never expose secret tokens in client-side code
- Use URL restrictions for public tokens
- Implement rate limiting on the server for API calls
- Validate and sanitize user inputs before geocoding

### Performance

- Use vector tiles for large datasets
- Implement clustering for dense marker sets
- Lazy load data based on viewport
- Debounce map events
- Use `minzoom` and `maxzoom` to control layer visibility
- Simplify geometries for lower zoom levels

### User experience

- Show loading states during API calls
- Provide clear error messages
- Use appropriate map styles for the use case
- Implement smooth camera transitions
- Add controls for common actions (zoom, geocoder, etc.)

### Code organisation

- Separate map logic from business logic
- Create reusable map components
- Use TypeScript for type safety
- Implement proper error boundaries
- Cache API responses when appropriate

## Common issues and solutions

### CORS errors

If using Mapbox APIs from a browser, ensure your token has the correct URL restrictions configured in your Mapbox account.

### Token not working

- Verify token is correctly set: `mapboxgl.accessToken = 'your-token'`
- Check token hasn't expired
- Ensure token has required scopes for the API you're using

### Map not displaying

- Check container element exists and has dimensions
- Verify style URL is correct
- Check browser console for errors
- Ensure Mapbox GL CSS is loaded

### Performance issues with many markers

- Use clustering for point data
- Switch to vector tiles for large datasets
- Implement viewport-based loading
- Reduce marker complexity

## Resources

- [Mapbox GL JS Documentation](https://docs.mapbox.com/mapbox-gl-js/)
- [Mapbox API Documentation](https://docs.mapbox.com/api/)
- [Mapbox Style Specification](https://docs.mapbox.com/mapbox-gl-js/style-spec/)
- [Mapbox Examples](https://docs.mapbox.com/mapbox-gl-js/example/)
- [Mapbox Studio](https://studio.mapbox.com/)

## Version information

This guide covers Mapbox GL JS v3.x. Check the [changelog](https://github.com/mapbox/mapbox-gl-js/blob/main/CHANGELOG.md) for updates.


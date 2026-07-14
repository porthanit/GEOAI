"""Render Thailand.geojson as an interactive HTML map with a Google Maps basemap."""

import geopandas as gpd
import folium

gdf = gpd.read_file("Thailand.geojson")
# simplify for smooth interactive rendering (country-level overview map)
gdf["geometry"] = gdf["geometry"].simplify(tolerance=0.001, preserve_topology=True)

center = [13.7, 100.5]  # Thailand approx center
m = folium.Map(location=center, zoom_start=6, tiles=None)

folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
    attr="Google Maps",
    name="Google Maps (Roadmap)",
    overlay=False,
    control=True,
).add_to(m)

folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attr="Google Satellite",
    name="Google Satellite",
    overlay=False,
    control=True,
).add_to(m)

folium.GeoJson(
    gdf,
    name="Thailand Boundary",
    style_function=lambda feature: {
        "fillColor": "#1a5276",
        "color": "#1a5276",
        "weight": 2,
        "fillOpacity": 0.15,
    },
).add_to(m)

folium.LayerControl().add_to(m)

m.save("Thailand.html")
print("saved Thailand.html")

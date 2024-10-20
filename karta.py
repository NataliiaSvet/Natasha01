import geopandas as gpd
import pandas as pd
import folium

# Load shapefile of Czech Republic administrative regions
gdf = gpd.read_file('path_to_czech_shapefile.shp')

# Load refugee data (example: number of refugees per region)
# Ensure that the dataset contains columns for regions and refugee counts
df = pd.read_csv('refugee_data.csv')

# Merge the shapefile with the refugee data based on region
gdf = gdf.merge(df, on='region_column_name')

# Initialize a Folium map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7)

# Add a choropleth layer to visualize refugee distribution
folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=['region_column_name', 'refugee_count'],
    key_on='feature.properties.region_column_name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of Ukrainian Refugees'
).add_to(m)

# Display map
m.save('czech_refugee_map.html')

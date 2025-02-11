# import streamlit as st
# import streamlit.components.v1 as components
# import ee
# import geemap.foliumap as geemap
# import pandas as pd
# import numpy as np
# from streamlit_folium import st_folium
# from folium.plugins import Draw

# # Set Streamlit Page Config
# st.set_page_config(layout="wide")

# # Authenticate and Initialize Earth Engine
# try:
#     ee.Initialize(project='ee-kimanipaul21')
# except Exception as e:
#     ee.Authenticate()
#     ee.Initialize()

# # Load CSS file
# with open("static/styles.css", "r", encoding="utf-8") as css_file:
#     st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# # Fixed Header
# st.markdown(
#     """
#     <div class="header">
#         <h1>🌍 Real-Time Drought Monitoring Dashboard</h1>
#         <h3>Analyze Vegetation Indices and Time-Series Data</h3>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Main Content Wrapper (Left + Right Panels)
# st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
# # Create Dashboard Layout (Left Panel & Right Panel)
# left_panel, right_panel = st.columns([1, 2])

# # Fetch Vegetation Indices (NDVI, SAVI, EVI)
# def get_indices(aoi):
#     landsat = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA') \
#         .filterBounds(aoi) \
#         .filterDate('2020-01-01', '2022-12-31') \
#         .median()
    
#     ndvi = landsat.normalizedDifference(['B5', 'B4']).rename('NDVI')
#     L = 0.5
#     savi = landsat.expression(
#         '((NIR - RED) / (NIR + RED + L)) * (1 + L)',
#         {'NIR': landsat.select('B5'), 'RED': landsat.select('B4'), 'L': L}
#     ).rename('SAVI')

#     modis = ee.ImageCollection('MODIS/006/MOD13Q1') \
#         .filterBounds(aoi) \
#         .filterDate('2020-01-01', '2022-12-31') \
#         .median()
    
#     evi = modis.select('EVI').rename('EVI')
    
#     return ndvi, savi, evi
# # # Define Horizontal Layout using Columns inside the dashboard container
# # left_panel, right_panel = st.columns([1, 2])  # Left panel (1/3), right panel (2/3)

# # # Left Panel (Controls & Legend)
# # with left_panel:
# #     # with open("templates/left_panel.html", "r", encoding="utf-8") as html_file:
# #     #     components.html(html_file.read(), height=400, scrolling=True)
# # # Load CSS file
# #   with open("static/styles.css", "r", encoding="utf-8") as css_file:
# #     st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
# #     # Index Selection in Streamlit
# #     selected_index = st.radio(
# #         "Select Vegetation Index:",
# #         ("NDVI", "SAVI", "EVI"),
# #         horizontal=True
# #     )


# # Left Panel (Streamlit UI Components)
# # with st.container():
# with left_panel:
#     st.markdown('<div class="left-panel">', unsafe_allow_html=True)
#     st.markdown("## 🛠 Controls & Legend")
#     # Index Selection (Radio Buttons)s
#     selected_index = st.radio(
#         "Select Vegetation Index:", 
#         ["NDVI", "SAVI", "EVI"],
#         horizontal=True
#     )

#     # Legend
#     st.markdown("### 🖌 Legend")
#     st.markdown("- **NDVI**: 🟩 Green (Healthy Vegetation)")
#     st.markdown("- **SAVI**: 🟤 Brown (Sparse Vegetation)")
#     st.markdown("- **EVI**: 🔵🔴 Blue-Red (Enhanced Vegetation Index)")

#     # Time-Series Chart
#     selected_location = st.session_state.get("selected_location", None)

#     if selected_location:
#         st.subheader("📊 Time-Series Analysis")

#         # Generate Fake Data for Testing (Replace with real GEE data extraction)
#         dates = pd.date_range(start='2020-01-01', periods=36, freq='ME')
#         values = np.random.uniform(0.2, 0.8, len(dates)) if selected_index == "NDVI" else (
#             np.random.uniform(0.1, 0.6, len(dates)) if selected_index == "SAVI" else np.random.uniform(1000, 6000, len(dates))
#         )

#         time_series_df = pd.DataFrame({"Date": dates, selected_index: values})
#         st.line_chart(time_series_df.set_index("Date"))

#     else:
#         st.warning("Click on the map to generate a time-series chart.")
#         st.markdown('</div>', unsafe_allow_html=True)



# # # Right Panel (Map & Data)
# # with right_panel:
# #     st.markdown("### 🌍 Vegetation Indices Map")
# # Right Panel (Map & Data)
# # with st.container():
# with right_panel:
#     st.markdown('<div class="right-panel">', unsafe_allow_html=True)
#     st.markdown("### 🌍 Vegetation Indices Map")

#     def create_map():
#         m = geemap.Map()
#         m.centerObject(ee.Geometry.Rectangle([50, 25, 55, 30]), 6)
#         Draw(export=True).add_to(m)

#         if 'aoi' in st.session_state:
#             aoi = st.session_state['aoi']
#             ndvi, savi, evi = get_indices(aoi)
#             index_options = {"NDVI": ndvi, "SAVI": savi, "EVI": evi}

#             # Load Selected Index on Map
#             m.addLayer(index_options[selected_index], {
#                 'min': 0, 
#                 'max': 1 if selected_index != "EVI" else 8000, 
#                 'palette': ['white', 'green'] if selected_index == "NDVI" else (
#                     ['yellow', 'brown'] if selected_index == "SAVI" else ['blue', 'green', 'red']
#                 )
#             }, selected_index)

#         return m

#     m = create_map()
#     map_data = st_folium(m, height=700, width=900)

    

#     # Capture user selections
#     if map_data.get("last_drawn"):
#         drawn_geom = map_data["last_drawn"]["geometry"]
#         aoi = ee.Geometry.Polygon(drawn_geom["coordinates"])
#         st.session_state['aoi'] = aoi

#     if map_data.get("last_clicked"):
#         st.session_state["selected_location"] = map_data["last_clicked"]
#         # Create map
# m = geemap.Map(location=[20, 0], zoom_start=3)


# st.markdown('</div>', unsafe_allow_html=True)

# # Close Main Content Wrapper
# st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import ee
import folium
import json
import pandas as pd
import plotly.express as px
import geopandas as gpd
from io import BytesIO
from shapely.geometry import shape
import plotly.express as px
from streamlit_folium import st_folium
from datetime import datetime
import os
import ee
import io
import tempfile
import shutil
import zipfile
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Set Streamlit Page Config
st.set_page_config(layout="wide")

# Authenticate and Initialize Earth Engine
try:
    ee.Initialize(project='ee-kimanipaul21')
except Exception:
    ee.Authenticate()
    ee.Initialize()

# Predefined AOI (Default)
def get_predefined_aoi():
    return ee.Geometry.Rectangle([35.0, -5.0, 42.0, 5.0])

# Function to Get AOI Bounds and Center
def get_aoi_bounds(aoi):
    bounds = aoi.bounds().coordinates().getInfo()[0]
    lats = [point[1] for point in bounds]
    lngs = [point[0] for point in bounds]
    center = [(max(lats) + min(lats)) / 2, (max(lngs) + min(lngs)) / 2]
    return center, [[min(lats), min(lngs)], [max(lats), max(lngs)]]

# Fetch MODIS Indices (NDVI, SAVI, EVI) with aggregation and clipping
@st.cache_data
def get_indices(_aoi, start_date, end_date, aggregation='median'):
    modis = ee.ImageCollection('MODIS/006/MOD13Q1')\
        .filterBounds(_aoi)\
        .filterDate(start_date, end_date)
    
    if aggregation == 'median':
        modis = modis.median()
    elif aggregation == 'mean':
        modis = modis.mean()
    elif aggregation == 'max':
        modis = modis.max()
    elif aggregation == 'min':
        modis = modis.min()
    
    modis = modis.clip(_aoi)
    
    ndvi = modis.select('NDVI').multiply(0.0001).rename('NDVI')
    evi = modis.select('EVI').multiply(0.0001).rename('EVI')
    
    L = 0.5
    savi = ndvi.expression(
        '((NDVI + L) / (1 + L))',
        {'NDVI': ndvi, 'L': L}
    ).rename('SAVI')
    # Fetch NDWI from MODIS MOD09GA dataset
    ndwi = ee.ImageCollection('MODIS/MOD09GA_006_NDWI')\
        .filterBounds(_aoi)\
        .filterDate(start_date, end_date)\
        .mean()\
        .clip(_aoi)\
        .rename('NDWI')
    
    return {"NDVI": ndvi, "SAVI": savi, "EVI": evi, "NDWI": ndwi}

# Function to Fetch Forest Loss from Hansen Global Forest Change (GFC)
def get_forest_loss(_aoi):
    gfc = ee.Image('UMD/hansen/global_forest_change_2021_v1_9')
    
    # Select forest loss year and create a binary mask (1 for loss, 0 for no loss)
    forest_loss = gfc.select('lossyear').gt(0).clip(_aoi).rename('Forest_Loss')
    
    return forest_loss

# Function to Fetch Carbon Flux Data
def get_carbon_flux(_aoi, start_date, end_date):
    carbon = ee.ImageCollection('MODIS/006/MOD17A2H')\
        .filterBounds(_aoi)\
        .filterDate(start_date, end_date)\
        .select('Gpp')
    carbon_flux = carbon.mean().clip(_aoi).rename('Carbon_Flux')
    return carbon_flux


# Function to Generate Time-Series Data
def get_time_series(_aoi, start_date, end_date, index):
    collection = ee.ImageCollection('MODIS/006/MOD13Q1')\
        .filterBounds(_aoi)\
        .filterDate(start_date, end_date)\
        .select(['NDVI', 'EVI'])
        # Compute SAVI if requested
    if index == "SAVI":
        L = 0.5
        collection = collection.map(lambda img: img.expression(
            '((NDVI + L) / (1 + L))',
            {'NDVI': img.select('NDVI').multiply(0.0001), 'L': L}
        ).rename('SAVI').copyProperties(img, ['system:time_start']))

    elif index == "NDWI":
        collection = ee.ImageCollection('MODIS/MOD09GA_006_NDWI')\
            .filterBounds(_aoi)\
            .filterDate(start_date, end_date)\
            .select('NDWI')


    elif index == "Forest_Loss":
        gfc = ee.Image('UMD/hansen/global_forest_change_2021_v1_9')
        collection = ee.ImageCollection.fromImages([
            gfc.select('lossyear').eq(year - 2000).set('system:time_start', ee.Date.fromYMD(year, 1, 1).millis())
            for year in range(2001, 2022)
        ])

    elif index == "Carbon_Flux":
        collection = ee.ImageCollection('MODIS/006/MOD17A2H')\
        .filterBounds(_aoi)\
        .filterDate(start_date, end_date)\
        .select('Gpp')\
        .map(lambda img: img.rename('Carbon_Flux'))

    else:
        return None  # Invalid index

    def reducer(image):
        mean_value = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=_aoi,
            scale=500,
            bestEffort=True
        )
        return ee.Feature(None, {
            'date': image.date().format(),
            index: mean_value.get(index)
        })
    
    series = collection.map(reducer).getInfo()
    dates = [feature['properties']['date'] for feature in series['features']]
    values = [feature['properties'][index] for feature in series['features']]
    df = pd.DataFrame({'Date': pd.to_datetime(dates), index: values})
     # Normalize values using Min-Max Scaling for better visualization
    df[index] = (df[index] - df[index].min()) / (df[index].max() - df[index].min())
    return df
    
def download_shapefile(image, aoi, index, output_path):
    try:
        # Ensure the image has a single band
        image = image.select([index])  

        # Apply thresholding to create a binary mask
        threshold = 0.2  
        binary_image = image.gt(threshold)

        # Reduce polygons to avoid excessive data
        vector = binary_image.reduceToVectors(
            geometryType='polygon',
            reducer=ee.Reducer.countEvery(),
            scale=2000,  # Increase scale to reduce polygon count
            geometry=aoi,
            bestEffort=True
        )

        # Convert to GeoJSON
        vector_data = vector.getInfo()

        # Convert to GeoDataFrame & keep only the index field
        gdf = gpd.GeoDataFrame.from_features(vector_data['features'])
        if index in gdf.columns:
            gdf = gdf[[index, 'geometry']]  # Keep only the selected index and geometry
        else:
            gdf = gdf[['geometry']]  # Fallback to only geometry if index is missing

        # Save to Shapefile
        gdf.to_file(output_path, driver="ESRI Shapefile")

        return output_path

    except Exception as e:
        st.error(f"Shapefile generation error: {e}")
        return None
# Function to generate the color ramp and legend with low and high values
def generate_color_ramp_legend(index, min_val, max_val, color_palette):
    # Create a gradient from min_val to max_val
    gradient = np.linspace(min_val, max_val, 256)
    
    # Generate a color ramp based on the selected palette
    fig, ax = plt.subplots(figsize=(5, 1), dpi=80)
    ax.imshow([gradient], aspect='auto', cmap=plt.cm.colors.ListedColormap(color_palette), extent=[0, 10, 0, 1])
    
    # Set labels for the min and max values at the ends of the color ramp
    ax.text(0, 1.1, f'{min_val:.2f}', ha='left', va='bottom', fontsize=10, color='black')
    ax.text(10, 1.1, f'{max_val:.2f}', ha='right', va='bottom', fontsize=10, color='black')
    
    # Remove the axes to only show the color ramp
    ax.set_axis_off()
    
    # Save the figure to an in-memory image
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
    buf.seek(0)  # Keep the pointer at the beginning for further usage
    
    # Convert the image to an appropriate format for display
    pil_img = Image.open(buf)  # Open the image
    # Do not close the buffer here, as the image is still being used
    return pil_img, buf

# Initialize session state for layers
if "layers" not in st.session_state:
    st.session_state.layers = {}
if "aoi_center" not in st.session_state:
    st.session_state.aoi_center = [0.0, 38.5]

# Left Panel (Controls)
left_panel, right_panel = st.columns([1, 2])

with left_panel:
    st.markdown("## 🛠 Controls & Legend")
    selected_index = st.radio("Select Vegetation Index:", ["NDVI", "SAVI", "EVI","NDWI","Forest_Loss","Carbon_Flux"], horizontal=True)
    start_date = st.date_input("Start Date", datetime(2020, 1, 1))
    end_date = st.date_input("End Date", datetime(2022, 12, 31))
    uploaded_aoi = st.file_uploader("Upload AOI (GeoJSON)", type="geojson")
    aggregation = st.selectbox("Select Aggregation Method", ["median", "mean", "max", "min"])

    if st.button("Load Data", key="load_data_btn"):
        with st.spinner("Fetching Data..."):
            aoi = get_predefined_aoi()
            if uploaded_aoi:
                geojson = json.load(uploaded_aoi)
                if 'features' in geojson and len(geojson['features']) > 0:
                    aoi = ee.Geometry(geojson['features'][0]['geometry'])
                else:
                    st.error("Invalid GeoJSON format.")
                    st.stop()
            
            center, bounds = get_aoi_bounds(aoi)
            st.session_state.aoi_center = center
            st.session_state.aoi_bounds = bounds

            # indices = get_indices(aoi, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), aggregation)
            # selected_image = indices[selected_index]
            if selected_index in ["NDVI", "SAVI", "EVI", "NDWI"]:
              indices = get_indices(aoi, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), aggregation)
              selected_image = indices[selected_index]
            elif selected_index == "Forest_Loss":
              selected_image = get_forest_loss(aoi)
            elif selected_index == "Carbon_Flux":
              selected_image = get_carbon_flux(aoi, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            else:
                st.error("Invalid selection")
                st.stop()
            
            palettes = {
                "NDVI": ['#d73027', '#f46d43', '#fdae61', '#a6d96a', '#1a9850'],
                "SAVI": ['#a6611a', '#dfc27d', '#80cdc1', '#018571'],
                "EVI": ['#4575b4', '#91bfdb', '#e0f3f8', '#fee090', '#fc8d59', '#d73027'],
                "NDWI":['#0000ff', '#00ffff', '#ffff00', '#ff0000', '#ffffff'],
                "Forest_Loss":['#00FF00', '#ff0000'],
                "Carbon_Flux":['#0e6030','#f0d3df','#262260']

            }
            
            vis_params = {'min': -1, 'max': 1, 'palette': palettes[selected_index], 'opacity': 0.6}
            layer = selected_image.visualize(**vis_params)

     # Calculate min and max values for the selected index
            min_val = selected_image.reduceRegion(
                reducer=ee.Reducer.min(),
                geometry=aoi,
                scale=500,
                bestEffort=True
            ).get(selected_index).getInfo()
            
            max_val = selected_image.reduceRegion(
                reducer=ee.Reducer.max(),
                geometry=aoi,
                scale=500,
                bestEffort=True
            ).get(selected_index).getInfo()


            
            url = layer.getMapId()['tile_fetcher'].url_format
            # st.session_state.layers[selected_index] = {'url': url, 'aoi': aoi}
            st.session_state.layers[selected_index] = {'url': url, 'aoi': aoi, 'image': selected_image}

            # Generate color ramp image and store it
            color_ramp_img, buf = generate_color_ramp_legend(selected_index, min_val, max_val, palettes[selected_index])
            st.session_state.color_ramp_img = color_ramp_img
            st.session_state.color_ramp_buf = buf

            # st.markdown(legend_html, unsafe_allow_html=True)
            st.success(f"{selected_index} (Clipped) added!")


        # Display the color ramp image stored in session state
    if "color_ramp_img" in st.session_state:
        st.image(st.session_state.color_ramp_img, caption=f"{selected_index} Color Ramp", use_container_width=True)

    if st.button("Download Layer as Shapefile"):
      if selected_index in st.session_state.layers and "image" in st.session_state.layers[selected_index]:
        try:
            output_path = f"{selected_index}_vegetation_index.shp"
            shapefile_path = download_shapefile(
                st.session_state.layers[selected_index]['image'],
                st.session_state.layers[selected_index]['aoi'],
                selected_index,
                output_path
            )
            if shapefile_path:
                with open(shapefile_path, "rb") as file:
                    st.download_button(
                        label="Download Shapefile",
                        data=file,
                        file_name=output_path,
                        mime="application/zip"
                    )
        except Exception as e:
            st.error(f"Error generating shapefile: {e}")
    else:
        st.warning("Please load the data first before downloading.")

# Right Panel (Map Display)
with right_panel:
    st.markdown("### 🌍 Vegetation Indices Map")
    folium_map = folium.Map(
        location=st.session_state.aoi_center,
        zoom_start=8,
        tiles="CartoDB positron"
    )
    if "aoi_bounds" in st.session_state:
        folium_map.fit_bounds(st.session_state.aoi_bounds)
    for index, data in st.session_state.layers.items():
        folium.raster_layers.TileLayer(
            tiles=data['url'],
            attr="MODIS",
            name=index,
            overlay=True,
            control=True
        ).add_to(folium_map)
    folium.LayerControl().add_to(folium_map)
    st_folium(folium_map, height=700, width=900)
    
    # if st.button("Generate Time-Series Chart"):
    #     df = get_time_series(st.session_state.layers[selected_index]['aoi'], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), selected_index)
    #     if df is not None:
    #      fig = px.line(df, x='Date', y=selected_index, title=f"{selected_index} Time-Series")
    #     st.plotly_chart(fig)
    if st.button("Generate Time-Series Chart"):
     if selected_index not in st.session_state.layers:
        st.error("Load the data first.")
    else:
        df = get_time_series(st.session_state.layers[selected_index]['aoi'], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), selected_index)
        
        if df is not None and not df.empty:
            fig = px.line(df, x='Date', y=selected_index, title=f"{selected_index} Time-Series")
            st.plotly_chart(fig)
         # Add CSV Download Button
        if not df.empty:
            csv = df.to_csv(index=False).encode("utf-8")
            file_name = f"{selected_index}_time_series_{start_date}_{end_date}.csv"
            st.download_button(
                 label="Download Time-Series Data as CSV",
                 data=csv,
                   file_name=file_name,
                   mime="text/csv"
        )







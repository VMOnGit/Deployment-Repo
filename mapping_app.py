from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES
import urllib.request
import streamlit as st

from utils import (
    st_get_osm_geometries,
    st_plot_all,
    get_colors_from_style,
    gdf_to_bytesio_geojson,
)
from prettymapp.geo import GeoCodingError, get_aoi
from prettymapp.settings import STYLES

st.set_page_config(
    page_title="Current Location", page_icon="🖼️", initial_sidebar_state="collapsed"
)
st.markdown("# Prettymapp")
draw_settings = STYLES["Peach"]
result_container = st.empty()
with st.spinner("Creating map... (may take up to a minute)"):
    
    try:
        aoi = get_aoi(coordinates = [9.5097264651732, 76.55097300000003], radius=1000, rectangular=True)
    except GeoCodingError as e:
        st.error(f"ERROR: {str(e)}")
        st.stop()
    df = st_get_osm_geometries(aoi=aoi)
    config = {
        "aoi_bounds": aoi.bounds,
        "draw_settings": draw_settings,
        "name_on": "my_map",
        "name": "my_map1",
        "font_size": 18,
        "font_color": 'blue',
        "text_x": 0,
        "text_y": 0,
        "text_rotation": 0,
        "shape": "rectangle",
        "contour_width": 12,
        "contour_color": '#FAF9F6',
        "bg_shape": 'rectangle',
        "bg_buffer": 2,
        "bg_color": '#FAF9F6',
    }
    fig = st_plot_all(_df=df, **config)
    # result_container.write(html, unsafe_allow_html=True)
    st.pyplot(fig, pad_inches=0, bbox_inches="tight", transparent=True, dpi=300)

# svg_string = plt_to_svg(fig)
# html = svg_to_html(svg_string)
# st.write("")
# fname = slugify(address)
# img_format = st.selectbox("Download image as", ["svg", "png", "jpg"], index=0)
# if img_format == "svg":
#     data = svg_string
# elif img_format == "png":
#     import io
#
#     data = io.BytesIO()
#     fig.savefig(data, pad_inches=0, bbox_inches="tight", transparent=True)
# st.download_button(label="Download image", data=data, file_name=f"{fname}.{img_format}")

st.markdown("</br>", unsafe_allow_html=True)
st.markdown("</br>", unsafe_allow_html=True)
ex1, ex2 = st.columns(2)


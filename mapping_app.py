from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES
import urllib.request
import streamlit as st
url = "IP-ADRESS-URL-OF-ESP-SERVER"  # ESP's url, ex: https://192.168.102/ (Esp serial prints it when connected to wifi)


#while True:
	#get_data()
aoi = get_aoi(coordinates = [9.505941623973825, 76.54946128618556], radius=1100, rectangular=False)
df = get_osm_geometries(aoi=aoi)

fig = Plot(
    df=df,
    aoi_bounds=aoi.bounds,
    draw_settings=STYLES["Peach"]
).plot_all()


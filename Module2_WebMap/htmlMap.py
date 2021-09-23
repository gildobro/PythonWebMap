import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[43.855216, -79.467542], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html = html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup= str(el)+"m", icon= folium.Icon(color = 'blue')))

map.add_child(fg)

map.save("Map_html_simple_popup.html")
import folium
import pandas as pd

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

data = pd.read_csv("Volcano.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")

##for coordinates in [[38.2,-99.1],[39.2,-95.1]]:
for lt,ln,el in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"m", icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=7, popup=str(el)+"m", fill_color=color_producer(el), color='white', fill_opacity='0.7'))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")

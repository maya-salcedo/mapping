import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data["NAME"])

html = """<h4>Volcano Information:<br>
<a href="<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height:%s m"""

def color_produce(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'pink'
    else:
        return 'blue'

map = folium.Map(location=[34.3693101,-117.9428368],tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="My Map")

#to add multiple Markers, use a for loop
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=str(el)+ " m", fill_color=color_produce(el), color='grey', fill_opacity=0.7))



map.add_child(fg)

map.save("Map1.html")


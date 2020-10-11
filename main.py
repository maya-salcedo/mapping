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

map = folium.Map(location=[44.8921239,-104.6792032],tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name="Volcanoes") #featuredGroup for volcanoes

#to add multiple Markers, use a for loop
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=str(el)+ " m", fill_color=color_produce(el), color='grey', fill_opacity=0.7))
#lambda is used because the function does not need to be called again
#x is the features
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                     else 'red'}))
#x['properties']['POP2005'] --> calling the dictionary that carries the information on the population



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

#this map contains a base layer, marker ayer and polygon layer

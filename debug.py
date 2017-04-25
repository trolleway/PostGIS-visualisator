import os
import psycopg2
import psycopg2.extras
import pprint


	# 1. Define connection string
conn_string = "host=localhost user=user dbname=osmdb password=user"
 

conn = psycopg2.connect(conn_string)
 

cursor = conn.cursor()

f = open('debug_printout.html', 'w')

f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Leaflet.FileLayer Plugin</title>
    <meta charset="utf-8" />
    <link 
        rel="stylesheet" 
        href="http://cdn.leafletjs.com/leaflet-0.7/leaflet.css"
    />
	<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
   <style>
   html, body, #map {
      height:100%;
      width:100%;
      padding:0px;
      margin:0px;
   } 
   </style>

</head>
<body>
    <div id="map"></div>

    <script
        src="http://cdn.leafletjs.com/leaflet-0.7/leaflet.js">
    </script>
    <script>
var DebugData = { "type": "FeatureCollection",
    "features": [''')



# 2. Write SQL here

sql='''
SELECT ST_ASGeoJSON(ST_Transform(wkb_geometry,4326)) as way FROM 
(

--write here

SELECT * 
FROM 
tablename
WHERE
1=1
LIMIT 100

--write here
 
) AS mainquery ;

'''






cursor.execute(sql)
conn.commit()
for row in cursor:
	counter=row[0]
	f.write('''
{ "type": "Feature",
        "geometry": 
''')
	f.write(row[0])
	f.write('''
	},''')


f.write('''
]
     }



        var map = L.map('map').setView([55.666, 37.666], 12);
        mapLink = 
            '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
            }).addTo(map);


	var DebugMapElementsStyle = {
	    "color": "#ff7800",
	    "weight": 5, 
	    "opacity": 0.5
	};

	 var postgisDebug = new L.LayerGroup();
        L.geoJson(DebugData, {style: DebugMapElementsStyle}).addTo(map);

       var bounds = L.latLngBounds(DebugData);
	map.fitBounds(bounds);
	alert('d');

    </script>
</body>
</html>
''')

f.close()

exit()

# Code source (most of it): https://support.esri.com/en/technical-article/000019645

# Import the necessary libraries
import urllib.parse, urllib.request, os, arcpy, json

# Change current working directory (where you want to save your shapefile and json file; otherwise they'll save in the same folder where you have this script)
os.chdir(r"C:\Users\JohnsonN35\Folder")

# Set up variables
cdPath = os.getcwd() # Get current working directory (used below for setting shapefile file path)
jsonName = "newMapService.json" # Change the json file name if desired
shpName = "newMapService.shp" # Change the shapefile file name if desired

# Specify the desired service URL; see end of code comment for instructions on how to get it if unknown
url = "https://gisagocss.state.mi.us/arcgis/rest/services/OpenData/michigan_geographic_framework/MapServer/16/query?"

# You probably won't need to alter anything below this line

# Query the parameters
params = {'where': '1=1',
		   'geometryType': 'esriGeometryEnvelope',
		   'spatialRel': 'esriSpatialRelIntersects',
		   'relationParam': '',
		   'outFields': '*',
		   'returnGeometry': 'true',
		   'geometryPrecision':'',
		   'outSR': '',
		   'returnIdsOnly': 'false',
		   'returnCountOnly': 'false',
		   'orderByFields': '',
		   'groupByFieldsForStatistics': '',
		   'returnZ': 'false',
		   'returnM': 'false',
		   'returnDistinctValues': 'false',
		   'f': 'pjson',
                   'token': " " # See code source for how to deal with tokens
		   }

encode_params = urllib.parse.urlencode(params).encode("utf-8")

# Create a request and read it using urllib
response = urllib.request.urlopen(url, encode_params)
json = response.read()

# Write the JSON response to text file
with open(jsonName, "wb") as ms_json:
    ms_json.write(json)

# Convert JSON to shapefile using the JSONToFeatures function
arcpy.JSONToFeatures_conversion(jsonName, cdPath + "\\\\" + shpName)



# How to get service url:
# 1. Go to the web page you want to get data from.
# 2. Go to the "3 dots" menu in the upper right (Edge or Chrome browsers), navigate to More tools, then click on Developer tools.
# 3. On the page that opens, go to the Network tab and sort the Name field. Look for ?f=json (there may be many instances, and they'll have a number in front, which is the layer ID).
# 4. Hover over ?f=json and browse the service names that appear. When you find the right one, right-click and copy the link address, which should be the service path plus ?f=json.
# 5. Delete ?f=json and after the layer ID, append query? to the service url.
# If you don't see ?f=json with a number in front of it, sort the Type field and browse through anything with types "fetch" or "xhr." Rest of the process will be the same.

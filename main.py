import requests
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Define the Overpass API endpoint
OVERPASS_API_URL = "http://overpass-api.de/api/interpreter"

# Example Overpass QL query: Fetch all parks in a specific area (bounding box)
query = """
[out:json];
area[name="Berlin"];
node["leisure"="park"](area);
out body;
"""

# Send request to the API
response = requests.get(OVERPASS_API_URL, params={"data": query})

# Check for successful response
if response.status_code == 200:
    print("Data fetched successfully!")
    data = response.json()

    print(data)
else:
    print(f"Error: {response.status_code}")
    exit()

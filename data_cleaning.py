import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geoplot as gplt
import geopandas as gpd
from shapely.geometry import Point

DATA_DIR = "data/"

# Load files
data = pd.read_csv(DATA_DIR + 'data_merged.csv', index_col=0)

with open(DATA_DIR + 'Boston_Neighborhoods.geojson') as json_file:
    boston_geojson = json.load(json_file)

# Some slight corrections to the data set
data.amount_ratings_excellent = data.amount_ratings_excellent.str.replace(
    r',', '').astype(int)
data.amount_ratings_average = data.amount_ratings_average.astype(int)
data.amount_ratings_poor = data.amount_ratings_poor.astype(int)
data.amount_ratings_terrible = data.amount_ratings_terrible.astype(int)

# Categories to be removed
categories = np.unique([data.category_1, data.category_2, data.category_3])
price_ranges = ['$', '$$ - $$$', '$$$$']

# Remove the categories from the price_range column and add them to the first
# category column that is empty
for i in range(len(data.price_range)):
    if data.price_range[i] in categories:
        # Remove categories from the price_range column
        category_to_remove = data.price_range[i]
        data.price_range[i] = '0'
        # Once removed we can add the removed
        # cateogry to the other column
        if data.category_1[i] == '0':
            data.category_1[i] = category_to_remove
        else:
            if data.category_2[i] == '0':
                data.category_2[i] = category_to_remove
            else:
                data.category_3[i] = data.category_1[i] = category_to_remove
    else:
        pass

# Handle geographic data: find neighborhood for each data point
df_neighbs = gpd.read_file(DATA_DIR + 'Boston_Neighborhoods.geojson')
df_locations = gpd.GeoDataFrame(
    data, geometry=gpd.points_from_xy(data.longitude, data.latitude))

matched_neighborhoods = []
for i in range(len(df_locations)):
    dummy = 0
    for j in range(len(df_neighbs)):
        if (df_neighbs.geometry[j]).contains(df_locations.geometry[i]):
            dummy = df_neighbs.Name[j]
        else:
            pass
    if dummy != 0:
        matched_neighborhoods.append(dummy)
    else:
        matched_neighborhoods.append(0)


# Save corrected data
# data.to_csv(DATA_DIR + "corrected_merged_data.csv", index=False)

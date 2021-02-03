import pandas as pd
from geopy.geocoders import Nominatim
import time
import math


def geolocator(address_data, geolocator):
    """ Calls the geolocator and gets the coordinates for the addresses.
        The input should be a list of strings containing addresses. """

    # Empty df to store results
    geolocation_results = []
    for address in list(address_data):
        try:
            # Check if there is actually an address stored
            if not address:
                pass
            else:
                geolocated_address = geolocator.geocode(address)
                geolocation_results.append({
                    "direction": address,
                    "latitude": geolocated_address.latitude,
                    "longitude": geolocated_address.longitude,
                    "error": False
                })
                time.sleep(1)
                print('Geolocated {}'.format(address))
        except AttributeError:
            print(
                'No result, skipping {} and appending it to errors array.'.format(address))
            geolocation_results.append({
                "direction": address,
                "longitude": '',
                "latitude": '',
                "error": True
            })
            pass

    return pd.DataFrame(geolocation_results)

# The geolocation can be performed with HERE
# gpd.tools.geocode(addresses.direction, provider='here', user_agent='master-project-Hertforshire', apikey='E_Ql8x525hJ6OjYciBIPDBBe28N-rZ8xjuPEVn-1sAw')

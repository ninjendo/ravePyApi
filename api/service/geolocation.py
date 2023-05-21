import requests
import pygeohash as geo
from api.common.constants import SSM_PARAMS
from api.errors.exceptions import CoordinatesNotFoundError


#
def get_geohash_details(address):
    addr = get_coordinates(address)
    addr["geohash_6"] = geo.encode(addr['latitude'], addr['longitude'], precision=6)
    addr["geohash_7"] = geo.encode(addr['latitude'], addr['longitude'], precision=7)
    addr["geohash_8"] = geo.encode(addr['latitude'], addr['longitude'], precision=8)
    return addr


def get_coordinates(address):
    api_key = SSM_PARAMS['radar']['apiKey']
    base_url = 'https://api.radar.io/v1/geocode/forward?'
    headers = {"Authorization": api_key}

    encoded_address = requests.utils.requote_uri(address)
    url = f'{base_url}query={encoded_address}'

    response = requests.get(url, headers=headers)
    data = response.json()

    if data['meta']['code'] == 200:
        addr = data['addresses'][0]
        return {"address": addr, "latitude": addr['latitude'], "longitude": addr['longitude']}
    else:
        raise CoordinatesNotFoundError(address)

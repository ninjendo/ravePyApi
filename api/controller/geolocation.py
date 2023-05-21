import requests
import logging

from flask.views import MethodView
from flask_smorest import abort, Blueprint

from api.schemas.geolocation import GeoLocation, Coordinates
from api.service.geolocation import get_coordinates, get_geohash_details

LOGGER = logging.getLogger("api.controller.property")

geo_ns = Blueprint('GeoLocation', 'geolocation', url_prefix='/geolocation', description='Property Management')


@geo_ns.route('/address/<address>')
class AddressInfo(MethodView):

    @geo_ns.response(200, GeoLocation)
    def get(self, address):
        """Retrieves address details and coordinates"""
        return get_coordinates(address)


@geo_ns.route('/geohash')
class GeoHash(MethodView):
    """Generates GeoHash"""

    @geo_ns.response(200, GeoLocation)
    @geo_ns.arguments(Coordinates, location='query')
    def get(self, address):
        """Generate geohash for given coordinates"""
        longitude = requests.args.get('long')
        lat = requests.args.get('lat')
        return get_geohash_details(address)

from marshmallow import Schema
from marshmallow.fields import String, Integer, Raw, Dict, Date, Nested


class GeoLocation(Schema):
    address = Raw()
    longitude = String()
    latitude = String()
    geohash_8 = String()
    geohash_7 = String()
    geohash_6 = String()


class Coordinates(Schema):
    long = String()
    lat = String()

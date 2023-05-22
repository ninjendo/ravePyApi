from marshmallow import Schema
from marshmallow.fields import String, Integer, Raw, Dict, Date, Nested, Decimal


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


class RadarAddress(Schema):
    addressLabel = String()
    city = String()
    confidence = String()
    country = String()
    countryCode = String()
    countryFlag = String()
    county = String()
    distance = Integer()
    formattedAddress = String()
    latitude = Decimal()
    longitude = Decimal()
    number = Integer()
    postalCode = Integer()
    state = String()
    stateCode = String()
    street = String()

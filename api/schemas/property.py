from marshmallow import Schema
from marshmallow.fields import String, Integer, Raw, Dict, Date, Nested, List

from api.schemas.geolocation import RadarAddress


class RawProperty(Schema):
    data = Raw()


class RawProperties(Schema):
    data = List(Nested(RawProperty))


class Address(Schema):
    street_num = String()
    street_name = String()
    zip_code = String()
    county = String()
    state = String()
    full_address = String()


class Property(Schema):
    id = String()
    address = Nested(RadarAddress)
    condition = String()
    status = String()
    details = String()
    status_date = Date()
    geo_hash_3 = String()
    geo_hash_5 = String()
    geo_hash_10 = String()


class Properties(Schema):
    properties = List(Nested(Property))

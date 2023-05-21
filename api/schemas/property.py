from marshmallow import Schema
from marshmallow.fields import String, Integer, Raw, Dict, Date, Nested


class Address(Schema):
    street_num = String()
    street_name = String()
    zip_code = String()
    county = String()
    state = String()
    full_address = String()


class Property(Schema):
    id = String()
    address = Nested(Address)
    list_price = Integer()
    arv = Integer()
    property_condition = String()
    market_status = String()
    status_modified_date = Date()
    longitude = String()
    latitude = String()
    geo_hash_3 = String()
    geo_hash_5 = String()
    geo_hash_10 = String()

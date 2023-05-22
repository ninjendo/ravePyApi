import os
from enum import Enum

from api.util.parameter_store import load_ssm_parameter

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
AWS_REGION = 'us-east-1'
RAVE_PARAM_STORE_DEV = '/rave/' + ENVIRONMENT + '/param'
SSM_PARAMS = load_ssm_parameter(RAVE_PARAM_STORE_DEV)

# dynamodb
TABLE_NAME = 'rave_geo'
GEOHASH_7 = {'table': 'rave_geo_7', 'hash_length': 7}
GEOHASH_6 = {'table': 'rave_geo_6', 'hash_length': 6}
KEY_DELIMITER = '#'
ADDRESS_KEY = 'ADDR'
PROPERTY_KEY = 'PROP'
IMAGES_KEY = 'IMAGES'
DETAILS_KEY = 'DET'

MILE_TO_METER_MULTIPLIER = 1609.34


class PropertyCondition(Enum):
    FORECLOSURE = 'foreclosure'
    FIXER = 'fixer upper'
    RENOVATED = 'renovated'
    TLC = 'tlc'
    MOVEIN = 'move-in ready'

class MarketStatus(Enum):
    ACTIVE = 'active'
    NON_INVESTOR = 'non-investor only'
    CLOSED = 'off-market'
    PENDING = 'pending'

EXCLUSIVE = 'exclusive'
EXTENDED = 'extended'
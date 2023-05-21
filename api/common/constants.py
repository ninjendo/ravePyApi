import os

from api.util.parameter_store import load_ssm_parameter

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
AWS_REGION = 'us-east-1'
RAVE_PARAM_STORE_DEV = '/rave/' + ENVIRONMENT + '/param'
SSM_PARAMS = load_ssm_parameter(RAVE_PARAM_STORE_DEV)

#dynamodb
GEOHASH_7 = {'table': 'rave_geo_7', 'hash_length': 7}
GEOHASH_6 = {'table': 'rave_geo_6', 'hash_length': 6}


MILE_TO_METER_MULTIPLIER = 1609.34

import logging

import boto3
import dynamodbgeo
import uuid

import boto3

from api.common.constants import AWS_REGION, MILE_TO_METER_MULTIPLIER

LOGGER = logging.getLogger("api.service.dynamogeo")

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name=AWS_REGION)


def get_config(table_name, hash_length):
    config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, table_name)
    config.hashKeyLength = hash_length
    return config


def check_and_create_table(table_name, hash_length):
    # Check if the table exists
    response = dynamodb.list_tables()
    if table_name in response['TableNames']:
        print(f"The table '{table_name}' already exists.")
    else:
        create_table(table_name, hash_length)


def create_table(table_name, hash_length):
    config = get_config(table_name, hash_length)

    table_util = dynamodbgeo.GeoTableUtil(config)
    create_table_input = table_util.getCreateTableRequest()

    # tweaking the base table parameters as a dict
    create_table_input["ProvisionedThroughput"]['ReadCapacityUnits'] = 5
    create_table_input["ProvisionedThroughput"]['ReadCapacityUnits']['WriteCapacityUnits'] = 1

    # Use GeoTableUtil to create the table
    table_util.create_table(create_table_input)


def save(property, geoDataManager):
    PutItemInput = {
        'Item': {
            'property_id': {'S': property.id},
            'address': {'S': property.address},
            'status': {'S': property.market_status},
            'modified_date': {'N': property.status_modified_date},
        },
        'ConditionExpression': "attribute_not_exists(hashKey)"
    }

    geoDataManager.put_Point(dynamodbgeo.PutPointInput(
        dynamodbgeo.GeoPoint(property.longitude, property.latitude),  # latitude then latitude longitude
        str(uuid.uuid4()),  # Use this to ensure uniqueness of the hash/range pairs.
        PutItemInput  # pass the dict here
    ))


def get_nearby(property, radius_in_miles, geoDataManager):
    result = geoDataManager.queryRadius(
        dynamodbgeo.QueryRadiusRequest(
            dynamodbgeo.GeoPoint(property.longitude, property.latitude),
            radius_in_miles * MILE_TO_METER_MULTIPLIER, None, sort=True))
    return result
import json
import logging
import hashlib
from api.common.constants import KEY_DELIMITER as KD, PROPERTY_KEY, PropertyCondition, MarketStatus, EXTENDED
from api.errors.exceptions import InvalidPropertyDataError, RequestInvalidError, MissingAddressError
from api.model.property import Rave
from api.service.geolocation import get_coordinates, get_geohash_details
from api.service.helper import trim_json, get_full_address

LOGGER = logging.getLogger("api.service.property")


def generate_hash_key(full_address):
    text_bytes = full_address.encode('utf-8')
    md5_hash = hashlib.md5(text_bytes).hexdigest()

    # Return the first 8 characters of the hash as the partition key
    partition_key = md5_hash[:8]
    return partition_key


def transform_key(key, entity_type=None):
    """
    If entity_type is provided, it returns the DB PK form. If not, it returns the raw PK form.
    :param key: primary key
    :param entity_type:
    :return:
    """
    if entity_type:
        if isinstance(key, int):
            return (entity_type + KD + str(key)).upper()
        else:
            return (entity_type + KD + key).upper()
    return key.split('#')[-1:]


def build_address_key(address):
    county = (address['county'].upper().replace("COUNTY", "").strip()) if address.get('county') else ""
    return (address['state'] + KD + county + KD + address['city']+ KD + str(address['postalCode'])).upper()


def save(data):
    """
    Saves property_item in database
    """
    prop = trim_json(data)
    try:
        address = get_full_address(prop)
        addr_details = get_geohash_details(address)
        attn_name = prop['propertyAddress'].get('attnName', None)
        to_name = prop['propertyAddress'].get('toName', None)

        prop['address'] = addr_details
        prop['address']['attn_name'] = attn_name
        prop['address']['to_name'] = to_name
        prop_db = convert_to_db_obj(prop)

        Rave.put(prop_db)
    except MissingAddressError as e:
        raise e
    except Exception as e:
        msg = "Unable to save item: " + prop['address']['formattedAddress']
        LOGGER.error(msg, e)
        raise InvalidPropertyDataError(msg, 400)


def save_all(properties):
    """
    Saves property_item in database
    """
    error_prop = ""
    cnt_error = 0
    for prop in properties:
        try:
            prop_obj = convert_to_db_obj(prop)
            Rave.put(prop_obj)
            LOGGER.info("SAVED: " + prop.address.full_address)
        except Exception as e:
            cnt_error = cnt_error + 1
            error_prop = error_prop + prop.address.full_address + ': ' + str(e) + '\n'
            LOGGER.error("Unable to save item: " + prop.address.full_address, e)
            error_prop.append({'addr': prop.address.full_address, 'error': e})

    if cnt_error == len(properties):
        LOGGER.error("Unable to save item(s): " + error_prop)
        raise RequestInvalidError("Unable to save any data. Please check your request.", 400)

    if cnt_error != 0:
        LOGGER.error("Unable to save item(s): " + error_prop)
        raise InvalidPropertyDataError(error_prop, 400)


def get(property_id):
    """
    Saves property_item in database
    """
    prop_key = transform_key(property_id, PROPERTY_KEY)
    return Rave.get(pk=prop_key, sk=prop_key)


def remove(property_id):
    """
    Deletes property from database
    """
    prop_key = transform_key(property_id, PROPERTY_KEY)
    prop = Rave.get(pk=prop_key, sk=prop_key)
    prop.delete()


def convert_to_db_obj(property_item):
    property_item['id'] = generate_hash_key(property_item['address']['formattedAddress'])
    db_obj = dict()
    prop_key = transform_key(property_item['id'], PROPERTY_KEY)

    prop_details = extract_non_essential_data(property_item)
    db_obj['pk'] = prop_key
    db_obj['sk'] = prop_key
    db_obj['addr_key'] = build_address_key(property_item['address'])
    db_obj['alt_key'] = property_item.get('alternateId', None)
    db_obj['status'] = get_market_status(property_item).value
    db_obj['status_date'] = get_market_status_date(property_item)
    db_obj['condition'] = get_property_condition(property_item).value
    db_obj['details'] = json.dumps(prop_details)
    db_obj['address'] = json.dumps(property_item['address'])

    db_obj['geohash_8'] = property_item['address']['geohash_8']
    db_obj['geohash_7'] = property_item['address']['geohash_7']
    db_obj['geohash_6'] = property_item['address']['geohash_6']

    return db_obj


def get_property_condition(prop_item):
    if prop_item.get('fhaCaseNumber', None) is not None:
        return PropertyCondition.FORECLOSURE
    return PropertyCondition.MOVEIN


def get_market_status(prop_item):
    if prop_item.get('hudListingPeriod', None) is not None:
        return MarketStatus.ACTIVE if prop_item['hudListingPeriod'] is EXTENDED else MarketStatus.NON_INVESTOR
    return MarketStatus.CLOSED


def get_market_status_date(prop_item):
    if prop_item.get('listDate', None) is not None:
        return prop_item['listDate']

def extract_non_essential_data(prop_orig):
    new_prop = prop_orig.copy()
    del new_prop['address']
    del new_prop['propertyAddress']

    if new_prop.get('seller', None) is not None and new_prop['seller'].get('mailingAddress', None) is not None:
        if new_prop['seller']['mailingAddress'].get('streetAddress', None) is None \
                or not bool(new_prop['seller']['mailingAddress']['streetAddress']):
            del new_prop['seller']['mailingAddress']
    return new_prop

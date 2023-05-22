import json

from api.errors.exceptions import MissingAddressError


def get_full_address(property_obj):
    if property_obj.get('propertyAddress', None) is None:
        raise MissingAddressError('Missing "propertyAddress" attribute')
    if property_obj['propertyAddress'].get('postalArea', None) is None:
        raise MissingAddressError('Missing "postalArea" attribute')
    street = property_obj['propertyAddress'].get('streetAddress', None)
    if street is None or street.get('fullStreetAddress', None) is None:
        raise MissingAddressError('Missing "fullStreetAddress" attribute')
    return property_obj['propertyAddress']['streetAddress']['fullStreetAddress'] + ' ' + property_obj['propertyAddress']['postalArea']

def trim_json(json_input):
    data = json_input
    if isinstance(json_input, str):
        data = json.loads(json_input)
    remove_empty_attributes(data)
    #result = json.dumps(data)

    return data


def remove_empty_attributes(obj):
    if isinstance(obj, dict):
        keys = list(obj.keys())
        for key in keys:
            if obj[key] is None or isinstance(obj[key], str) and (obj[key]).strip() == "":
                del obj[key]
            else:
                remove_empty_attributes(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            remove_empty_attributes(item)

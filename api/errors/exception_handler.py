import marshmallow
from flask import jsonify

from api.errors.exceptions import MissingAddressError, InvalidPropertyDataError, RequestInvalidError
from app import APP


@APP.errorhandler(MissingAddressError)
def handle_invalid_usage(error):
    return generic_error_handler(error)


@APP.errorhandler(InvalidPropertyDataError)
def handle_invalid_usage(error):
    return str(error), 400


@APP.errorhandler(RequestInvalidError)
def handle_invalid_usage(error):
    return str(error), 400


@APP.errorhandler(marshmallow.exceptions.ValidationError)
def handle_invalid_usage(error):
    return str(error), 400


def generic_error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

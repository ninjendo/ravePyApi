import marshmallow

from app import APP

@APP.errorhandler(UserNotFoundException)
def handle_invalid_usage(error):
    return generic_error_handler(error)


@APP.errorhandler(marshmallow.exceptions.ValidationError)
def handle_invalid_usage(error):
    return str(error), 400

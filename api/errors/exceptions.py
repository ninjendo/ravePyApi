class AuthError(Exception):
    """Authorization error exception."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(AuthError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class CustomException(Exception):
    """Missing property error."""

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class PropertyNotFoundError(CustomException):
    """Missing property error."""
    pass


class CoordinatesNotFoundError(CustomException):
    """Missing Coordinates error."""
    pass


class InvalidPropertyDataError(CustomException):
    """Invalid property data."""

    pass


class RequestInvalidError(CustomException):
    """Invalid request."""

    pass


class MissingAddressError(CustomException):
    """Missing postal address error."""

    pass

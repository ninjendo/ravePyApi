class AuthError(Exception):
    """Authorization error exception."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(AuthError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class PropertyNotFoundError(Exception):
    """Missing property error."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(PropertyNotFoundError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class CoordinatesNotFoundError(Exception):
    """Missing Coordinates error."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(CoordinatesNotFoundError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class InvalidPropertyDataError(Exception):
    """Invalid property data."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(InvalidPropertyDataError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class RequestInvalidError(Exception):
    """Invalid request."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(RequestInvalidError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class MissingAddressError(Exception):
    """Missing postal address error."""

    def __init__(self, error, status_code):
        """Initializes AuthError."""
        super(MissingAddressError, self).__init__(error)
        self.error = error
        self.status_code = status_code

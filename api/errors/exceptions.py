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

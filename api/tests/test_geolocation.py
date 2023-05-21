from unittest import TestCase, mock
from unittest.mock import MagicMock

from api.controller.geolocation import Coordinates
from api.tests.mock_data.geolocation import MOCK_RADAR_COORDINATES
from api.tests.util import mocked_requests_get
from app import APP


class TestGeolocation(TestCase):

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_get_coordinates(self, met):
        """
        Test Get coordinates
        """
        resp = None
        with APP.test_request_context('/coordinates/<address>'):
            api = Coordinates()
            resp = api.get("963 Moreland Ave Atlanta, GA 30316")

        self.assertEqual(resp.status, "200 OK")

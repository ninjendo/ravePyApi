from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_smorest import Api

from api.common.constants import GEOHASH_7
from api.service.dynamogeo import check_and_create_table
from api.util.logger import setup_logging

APP = Flask(__name__)
APP.config['API_TITLE'] = 'Rave Python API'
APP.config['API_VERSION'] = 'v1'
APP.config['OPENAPI_VERSION'] = '3.0.0'
APP.config['OPENAPI_URL_PREFIX'] = '/'
APP.config['OPENAPI_SWAGGER_UI_PATH'] = '/api/'
APP.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
APP.config['API_SPEC_OPTIONS'] = {
    'security': [{"bearerAuth": []}, {"apiKeyAuth": []}],
    'components': {
        "securitySchemes":
            {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
                ,
                'apiKeyAuth': {
                    'type': 'apiKey',
                    'in': 'header',
                    'name': 'x-api-key'
                }
            }
    }
}

CORS(APP)
Compress(APP)

api = Api(APP)

from api.controller.property import prop_ns
from api.controller.geolocation import geo_ns

api.register_blueprint(prop_ns)
api.register_blueprint(geo_ns)
setup_logging()

if __name__ == '__main__':
    APP.run()

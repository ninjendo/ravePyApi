import logging

from flask.views import MethodView
from flask_smorest import abort, Blueprint

LOGGER = logging.getLogger("api.controller.property")

prop_ns = Blueprint('Property', 'property', url_prefix='/properties', description='Property Management')


@prop_ns.route('/<property_id>')
class GetAssetPreview(MethodView):

    def get(self, property_id):
        """Get Property by ID"""
        return "hello property " + property_id

import logging

from flask.views import MethodView
from flask_smorest import abort, Blueprint

from api.schemas.property import RawProperty, RawProperties
import api.service.property as svc

LOGGER = logging.getLogger("api.controller.property")

prop_ns = Blueprint('Property', 'property', url_prefix='/properties', description='Property Management')


@prop_ns.route('/')
class Property(MethodView):
    @prop_ns.arguments(RawProperty)
    def put(self, data):
        """Save or update a property in database"""
        svc.save(data['data'])

    @prop_ns.arguments(RawProperties)
    def post(self, data):
        """Creates multiple properties in the database"""
        svc.save_all(data)


@prop_ns.route('/<property_id>')
class PropertyById(MethodView):
    def get(self, property_id):
        """Get Property by ID"""
        return svc.get(property_id)

    def delete(self, property_id):
        """Deletes asset from S3 and database"""
        try:
            svc.remove(property_id)
        except Exception as err:
            abort(400, message=str(err))

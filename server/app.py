#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Owner, Property, Apartment, Tenant

class Users(Resource):
    def post(self):
        data = request.get_json()
        user = User(username = data['username'], email = data['email'], password_hash = data['password'])
        db.session.add(user)
        db.session.commit()
        return make_response({'user': user.to_dict()}, 201)


api.add_resource(Users, '/api/v1/users')


class Owners(Resource):
    def post(self):
        data = request.json
        owner = Owner(name = data['name'], contact_info = data['contact_info'], user_id = data['user_id'])
        db.session.add(owner)
        db.session.commit()
        return make_response ( {'owner' : owner.to_dict()}, 201)
    
api.add_resource(Owners, '/api/v1/owners')


class Properties(Resource):
    def post(self):
        data = request.json
        property = Property(owner_id = data['owner_id'], address = data['address'], total_apts = data['total_apts'])
        db.session.add(property)
        db.session.commit()
        return make_response( {'property' : property.to_dict()}, 201)
    
    def get(self):
        all_properties = [ p.to_dict() for p in Property.quert.all()]
        return make_response (all_properties, 200)
    
api.add_resource(Properties, '/api/v1/properties')

class PropertiesById(Resource):
    def get(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response( {'error': 'Property not found.'}, 404 )
        return make_response( property.to_dict(), 200)

api.add_resource(PropertiesById, '/api/v1/properties/<id>')


class Apartments(Resource):
    def get(self):
        all_apartments = [ a.to_dict() for a in Apartment.query.all()]
        return make_response ( all_apartments, 200)
    
    def post(self):
        data = request.json
        apartment = Apartment( property_id = data['property_id'], tenant_id = data['tenant_id'], apt_name = data['apt_name'], lease_start = data["lease_start"], lease_end = data['lease_end'])
        db.session.add(apartment)
        db.session.commit()
        return make_response ( {'apartment': apartment.to_dict()}, 201 )
    
api.add_resource(Apartments, '/api/v1/apartments')

class ApartmentsById(Resource):
    def get(self, id):
        apartment = Apartment.query.get(id)
        if not apartment:
            return make_response( {'error': 'Apartment not found.'}, 404 )
        return make_response( apartment.to_dict(), 200)
    
api.add_resource(ApartmentsById, '/api/v1/apartments/<id>')


class Tenants(Resource):
    def get(self):
        all_tenants = [ t.to_dict() for t in Tenant.query.all()]
        return make_response( all_tenants, 200)

    def post(self):
        data = request.json
        tenant = Tenant(name = data['name'], contact_info = data['contact_info'])
        db.session.add(tenant)
        db.session.commit()
        return make_response( {'tenant': tenant.to_dict()}, 201  )

class TenantsById(Resource):
    def get(self, id):
        tenant = Tenant.query.get(id)
        if not tenant:
            return make_response( {'error': 'Tenant not found.'}, 404 )
        return make_response( tenant.to_dict(), 200)
    
    def patch(self, id):
        tenant = Tenant.query.get(id)
        if not tenant:
            return make_response( {'error': 'Tenant not found.'}, 404 )
        data = request.json
        try:
            for attr in data:
                setattr( tenant, attr, data[attr] )
        except:
            return make_response( { 'error': [ 'Please try again' ] }, 422 )
        db.session.commit()

        return make_response( tenant.to_dict(), 200 )
    
    def delete(self, id):
        tenant = Tenant.query.get(id)
        if not tenant:
            return make_response( {'error': 'Tenant not found.'}, 404 )
        db.session.delete(tenant)
        db.session.commit()
        return make_response('', 204)


api.add_resource(TenantsById, '/api/v1/tenants/<id>')



# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)


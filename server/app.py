#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from flask import jsonify

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
        session['user_id'] = user.id
        return make_response({'user': user.to_dict()}, 201)


api.add_resource(Users, '/api/v1/users')

@app.route('/api/v1/authorized')
def authorized():
    try:
        user = User.query.filter_by(id=session.get('user_id')).first()
        return make_response(user.to_dict(), 200)
    except:
        return make_response({ 'error': 'User not found'}, 404)
    
@app.route('/api/v1/logout', methods=['DELETE'])
def logout():
    session['user_id'] = None
    return make_response('', 204)

@app.route('/api/v1/login', methods=['POST'])
def login():
    if request.method == "POST":
        data = request.json
        username = data['username']
        user = User.query.filter_by(username=username).first()
        try:
            password = data['password']
            if user.authenticate(password):
                # import ipdb; ipdb.set_trace()
                session['user_id'] = user.id
                return make_response({'user': user.to_dict()}, 200)
            else:
                return make_response({'error' : 'incorrect password'}, 401)
        except:
            return make_response({'error': 'username incorrect'}, 401)

class Owners(Resource):
    def post(self):
        data = request.json
        owner = Owner(name = data['name'], contact_info = data['contact_info'], user_id = data['user_id'])
        db.session.add(owner)
        db.session.commit()
        return make_response ( {'owner' : owner.to_dict()}, 201)
    
    def get(self):
        all_owners = [o.to_dict() for o in Owner.query.all()]
        return make_response( all_owners, 200)
    
api.add_resource(Owners, '/api/v1/owners')

@app.route('/api/v1/owners/<owner_id>/properties')
def owner_properties(owner_id):
    owner = Owner.query.get(owner_id)
    if not owner:
        return make_response({'error': 'Owner not found.'}, 404)
    
    properties = Property.query.filter_by(property_id=owner.property.id).all()
    property_data = [p.to_dict() for p in properties]
    
    return jsonify(property_data), 200


@app.route('/api/v1/properties/<property_id>/apartments')
def property_apartments(property_id):
    property = Property.query.get(property_id)

    if not property:
        return make_response({'error': 'Property not found.'}, 404)

    apartments = Apartment.query.filter_by(property_id=property.id).all()
    apartments_data = [apt.to_dict() for apt in apartments]

    return jsonify(apartments_data), 200

@app.route('/api/v1/apartments/<apartment_id>/tenant')
def apartment_tenant(apartment_id):
    apartment = Apartment.query.get(apartment_id)

    if not apartment:
        return make_response({'error': 'Apartment not found.'}, 404)

    tenant = Tenant.query.get(apartment.tenant_id)

    if not tenant:
        return make_response({'error': 'Tenant not found for this apartment.'}, 404)

    return jsonify(tenant.to_dict()), 200

  



class Properties(Resource):
    def post(self):
        data = request.json
        property = Property(owner_id = data['owner_id'], address = data['address'], total_apts = data['total_apts'])
        db.session.add(property)
        db.session.commit()
        return make_response( {'property' : property.to_dict()}, 201)
    
    def get(self):
        all_properties = [p.to_dict() for p in Property.query.all()]
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
    
api.add_resource(Tenants, '/api/v1/tenants')

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



@app.route('/api/v1/tenants/<apt_name>', methods=['POST'])
def add_tenant(apt_name):
    data = request.json
    tenant = Tenant(name=data['name'], contact_info=data['contact_info'])
    db.session.add(tenant)
    db.session.commit()
    
    apartment = Apartment.query.filter_by(apt_name=apt_name).first()
    apartment.tenant_name = apartment.tenant_name + f', {tenant.name}'
    if not apartment:
        db.session.rollback()
        return make_response({'error': 'Apartment not found.'}, 404)
    
    db.session.commit()
    
    return make_response({'tenant': tenant.to_dict()}, 201)

@app.route('/api/v1/tenants/<tenant_id>/update', methods=['PATCH'])
def update_tenant(tenant_id):
    tenant = Tenant.query.get(tenant_id)
    if not tenant:
        return make_response({'error': 'Tenant not found.'}, 404)
    
    data = request.json
    try:
        for attr in data:
            setattr(tenant, attr, data[attr])
    except:
        return make_response({'error': ['Please try again']}, 422)
    
    db.session.commit()

    return make_response(tenant.to_dict(), 200)

@app.route('/api/v1/tenants/<tenant_id>', methods=['DELETE'])
def delete_tenant(tenant_id):
    tenant = Tenant.query.get(tenant_id)
    if not tenant:
        return make_response({'error': 'Tenant not found.'}, 404)
    
    db.session.delete(tenant)
    db.session.commit()
    
    return make_response('', 204)




# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.before_request
def check_logged_id():

    if request.endpoint in ['properties'] and not session.get('user_id'):
        return make_response({'error' : 'unauthorized. Please login'}, 401)


if __name__ == '__main__':
    app.run(port=5555, debug=True)


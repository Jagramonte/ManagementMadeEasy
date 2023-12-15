from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy


from config import db, bcrypt

# Models go here!

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash',)

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    _password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, server_default =db.func.now(), onupdate = db.func.now())

    @property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, plain_text_password):
        byte_object = plain_text_password.encode('utf-8')
        encrypted_password_obj = bcrypt.generate_password_hash(byte_object)
        hashed_password_string = encrypted_password_obj.decode('utf-8')
        self._password_hash = hashed_password_string


    #relationships
    owners = db.relationship('Owner', back_populates = 'user')

        


class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    contact_info = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #relationships
    user = db.relationship('User', back_populates = 'owners')


class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    adderess = db.Column(db.String)
    total_apts = db.Column(db.Integer)

    #relationships
    apartments = db.relationship('Apartment', back_populates = 'property')


class Apartment(db.Model, SerializerMixin):
    __tablename__ = 'apartments'

    id = db.Column(db.Integer, primary_key = True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    apt_name = db.Column(db.String)
    lease_start = db.Column(db.String)
    lease_end = db.Column(db.String)

    #relationships
    property = db.relationship('Property', back_populates = 'apartments')
    tenant = db.relationship('Tenant', back_populates = 'apartments')


class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    contact_info = db.Column(db.String)


    #relationships
    apartments = db.relationship('Apartment', back_populates = 'tenant')

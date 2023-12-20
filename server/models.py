from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy


from config import db, bcrypt

# Models go here!

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash','-owners.user')

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)   #remove later
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

    def authenticate(self, password_string):
        byte_object = password_string.encode('utf-8')
        return bcrypt.check_password_hash(self.password_hash, byte_object)


    #relationships
    owners = db.relationship('Owner', back_populates = 'user')

        


class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    serialize_rules = ('-properties.owner','-users.owner')

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    contact_info = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # def __init__(self,name,contact_info,user_id):
    #     self.name = name
    #     self.contact_info = contact_info
    #     self.user_id = user_id

    #relationships
    user = db.relationship('User', back_populates = 'owners')
    properties = db.relationship('Property', back_populates = 'owner',foreign_keys='Property.owner_id')




class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'

    serialize_rules = ('-owner.properties', '-apartments.properties')

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    owner_name = db.Column(db.String)
    address = db.Column(db.String)
    total_apts = db.Column(db.Integer)

    # def __init__(self,owner_id,owner_name,address,total_apts):
    #     self.owner_id = owner_id
    #     self.owner_name = owner_name
    #     self.adderess = address
    #     self.total_apts = total_apts

    #relationships
    apartments = db.relationship('Apartment', back_populates = 'property')
    owner = db.relationship('Owner', back_populates = 'properties')


class Apartment(db.Model, SerializerMixin):
    __tablename__ = 'apartments'

    id = db.Column(db.Integer, primary_key = True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    tenant_name = db.Column(db.String) #commentoutlater
    apt_name = db.Column(db.String)
    lease_start = db.Column(db.String)
    lease_end = db.Column(db.String)

    # def __init__(self,tenant_id,property_id,tenant_name,apt_name,lease_start,lease_end):
    #     self.tenant_id = tenant_id
    #     self.property_id = property_id
    #     self.tenant_name = tenant_name
    #     self.apt_name = apt_name
    #     self.lease_start = lease_start
    #     self.lease_end = lease_end

    serialize_rules = ('-property.apartments', '-tenant.apartments')

    #relationships
    property = db.relationship('Property', back_populates = 'apartments')
    tenant = db.relationship('Tenant', back_populates = 'apartments',foreign_keys='Apartment.tenant_id')


class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    contact_info = db.Column(db.String)

    serialize_rules = ('-apartments.tenant',)

    #relationships
    apartments = db.relationship('Apartment', back_populates = 'tenant')

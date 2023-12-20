#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Property, Owner, Apartment, Tenant, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        Owner.query.delete()
        Property.query.delete()
        Apartment.query.delete()
        Tenant.query.delete()

        owners = []
        properties=[]
        apartments=[]
        tenants=[]
        
        o1 = owners.append(Owner(name ='Bob Shmob',contact_info ='Bob@mail.com',user_id =10))
        p1 = properties.append(Property(owner_id = 10, owner_name = 'Bob Shmob', address = '123 Fake Street', total_apts ='3 apartments'))
        a1 = apartments.append(Apartment(tenant_id =1,property_id = 1,tenant_name ='Joe',apt_name ='1A',lease_start ='9/11/23', lease_end ='12/22/23'))
        t1 = tenants.append(Tenant(name = 'Joe', contact_info ='Joe@mail.com'))

        db.session.add_all(owners +properties + apartments + tenants)
        db.session.commit()
        

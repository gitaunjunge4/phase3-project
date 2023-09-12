#!/usr/bin/env python3

from faker import Faker
import random 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import SaleRepresentative, Product, Customer 

if __name__ == '__main__':

    engine = create_engine('sqlite:///sales.db')
    session = sessionmaker()(bind=engine)

    session.query(SaleRepresentative).delete()
    session.query(Product).delete()
    session.query(Customer).delete()

    fake = Faker()

    print("Genrerating Sale Representatives...")

    salereps = [
        SaleRepresentative(
            name=fake.unique.name(), 
            email=fake.unique.email(),
            region=fake.country(),
            phone_number=fake.phone_number(),
        )
    for i in range(20)]

    # print(salereps)
    session.bulk_save_objects(salereps)
    session.commit()


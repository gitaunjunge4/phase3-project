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


    #generates sake salerepresentatives details and saves it to the db
    print("Genrerating Sale Representatives...")
    
    salereps = [ 
        SaleRepresentative(
            name=fake.unique.name(), 
            email=fake.unique.email(),
            region=fake.country(),
            phone_number=fake.phone_number(),
        )

    for i in range(10)]
    # print(salereps)
    session.bulk_save_objects(salereps)
    session.commit()
    

    #generates fake product details and saves it to the db
    print("Generating store Products...")

    store_products = ["Milk", "Bread", "Cookies", "Salt", "Sugar", "Butter",
                    "Apple", "Crisps", "Book", "Soda", "Tomatoes", "Kales",
                    "Cabbage", "Lotion", "Tissue", "Toothbrush", "Toothpaste",
                    "Water", "Black Pepper", "Duvet"]
    
    products = [
        Product(
                name=random.choice(store_products), 
                price=round(random.uniform(4.65, 89.98), 2)
        )
    for i in range(50)]
    session.bulk_save_objects(products)
    session.commit()
     




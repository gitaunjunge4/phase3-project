#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import SaleRepresentative, Product, Customer, purchase

if __name__ == '__main__':

    engine = create_engine('sqlite:///sales.db')
    session = sessionmaker()(bind=engine)

    import ipdb; ipdb.set_trace()

    
#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (Column, Integer, String, 
    Float, ForeignKey, DateTime, CheckConstraint, UniqueConstraint)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db')

Base = declarative_base()

class SaleRepresentative(Base):
    __tablename__ = 'salesreps'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    region = Column(String())
    phone_number = Column(Integer(), unique=True, nullable=False)

    #Establish a one-to-many relationship between SaleRepresentative and Customer
    customers = relationship("Customer", back_populates='salesrep')

    def __repr__(self):
        return f"Sale_Representative {self.id}:"\
            + f"Name: {self.name}, " \
            + f"Email: {self.email}," \
            + f"Region: {self.region}," \
            + f"Phone: {self.phone_number}"
    

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    def __repr__(self):
        return f"Product ID {self.id}:"\
            + f"Name: {self.name}, " \
            + f"Price: {self.price}"
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    phone_number = Column(Integer(), nullable=False)
    address = Column(String(), nullable=False)
    sale_rep = Column(Integer(), ForeignKey('salesreps.id'))
    
    #Establish a many-to-one relationship between Customer and SaleRepresentative
    salesrep = relationship('SaleRepresentative', back_populates='customers')
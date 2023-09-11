#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, 
    DateTime, CheckConstraint, UniqueConstraint)

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

    def __repr__(self):
        return f"Sale_Representative {self.id}:"\
            + f"Name: {self.name}, " \
            + f"Email: {self.email}," \
            + f"Region: {self.region}," \
            + f"Phone: {self.phone_number}"
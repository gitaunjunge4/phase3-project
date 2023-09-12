from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String, 
    Float, ForeignKey, DateTime, Table, MetaData)
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


#Defining the relationship table between Customers and Products using table Purchase
purchase= Table(
    'purchases',
    Base.metadata, 
    Column('ID', Integer(), primary_key=True),
    Column('Bought at', DateTime(), server_default=func.now()),
    Column('Product ID', ForeignKey('products.id')),
    #Column('Product Name', ForeignKey('products.name')),
    Column('Customer ID', ForeignKey('customers.id')),
    #Column('Customer Name', ForeignKey('customers.name')),
    extend_existing=True,
)


#Defining the SaleRepresentative table
class SaleRepresentative(Base):
    __tablename__ = 'salesreps'

    id = Column(Integer(), primary_key=True)
    name = Column(String(55), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    region = Column(String())
    phone_number = Column(Integer(), nullable=False)

    #Establish a one-to-many relationship between SaleRepresentative and Customer
    customers = relationship("Customer", back_populates='salesrep')

    def __repr__(self):
        return f"Sale Representative ID: {self.id} "\
            + f"Name: {self.name}, " \
            + f"Email: {self.email}, " \
            + f"Region: {self.region}, " \
            + f"Phone Number: {self.phone_number}."
    

#Defining the Product table
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    #Establish an asssociation with Customer using the purchase association table
    customers = relationship("Customer", secondary=purchase, backref='products')

    def __repr__(self):
        return f"Product ID {self.id}:"\
            + f"Name: {self.name}, " \
            + f"Price: Ksh {self.price}"
    

#Defining the Customer table
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    phone_number = Column(Integer(), nullable=False)
    address = Column(String(), nullable=False)
    sale_rep = Column(Integer(), ForeignKey('salesreps.id'))

    #Establish an asssociation with Product using the purchase association table
    #products = relationship('Product', secondary=purchase, back_populates='customers')

    #Establish a many-to-one relationship between Customer and SaleRepresentative
    salesrep = relationship('SaleRepresentative', back_populates='customers', foreign_keys=[sale_rep])

    

    def __repr__(self):
        return f"Customer ID: {self.id}, "\
            + f"Name: {self.name}, " \
            + f"Phone Number: {self.phone_number}, "\
            + f"Address: {self.address}, " \
            + f"Sale_rep: {self.sale_rep}. "
    



    
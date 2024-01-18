from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    comment = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

    # Define the relationships
    customer = relationship('Customer', back_populates='customer_reviews', overlaps="reviews_customers")
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps="reviews_restaurants")

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    name = Column(String, nullable=False)

    # Define the relationships
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers', overlaps="restaurants_customers")
    customer_reviews = relationship('Review', back_populates='customer', overlaps="reviews_customers")

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)

    # Define the relationships
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants', overlaps="customers_restaurants")
    reviews = relationship('Review', back_populates='restaurant', overlaps="reviews_restaurants")

# Create an SQLite database engine
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

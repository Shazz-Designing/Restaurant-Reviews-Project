from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

restaurant1 = Restaurant(name='Java', price=3)
restaurant2 = Restaurant(name='Art Cafe', price=2)

customer1 = Customer(first_name='Shazz', last_name='Adot')
customer2 = Customer(first_name='Jane', last_name='Juma')

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

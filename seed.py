from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed data

# Restaurants
restaurant1 = Restaurant(name='Hilton', price=5)
restaurant2 = Restaurant(name='Art Cafe', price=4)
restaurant3 = Restaurant(name='Kilimanjaro', price=3)
restaurant4 = Restaurant(name='Sonford', price=2)
restaurant5 = Restaurant(name='Kibandaski', price=1)

# Customers
customer1 = Customer(first_name='Shazz', last_name='Adot')
customer2 = Customer(first_name='Jane', last_name='Juma')
customer3 = Customer(first_name='Martin', last_name='Gitonga')

# Reviews
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)
review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)
review4 = Review(star_rating=5, restaurant=restaurant4, customer=customer1)
review5 = Review(star_rating=2, restaurant=restaurant5, customer=customer2)
review6 = Review(star_rating=5, restaurant=restaurant1, customer=customer3)
review7 = Review(star_rating=3, restaurant=restaurant2, customer=customer1)
review8 = Review(star_rating=3, restaurant=restaurant3, customer=customer2)
review9 = Review(star_rating=4, restaurant=restaurant4, customer=customer3)
review10 = Review(star_rating=5, restaurant=restaurant5, customer=customer1)

session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, customer1, customer2, customer3, review1, review2, review3, review4, review5, review6, review7, review8, review9, review10])
session.commit()

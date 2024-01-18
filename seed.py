from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Customer, Restaurant, Review

# Create an SQLite database
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)

# Create a session to interact with the database
session = Session(engine)

# Create and add more sample data
customer1 = Customer(first_name='Shazz', last_name='Adot', name='Shazz Adot')
customer2 = Customer(first_name='Jane', last_name='Juma', name='Jane Juma')
customer3 = Customer(first_name='Martin', last_name='Gitonga', name='Martin Gitonga')

restaurant1 = Restaurant(name='Hilton', price=5)
restaurant2 = Restaurant(name='Kempinsky', price=3)
restaurant3 = Restaurant(name='Spice Palace', price=4)
restaurant4 = Restaurant(name='Sonford', price=2)
restaurant5 = Restaurant(name='kibandasky', price=3)

review1 = Review(comment='Great place!', customer=customer1, restaurant=restaurant1)
review2 = Review(comment='Nice atmosphere!', customer=customer2, restaurant=restaurant2)
review3 = Review(comment='Amazing food!', customer=customer3, restaurant=restaurant3)
review4 = Review(comment='Good service!', customer=customer1, restaurant=restaurant4)
review5 = Review(comment='Friendly staff!', customer=customer2, restaurant=restaurant5)
review6 = Review(comment='Delicious dishes!', customer=customer3, restaurant=restaurant1)
review7 = Review(comment='Quick service!', customer=customer1, restaurant=restaurant2)
review8 = Review(comment='Cozy ambiance!', customer=customer2, restaurant=restaurant3)
review9 = Review(comment='Affordable prices!', customer=customer3, restaurant=restaurant4)
review10 = Review(comment='Excellent experience!', customer=customer1, restaurant=restaurant5)

# Add data to the session
session.add_all([customer1, customer2, customer3, restaurant1, restaurant2, restaurant3, restaurant4, restaurant5,
                 review1, review2, review3, review4, review5, review6, review7, review8, review9, review10])

# Commit the changes to the database
session.commit()

# Query and print data for verification
customers = session.query(Customer).all()
print("Customers:", customers)

restaurants = session.query(Restaurant).all()
print("Restaurants:", restaurants)

reviews = session.query(Review).all()
print("Reviews:", reviews)

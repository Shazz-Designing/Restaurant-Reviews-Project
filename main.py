from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an SQLite database engine
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Review class methods
review = session.query(Review).first()
customer_instance = review.customer() if review else None
restaurant_instance = review.restaurant() if review else None

print(f"Review customer: {customer_instance}")
print(f"Review restaurant: {restaurant_instance}")

# Restaurant class methods
restaurant = session.query(Restaurant).first()
reviews_collection = restaurant.reviews() if restaurant else None
customers_collection = restaurant.customers() if restaurant else None
review = session.query(Review).first()
print(f"Review for {review.restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars.")

restaurant = session.query(Restaurant).filter_by(name='Hilton').first()
if restaurant:
    print(restaurant.all_reviews())
else:
    print("Restaurant not found.")

# Customer class methods
customer = session.query(Customer).first()
reviews_collection = customer.reviews() if customer else None
restaurants_collection = customer.restaurants() if customer else None

print(f"Customer reviews: {reviews_collection}")
print(f"Customer restaurants: {restaurants_collection}")

# Customer aggregate and relationship methods
print(f"Customer full name: {customer.full_name() if customer else None}")
print(f"Customer favorite restaurant: {customer.favorite_restaurant().name if customer else None}")

# Adding a new review for a customer
new_review = Review(star_rating=4, restaurant=restaurant, customer=customer)
session.add(new_review)
session.commit()

# Deleting all reviews for a restaurant for a customer
customer.delete_reviews(restaurant)
session.commit()

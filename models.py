from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    @classmethod
    def fanciest(cls):
        # Restaurant instance with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()

    def reviews(self):
        # Collection of all the reviews for the restaurant
        return [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def full_name(self):
        # Full name of the customer, with first name and last name concatenated
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Restaurant instance with the highest star rating from this customer
        highest_rated_review = max(self.reviews, key=lambda review: review.star_rating, default=None)
        return highest_rated_review.restaurant if highest_rated_review else None

    def add_review(self, restaurant, rating):
        # New review for the restaurant with the given restaurant_id
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        # Remove all reviews for this restaurant
        reviews_to_delete = session.query(Review).filter_by(customer=self, restaurant=restaurant).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        # String formatted as specified in the deliverables
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

# Create an SQLite database engine
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

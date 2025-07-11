from app import app, db
from models import User, Restaurant, Dish, Review

def create_sample_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        user1 = User(username='Sairaj')
        user2 = User(username='Jayashree')
        res1 = Restaurant(name='Great Indian Curry House')
        res2 = Restaurant(name='Hyderabadi Delights')
        dish1 = Dish(name='Spicy Paneer Tikka', description='Grilled paneer with a spicy marinade.', price=250, restaurant=res1)
        dish2 = Dish(name='Creamy Chicken Pasta', description='Pasta in a rich and creamy white sauce with chicken.', price=350, restaurant=res2)
        dish3 = Dish(name='Mushroom Masala', description='A savory dish with mushrooms in a tangy tomato gravy.', price=220, restaurant=res1)
        dish4 = Dish(name='Cheesy Garlic Bread', description='Crispy bread with garlic and lots of cheese.', price=180, restaurant=res2)
        review1 = Review(text="Loved the spicy paneer! So well cooked and perfectly savory.", rating=5, user=user1, dish=dish1)
        review2 = Review(text="The chicken was tender and the sauce was so creamy and cheesy. A bit bland though.", rating=4, user=user1, dish=dish2)
        review3 = Review(text="The paneer was not spicy at all. Very disappointing.", rating=2, user=user2, dish=dish1)
        review4 = Review(text="Absolutely loved how cheesy and crispy this was. The perfect appetizer!", rating=5, user=user2, dish=dish4)
        db.session.add_all([user1, user2, res1, res2, dish1, dish2, dish3, dish4, review1, review2, review3, review4])
        db.session.commit()
        print("Sample data created successfully!")
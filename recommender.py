from models import User, Dish, Review
from nlp_processor import analyze_review_text

def build_user_taste_profile(user_id):
    user_reviews = Review.query.filter_by(user_id=user_id).all()
    
    taste_profile = {
        "attributes": {},
        "ingredients": {}
    }

    for review in user_reviews:
        analysis = analyze_review_text(review.text)
        if analysis['sentiment'] == 'positive' or review.rating >= 4:
            for attr in analysis['attributes']:
                taste_profile['attributes'][attr] = taste_profile['attributes'].get(attr, 0) + 1
            for ing in analysis['ingredients']:
                taste_profile['ingredients'][ing] = taste_profile['ingredients'].get(ing, 0) + 1
    
    return taste_profile

def get_dish_recommendations(user_id):
   
    taste_profile = build_user_taste_profile(user_id)
    all_dishes = Dish.query.all()
    
    recommendations = []

    for dish in all_dishes:
        score = 0
        
        dish_text = (dish.name + " " + dish.description).lower()
        
        for attr, count in taste_profile['attributes'].items():
            if attr in dish_text:
                score += count

        for ing, count in taste_profile['ingredients'].items():
            if ing in dish_text:
                score += count

        if score > 0:
            recommendations.append({"dish": dish.name, "restaurant": dish.restaurant.name, "score": score})

    recommendations.sort(key=lambda x: x['score'], reverse=True)
    
    return recommendations
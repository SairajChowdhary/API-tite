from app import app
from models import User, Review, Dish
from recommender import get_dish_recommendations

def evaluate_recommender():
    
    total_users_tested = 0
    successful_predictions = 0

    with app.app_context():
        users = User.query.all()
        for user in users:
            positive_review_to_hide = None
            for review in user.reviews:
                if review.rating >= 4:
                    positive_review_to_hide = review
                    break 

            if not positive_review_to_hide:
                continue 

            original_reviews = list(user.reviews)
            user.reviews.remove(positive_review_to_hide)
            
            total_users_tested += 1

            recommendations = get_dish_recommendations(user.id)[:3]
            recommended_dish_names = [rec['dish'] for rec in recommendations]

            hidden_dish_name = Dish.query.get(positive_review_to_hide.dish_id).name
            print(f"Testing for user: {user.username}")
            print(f"Hiding liked dish: '{hidden_dish_name}'")
            print(f"Top 3 recommendations: {recommended_dish_names}")

            if hidden_dish_name in recommended_dish_names:
                successful_predictions += 1
                print("--> SUCCESS!\n")
            else:
                print("--> FAIL\n")

            user.reviews = original_reviews

    if total_users_tested == 0:
        print("No users with positive reviews to test.")
        return 0

    hit_rate = (successful_predictions / total_users_tested) * 100
    return hit_rate

if __name__ == '__main__':
    print("--- Starting Recommender Evaluation ---")
    final_score = evaluate_recommender()
    print("--- Evaluation Complete ---")
    print(f"Final Top-3 Hit Rate: {final_score:.2f}%")
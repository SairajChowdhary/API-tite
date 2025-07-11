from flask import Flask, jsonify, request
from models import db
from recommender import get_dish_recommendations

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gourmetgo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/setup', methods=['POST'])
def setup_database():
    """Endpoint to set up the database with sample data."""
    # ADD THE IMPORT HERE, INSIDE THE FUNCTION
    from sample_data import create_sample_data
    create_sample_data()
    return jsonify({"message": "Database setup complete."})

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def recommend_dishes(user_id):
    """
    Returns dish recommendations for a given user.
    """
    recommendations = get_dish_recommendations(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
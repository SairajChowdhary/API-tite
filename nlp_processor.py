import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')


ATTRIBUTES = ['spicy', 'sweet', 'sour', 'cheesy', 'creamy', 'crispy', 'tangy', 'savory']
INGREDIENTS = ['chicken', 'paneer', 'mushroom', 'beef', 'pork', 'fish', 'potato', 'tomato', 'onion']

def analyze_review_text(text):
    
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    
    sentiment = 'positive' if sentiment_score >= 0.05 else 'negative' if sentiment_score <= -0.05 else 'neutral'

    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]

    extracted_attributes = [token for token in filtered_tokens if token in ATTRIBUTES]
    extracted_ingredients = [token for token in filtered_tokens if token in INGREDIENTS]

    return {
        "sentiment": sentiment,
        "attributes": list(set(extracted_attributes)),
        "ingredients": list(set(extracted_ingredients))
    }
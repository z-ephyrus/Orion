from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def get_sentiment(cleaned_text_string):
    scores = sid.polarity_scores(cleaned_text_string)
    
    return scores
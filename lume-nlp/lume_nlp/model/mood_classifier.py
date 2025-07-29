from transformers import pipeline

#creating pipeline object
sentiment_pipeline = pipeline("sentiment-analysis")

#define classify_mood function
def classify_mood(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    label = result['label']

    if label == 'POSITIVE':
        return "happy"
    elif label == 'NEGATIVE':
        return "sad"
    else:
        return "neutral"
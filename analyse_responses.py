import spacy
from textblob import TextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def extract_key_phrases(text):
    doc = nlp(text)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

def overall_quality_assessment(sentiment, key_phrases):
    if sentiment == "Positive" and key_phrases:
        return "High Quality"
    elif sentiment == "Negative":
        return "Low Quality"
    else:
        return "Medium Quality"

def main():
    responses = []
    with open("responses.txt", "r") as file:
        response = ""
        for line in file:
            if line.strip() == "":
                if response:
                    responses.append(response.strip())
                    response = ""
            else:
                response += line + " "
        if response:  # for the last response
            responses.append(response.strip())
    
    for i, response in enumerate(responses):
        sentiment = analyze_sentiment(response)
        key_phrases = extract_key_phrases(response)
        quality_assessment = overall_quality_assessment(sentiment, key_phrases)
        
        print(f"Response {i+1}:")
        print(f"Text: {response}")
        print(f"Sentiment: {sentiment}")
        print(f"Key Phrases: {key_phrases}")
        print(f"Overall Quality: {quality_assessment}\n")

if __name__ == "__main__":
    main()

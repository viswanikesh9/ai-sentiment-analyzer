from textblob import TextBlob

print("AI Sentiment Analyzer")
print("---------------------")

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("\nSentiment:", sentiment)
print("Polarity Score:", round(polarity, 2))

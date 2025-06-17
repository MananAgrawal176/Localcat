import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

positive_reviews = [
    "Absolutely loved this film! A must-watch.",
    "storyline and brilliant acting. Highly recommend.",
    "The movie was fantastic from start to finish.",
    "Heartwarming and beautifully shot. I smiled the whole time.",
    "An inspiring and uplifting experience.",
    "Top-notch performance by the lead actor. Very enjoyable.",
    "One of the best movies I've seen this year.",
    "A delightful film with a powerful message.",
    "Perfect blend of humor and emotion. Loved it!",
    "A cinematic masterpiece. Would watch again!"
] * 5

negative_reviews = [
    "The movie was painfully slow and boring.",
    "Poor acting and an even worse storyline.",
    "I regret wasting my time on this film.",
    "It made no sense and was horribly executed.",
    "The worst movie I’ve seen in years.",
    "Disappointing. I had high hopes but it fell flat.",
    "Unoriginal plot and lifeless characters.",
    "Too predictable and not engaging at all.",
    "Bad direction and poor editing ruined it.",
    "Nothing about this movie worked for me."
] * 5

Review = positive_reviews + negative_reviews
Sentiment = ['Positive']*50 + ['Negative']*50

df = pd.DataFrame({
    'Review': Review,
    'Sentiment': Sentiment
})

vectorizer = CountVectorizer(stop_words='english', max_features=500)
X = vectorizer.fit_transform(df['Review'])
y = df['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train ,y_train)

pred= model.predict(X_test)
accuracy = accuracy_score(y_test, pred)
# print (accuracy)


def predict_review_sentiment(model , vectorizer , review):
    vector = vectorizer.transform([review])
    prediction = model.predict(vector)[0]
    return prediction


Single_review= "IT is not a great movie to watch"

print(predict_review_sentiment(model, vectorizer, Single_review))

# Required libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Example dataset
file_path = "C:/Master Degree/Programs/Advanced Programming/adv-programming/weekly_hws/1-SpamDetection/SMSSpamCollection"

data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:  # Ensure there are both message and label
            type, message = parts
            data.append((message, type))

# Separating the data and labels
texts = [text for text, label in data]
labels = [label for text, label in data]


# Splitting the dataset
text_train, text_test, label_train, label_test = train_test_split(texts, labels, test_size=0.33, random_state=42)

# Vectorizing the text data
vectorizer = CountVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(text_train)
X_test = vectorizer.transform(text_test)

# Training the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, label_train)

# Making predictions
predictions = classifier.predict(X_test)

# Evaluating the classifier
print(f"Accuracy: {accuracy_score(label_test, predictions)}")
print("Classification Report:")
print(classification_report(label_test, predictions))
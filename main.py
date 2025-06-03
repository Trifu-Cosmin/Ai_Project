import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# 1. Încarcă datele
df = pd.read_csv("phishing_email.csv")

# 2. Setăm X (text) și y (etichetă)
X = df['text_combined']
y = df['label']

# 3. Împărțim datele în train și test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Vectorizare text cu TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Antrenare model Naive Bayes
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Predictii
y_pred = model.predict(X_test_vec)

# 7. Evaluare
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

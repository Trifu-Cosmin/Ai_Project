import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Încarcă datasetul
df = pd.read_csv("phishing_email.csv")
X = df['text_combined']
y = df['label']

# Împărțire în train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizare TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Salvare model și vectorizator
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print(" Modelul și vectorizatorul au fost salvate cu succes.")

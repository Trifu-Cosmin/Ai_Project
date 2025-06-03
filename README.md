# Ai_Project
#  Phishing Email Detector (University Project)

This project was built as part of a university assignment, but it ended up teaching me a lot more than I expected — from handling real-world datasets to working with machine learning pipelines. It’s a phishing email detector that uses classical machine learning to distinguish between phishing and legitimate emails.

Even though it's academic in origin, I tried to build it like a real-world project — organized code, reusable components, and clear outputs.

---

##  What's Inside

Phising E-mail detector with ML/
├── app.py # Simple app interface for predictions
├── main.py # Main script for training the model
├── save_model.py # Handles saving the trained model
├── phishing_model.pkl # Trained machine learning model
├── vectorizer.pkl # Saved text vectorizer (TF-IDF)
├── logs.txt # Training logs and outputs
├── *.csv # Various phishing and spam datasets
└── phishing-dataset/ # Backup of all dataset files

---

##  Datasets Used

I used several publicly available datasets to train the model. These include:

- **CEAS 2008**
- **Enron**
- **Ling-Spam**
- **SpamAssassin**
- **Nazario**
- **Nigerian Fraud**
- **phishing_email.csv** (Custom)

The goal was to mix real phishing examples with legitimate emails from different sources to improve the accuracy and generalization of the model.

---

##  What the Project Does

1. **Preprocesses text data** from various email datasets  
2. **Vectorizes the text** using TF-IDF  
3. **Trains a machine learning model** (e.g., Naive Bayes or Logistic Regression)  
4. **Saves the model and vectorizer** using `pickle`  
5. **Runs predictions** using a basic interface (`app.py`)  

---

##  How to Run It

### 1. Install Requirements

If you don’t already have the necessary packages:

```bash
pip install -r requirements.txt
```
2. Train the Model
```bash
python main.py
```
This will train the model, log the performance, and save the model/vectorizer to .pkl files.


3. Predict New Emails
```bash
python app.py
```
This script loads the saved model and vectorizer so you can test predictions on custom email texts.


 What I Learned
How to clean and process real-world text data
The power and limitations of traditional machine learning on NLP tasks
How to structure a project for both academic and real-world use
Saving and loading models for reuse
Working with multiple messy datasets and combining them effectively

 Possible Improvements
Add a web interface using Streamlit or Flask
Try out deep learning models like LSTM or BERT
Use email metadata (e.g., sender domain) in addition to text
Add live email scanning or Gmail API integration

 Notes
This was a university project, but it helped me understand a lot of practical machine learning workflows. It's definitely not perfect, but it's a great starting point if you're also learning or need inspiration for a similar assignment.

Feel free to fork, copy, or build on it!

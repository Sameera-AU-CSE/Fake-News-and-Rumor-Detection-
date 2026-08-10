# Fake News and Rumor Detection System Using NLP & Machine Learning

An end-to-end Machine Learning and Natural Language Processing (NLP) system designed to detect and classify fake news and online rumors across multiple datasets.

---

##  Project Overview
Misinformation and online rumors spread rapidly across social media platforms. This project implements a full-stack Machine Learning pipeline and web application to automatically analyze, classify, and verify news and rumor texts in real-time.

---

## 🛠️ Tech Stack & Methods

* **Preprocessing & NLP:** Python, RegEx, NLTK, Scikit-Learn (`TF-IDF Vectorizer`, `CountVectorizer`)
* **Machine Learning Algorithms:** Logistic Regression, Naive Bayes, Support Vector Machines (SVM)
* **Backend:** Python API framework
* **Frontend:** HTML5, CSS3, JavaScript

---

##  End-to-End Workflow

1. **Dataset Collection & Preprocessing:**
   * Handled two separate datasets: **Fake vs. Real News** and **Fake vs. Real Rumors**.
   * Performed thorough data cleaning using Regular Expressions (Regex), punctuation removal, missing value handling, and tokenization/lemmatization.

2. **Feature Extraction (NLP):**
   * Transformed raw unstructured text into numerical feature representations using both **CountVectorizer** and **TF-IDF Vectorization**.

3. **Model Training & Evaluation:**
   * Trained and evaluated three core ML algorithms across both datasets: **Logistic Regression**, **Naive Bayes**, and **Support Vector Classifier (SVM)**.
   * **Key Finding:** Logistic Regression consistently achieved the highest accuracy and best performance across both datasets.

4. **Web Application Integration:**
   * Integrated trained model pipelines with a backend API service.
   * Connected the backend API to an intuitive HTML frontend for real-time user input and prediction display.

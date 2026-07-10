# AI-Based Mental Health Support Chatbot

## Overview

An AI-powered chatbot that provides mental health support using Natural Language Processing, Emotion Recognition, Machine Learning, and Retrieval-Augmented Generation.

---

## Features

- Mental health condition classification
- Emotion detection
- Context-aware response generation
- Conversation memory
- Safety risk detection
- MongoDB conversation storage

---

## System Architecture

User

↓

Flask Frontend

↓

Flask REST API

↓

AI Pipeline

↓

ML Models + RAG

↓

MongoDB


---

## Technologies Used

### Backend

- Python
- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Machine Learning

- Scikit-learn
- TF-IDF
- Logistic Regression

### NLP

- Transformers
- RoBERTa
- GoEmotions

### Retrieval

- FAISS
- Sentence Transformers

### Database

- MongoDB


---

## Dataset

### Kaggle Mental Health Dataset

Used for mental health classification.

### GoEmotions Dataset

Used for emotion recognition.

### Reddit Mental Health Dataset

Used for response retrieval.


---

## Installation

Clone repository:

```bash
git clone <repository-url>
Install dependencies:
pip install -r requirements.txt

Run Backend
python backend/app.py

Run Frontend
python frontend/app.py

Example
Input:
"I feel anxious about my future"
Output:
Emotion:
Fear
Condition:
Anxiety
Response:
"Let's discuss what is making you feel worried."

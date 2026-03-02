Mobile Addiction Analyzer

Mobile Addiction Analyzer is a Machine Learning-based web application developed using Python and Streamlit to predict the level of mobile addiction based on user behavioral inputs.
The system analyzes factors such as screen time, social media usage, sleep disturbance, and dependency patterns, and provides real-time addiction level predictions using a trained ML classification model.
This project demonstrates the practical implementation of data preprocessing, model training, model serialization, and deployment of an AI solution through an interactive web interface.
Tech Stack

Programming Language: Python
Machine Learning: Scikit-learn
Model Serialization: Joblib
Frontend & Deployment: Streamlit
Data Handling: Pandas, NumPy
⚙️ Features

Interactive user input form
Pre-trained Machine Learning model integration
Real-time prediction results
Clean and responsive Streamlit UI
Lightweight and easy to deploy
🧠 Machine Learning Workflow

Data Collection
Data Preprocessing
Feature Encoding
Model Training
Model Evaluation
Model Saving using Joblib
Deployment with Streamlit
📂 Project Structure


Mobile_Addiction_Analyzer/
│
├── app.py                      # Main Streamlit application
├── mobile_addiction_model.pkl  # Trained ML model
├── encoder.pkl                 # Label encoder (if used)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

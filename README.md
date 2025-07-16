# Diabetes Prediction Using SVM

## Project Overview
This project implements a machine learning model to predict diabetes risk based on clinical features. The Support Vector Machine (SVM) algorithm is used to classify whether a person is diabetic or not.

---

## Technologies and Tools Used

- **Python 3.x** — Programming language used for development.
- **Pandas** — For data manipulation and analysis.
- **NumPy** — For numerical operations.
- **scikit-learn (sklearn)** — Machine learning library for model training, scaling, and evaluation.
  - `StandardScaler` for feature scaling.
  - `train_test_split` to split data into training and testing sets.
  - `SVC` (Support Vector Classifier) for classification.
  - `accuracy_score` to evaluate model performance.
- **Flask** — Lightweight web framework to create the API endpoint for predictions.
- **flask-cors** — To handle Cross-Origin Resource Sharing (CORS) for frontend-backend communication.
- **jQuery** — For making AJAX requests from the frontend (optional, can be replaced with fetch API).

---

## Dataset
The model is trained on the [Pima Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database) which contains medical diagnostic measurements.

---

## Features Used
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

---

## How to Run

1. Clone the repository.

2. Install required packages:
    ```bash
    pip install numpy pandas scikit-learn flask flask-cors
    ```

3. Train the model or load pre-trained model artifacts.

4. Run the Flask API server:
    ```bash
    python app.py
    ```

5. Use the frontend HTML/JS to send input data and get predictions.

---

## Project Structure


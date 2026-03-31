# 🏥 Multiple Disease Prediction System WebApp

An AI-powered healthcare web application developed using **Streamlit** that predicts multiple diseases using Machine Learning models. This system integrates four disease prediction modules and provides accurate results based on user input.

---

## 🚀 Diseases Covered

* 🩺 Diabetes Prediction System
* ❤️ Heart Disease Prediction System
* 🧠 Parkinson Disease Prediction System
* 🎗️ Breast Cancer Prediction System

---

## 📌 Overview

This web application allows users to select from multiple disease prediction systems and generate predictions based on medical input features. Each model is built using proper data analysis, preprocessing, and optimization techniques to ensure high accuracy and reliability.

---

## ⚙️ Installation

Clone the repository
Navigate to the project directory
Install the required dependencies

# Navigate to the project folder
cd Multiple-Disease-Prediction-System

# Install dependencies
pip install -r requirements.txt
```


## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run Multiple_Disease_Prediction.py
```

👉 The app will open in your browser.
👉 Select a disease from the sidebar and enter input values to get predictions.

---

## 📊 Dataset Description

### 🩺 Diabetes Prediction

* 768 records, 8 features
* Includes glucose, blood pressure, insulin, etc.

### ❤️ Heart Disease Prediction

* 1025 records, 14 features
* Includes age, chest pain type, resting BP, etc.

### 🧠 Parkinson Disease Prediction

* 195 records, 22 features
* Includes vocal frequency & amplitude variations

### 🎗️ Breast Cancer Prediction

* 569 records, 30 features
* Includes radius, texture, perimeter, area

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Scikit-learn**
* **XGBoost**
* **Pandas & NumPy**
* **Matplotlib & Seaborn**

---

## 🧠 Model Development Process

* Data Collection & Analysis (EDA)
* Data Preprocessing

  * Missing values handling
  * Outlier detection
  * Encoding
  * Feature scaling
* Model Selection
* Feature Selection (RFE)
* Hyperparameter Tuning (GridSearchCV)
* Final Model Training & Evaluation

---

## 🤖 Models Used

### 🩺 Diabetes

* Support Vector Classifier
* Logistic Regression
* Random Forest

### ❤️ Heart Disease

* XGBoost
* Random Forest
* Logistic Regression

### 🧠 Parkinson

* K-Nearest Neighbour
* XGBoost
* Random Forest

### 🎗️ Breast Cancer

* Logistic Regression
* XGBoost
* K-Nearest Neighbour

---

## 📈 Model Evaluation

| Disease       | Model               | Accuracy |
| ------------- | ------------------- | -------- |
| Diabetes      | Random Forest       | 75.32%   |
| Heart         | XGBoost / RF        | 100%     |
| Parkinson     | KNN                 | 100%     |
| Breast Cancer | Logistic Regression | 97.36%   |

---

## 📌 Conclusion

This system provides a user-friendly interface for predicting multiple diseases with high accuracy. It helps in early diagnosis and supports better healthcare decision-making.

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud**.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 👩‍💻 Author

**Vaika Prajapati**

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

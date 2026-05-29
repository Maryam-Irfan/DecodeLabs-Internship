# K-Nearest Neighbors (KNN) Classification using Iris Dataset

A beginner-friendly Machine Learning project implementing the **K-Nearest Neighbors (KNN)** algorithm using the famous **Iris Dataset** in Python with **Scikit-learn** and **Google Colab**.

This project demonstrates the complete supervised learning workflow including:

* Data loading
* Data preprocessing
* Feature normalization
* Train-test splitting
* K-value tuning
* Model training
* Prediction
* Performance evaluation

---

# Project Overview

The goal of this project is to classify iris flowers into different species based on their physical measurements.

The project uses:

* **K-Nearest Neighbors (KNN)** for classification
* **StandardScaler** for feature normalization
* **Error-rate tuning graph** for selecting optimal K value
* **Scikit-learn** for machine learning implementation

---

# Dataset

The project uses the built-in **Iris Dataset** provided by Scikit-learn.

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

# Technologies Used

* Python
* Google Colab
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

# Machine Learning Workflow

## 1. Data Loading

The Iris dataset is loaded using Scikit-learn.

## 2. Data Splitting

The dataset is divided into:

* Training Data
* Testing Data

## 3. Feature Scaling

Data normalization is performed using:

```python
StandardScaler()
```

This improves KNN performance because KNN is distance-based.

## 4. K-Value Tuning

Different K values are tested to identify the optimal number of neighbors.

An error-rate graph is plotted for analysis.

## 5. Model Training

The KNN classifier is trained using the training dataset.

## 6. Prediction & Evaluation

The trained model predicts flower classes on unseen test data.

Evaluation metrics include:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

# Project Structure

```bash
├── knn_classification.ipynb
├── README.md
```

---

# Installation & Usage

## Run on Google Colab

Open the notebook in:

[https://colab.research.google.com/](https://colab.research.google.com/)

Upload the `.ipynb` file and run all cells.

---

# Required Libraries

Install dependencies if needed:

```bash
pip install numpy pandas matplotlib scikit-learn
```


---

# Results

The model achieved high classification accuracy on the Iris dataset after normalization and K-value tuning.

The project successfully demonstrated:

* Supervised learning
* Classification using KNN
* Feature scaling
* Hyperparameter tuning
* Model evaluation

---

# Future Improvements

Possible future enhancements include:

* Cross-validation
* Testing on larger datasets
* Comparing with other algorithms

  * Logistic Regression
  * Decision Trees
  * SVM
* Hyperparameter optimization

---

# Concepts Covered

* Supervised Learning
* Classification
* K-Nearest Neighbors (KNN)
* Euclidean Distance
* Data Normalization
* Feature Scaling
* Hyperparameter Tuning

---

# References

## Documentation

* [Scikit-learn Documentation](https://scikit-learn.org/stable/?utm_source=chatgpt.com)
* [Google Colab](https://colab.research.google.com/?utm_source=chatgpt.com)

---

# Author

Developed by Maryam Irfan as part of an Artificial Intelligence classification project (Decode Labs Internship) using Machine Learning and KNN.

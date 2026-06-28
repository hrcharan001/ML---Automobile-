# 🚗 AutoValue-Predictor - End-to-End Automobile Price Prediction System

An end-to-end Machine Learning project that predicts the selling price of an automobile based on its specifications. This project demonstrates the complete lifecycle of a real-world ML application—from data preprocessing and feature engineering to model deployment as a REST API using Flask and Vercel.

> Turning raw automobile data into accurate price predictions with Machine Learning.

---

## 📌 Project Overview

Pricing an automobile depends on several technical and physical characteristics such as engine size, horsepower, fuel type, body style, dimensions, drive wheels, and many more.

In this project, a Machine Learning model has been trained to learn these relationships and estimate the market price of a vehicle.

The project also exposes the trained model through a REST API, making it ready for integration into web or mobile applications.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Missing Value Handling
- Numerical & Categorical Feature Processing
- Pipeline-Based Machine Learning Workflow
- Linear Regression Model
- REST API using Flask
- Deployment Ready using Vercel
- Serialized Model using Pickle
- Scalable Project Structure

---

## 📊 Dataset Information

The dataset contains various automobile specifications including:

- Symboling
- Make
- Fuel Type
- Aspiration
- Number of Doors
- Body Style
- Drive Wheels
- Engine Location
- Wheel Base
- Length
- Width
- Height
- Curb Weight
- Engine Type
- Number of Cylinders
- Engine Size
- Fuel System
- Bore
- Stroke
- Compression Ratio
- Horsepower
- Peak RPM
- City MPG
- Highway MPG

### Target Variable

**Price**

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection

Imported automobile dataset using Pandas.

### 2. Data Cleaning

- Replaced invalid values (`?`) with NaN
- Converted required columns to numeric
- Removed rows with missing target values

### 3. Data Preprocessing

- Missing value imputation
- Numerical feature scaling
- Categorical feature encoding
- Pipeline-based preprocessing

### 4. Model Training

Model Used:

- Linear Regression

### 5. Model Evaluation

Performance measured using:

- R² Score

### 6. Model Serialization

Saved the trained pipeline using Pickle for deployment.

---

## 🌐 REST API

The project includes a Flask API.

### Home Endpoint

```
GET /
```

Returns

```text
🚗 Automobile Prediction API is Live!
```

### Prediction Endpoint

```
POST /predict
```

Example JSON Input

```json
{
  "make":"toyota",
  "fuel-type":"gas",
  "body-style":"sedan",
  "engine-size":130,
  "horsepower":111,
  "peak-rpm":5000,
  "height":54.5
}
```

Example Response

```json
{
    "status":"success",
    "predicted_price":15234.67
}
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- Pickle
- Vercel

---

## 📈 Learning Outcomes

This project strengthened my understanding of:

- Data preprocessing techniques
- Feature engineering
- Machine Learning pipelines
- Regression algorithms
- Model serialization
- API development with Flask
- Deployment workflows
- Production-ready ML project structure

---

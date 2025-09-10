# UCI Heart Disease Prediction

A simple and interactive **Streamlit** web application that predicts the presence of heart disease using machine learning models trained on the UCI Heart Disease Dataset.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Demo](#demo)  
- [Model & Results](#model--results)  
- [Project Structure](#project-structure)  
- [Future Work](#future-work)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)

---

## About

This project delivers a user-friendly web interface where users input key medical features—such as age, chest pain type, maximum heart rate, fasting blood sugar, etc.—and receive a real-time prediction on the presence of heart disease.

---

## Features

- Hosted on **Streamlit** for ease of use  
- Accepts clinical inputs: `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`  
- Predicts heart disease risk via a trained machine learning model  

---

## Dataset

- Utilizes the **UCI Heart Disease Dataset**, specifically the Cleveland subset, containing 14 key clinical attributes.  
- The “target” label indicates the presence (1–4) or absence (0) of heart disease.  
- For this project, it's treated as a **binary classification**:  
  - `0` = no disease  
  - `1` = disease  

Dataset reference: [UCI Machine Learning Repository - Heart Disease](https://archive.ics.uci.edu/dataset/45/heart%2Bdisease)

---



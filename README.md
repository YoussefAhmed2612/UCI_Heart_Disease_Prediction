# ❤️ UCI Heart Disease Prediction

This project is a **Streamlit web app** that predicts the likelihood of heart disease based on patient health data. It uses the **UCI Heart Disease Dataset (Cleveland subset)** and machine learning models built with **Scikit-learn**.

---

## 🔍 About the Project
- Input clinical data such as **age, cholesterol, blood pressure, chest pain type**, and more.  
- The model predicts **0 = No Disease** or **1 = Disease Present**.  
- Built to demonstrate how **machine learning can be applied in healthcare**.

---

## 📊 Dataset
- Source: [UCI Repository - Heart Disease](https://archive.ics.uci.edu/dataset/45/heart%2Bdisease)  
- Attributes: 14 medical features (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal).  
- Target: `0` (no disease), `1` (disease present).

---

## ⚙️ Installation

Clone the repo and install requirements:

git clone https://github.com/YoussefAhmed2612/UCI_Heart_Disease_Prediction.git
cd UCI_Heart_Disease_Prediction
pip install -r requirements.txt


---

## 🚀 Usage

Run the app locally with Streamlit:

streamlit run app.py


---

## 📷 Demo

Add screenshots in the `assets/` folder and they will appear here:

- Home Screen  
- Prediction Example

---

## 📂 Project Structure

├── app.py # Main Streamlit app
├── model/ # Trained ML model
├── data/ # Dataset or preprocessing code
├── requirements.txt # Dependencies
└── README.md


---

## 📈 Results

- Baseline models tested: Logistic Regression, SVM, Random Forest  
- Metrics evaluated: Accuracy, Precision, Recall, ROC–AUC

---

## 🔮 Future Improvements

- Add visualization of feature importance  
- Compare deep learning approaches  
- Deploy to Heroku or Streamlit Cloud for easy public access

---

## 🤝 Contributing

1. Fork the repo  
2. Create a branch  
3. Commit your changes  
4. Open a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- UCI Machine Learning Repository  
- Built with Python, Scikit-learn, Pandas, Streamlit

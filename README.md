
# ThinkNeu — AI-Powered Startup Prediction Platform

ThinkNeu is a web platform that empowers **entrepreneurs** and **investors** with AI-driven insights to evaluate the success potential of startups. Built using Flask and TensorFlow, the platform predicts the probability of a startup's success based on historical and business features.

---

## 🚀 Features

### 🌐 Website Interface
- Tailwind CSS-powered responsive UI
- Role-based onboarding for Entrepreneurs and Investors
- Clean dashboards for both CEOs and Investors
- Seamless Login/Register workflow

### 🤖 AI-Powered Startup Prediction
- Predicts startup success likelihood using a trained TensorFlow model
- Takes into account funding history, category, investor types, and other features
- Presents results directly in the CEO dashboard

---

## 📁 Project Structure

```
startup_predictor_app/
│
├── app.py                       # Flask app with ML prediction logic
├── model.h5                     # Trained TensorFlow model
├── scaler.pkl                   # Scikit-learn scaler for preprocessing
├── templates/
│   ├── ceos-dashboard.html      # Entrepreneur dashboard (integrated with model output)
│   ├── investors-dashboard.html# Investor view
│   ├── Login.html               # User login
│   ├── register.html            # User registration
│   └── onboarding.html          # Role selector (Investor/Entrepreneur)
├── static/                      # (Optional) for CSS/JS/image assets
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/your-username/thinkneu.git
cd startup_predictor_app
```

### 2. 🧪 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

**OR** manually:

```bash
pip install flask numpy==1.26.4 joblib tensorflow scipy
```

> ⚠️ Important: Use `numpy<2.0` to avoid incompatibilities with `scaler.pkl` and TensorFlow.

### 4. 🧠 Ensure Model Files Exist

- `model.h5` — TensorFlow model
- `scaler.pkl` — Preprocessing scaler (must match the training environment)

Both should be in the same directory as `app.py`.

---

## 🖥️ Running the App Locally

```bash
python app.py
```

Then open in your browser:

```
http://127.0.0.1:5000/
```

---

## 🧾 Prediction Workflow

1. CEO logs in and accesses the dashboard
2. Fills out the startup metrics form
3. Submits form to `/predict`
4. Backend preprocesses input, applies ML model
5. Result (success probability & verdict) is displayed in the same page

---

## 🧠 Tech Stack

- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Backend**: Flask (Python)
- **ML Model**: TensorFlow/Keras
- **Preprocessing**: Scikit-learn `StandardScaler` (via `joblib`)
- **Data**: Startup features like funding, category, and investors

---

## ✅ TODO (Suggestions)

- Add user authentication backend (JWT or Flask-Login)
- Persist startup submissions to a database (SQLite/PostgreSQL)
- Add investor dashboard filtering/sorting for startups
- Improve prediction explanations with SHAP or similar

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙌 Acknowledgements

- [TailwindCSS](https://tailwindcss.com/)
- [TensorFlow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/)

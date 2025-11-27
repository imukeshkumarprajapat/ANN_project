# 🌸 Iris Flower Classification (ANN + Streamlit)

This project demonstrates how to build and deploy an **Artificial Neural Network (ANN)** using TensorFlow/Keras to classify Iris flowers into three species: *Setosa*, *Versicolor*, and *Virginica*.  
The model is deployed as an interactive **Streamlit web app** where users can input flower measurements and get real‑time predictions.

---

## 🚀 Features
- Preprocessing with **StandardScaler** and **LabelEncoder** (saved as `.pkl` files).
- ANN model trained on the Iris dataset, saved in **native Keras format (`.keras`)**.
- Interactive **Streamlit UI** for user input and prediction.
- Clean and beginner‑friendly code structure for easy understanding.

---

## 📂 Project Structure

├── app.py # Streamlit application ├── ann_model.keras # Trained ANN model ├── scaler.pkl # Saved StandardScaler ├── label_encoder.pkl # Saved LabelEncoder ├── requirements.txt # Project dependencies └── README.md # Project documentation

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/iris-ann-streamlit.git
   cd iris-ann-streamlit

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3.Install dependencies:

pip install -r requirements.txt


▶️ Usage
Run the Streamlit app:

Open the browser at http://localhost:8501 and enter flower measurements:

Sepal Length

Sepal Width

Petal Length

Petal Width

The app will display the predicted species

📦 Requirements
Main dependencies:

streamlit

numpy

pandas

scikit-learn

tensorflow

matplotlib (optional for visualization)

seaborn (optional for visualization)


🌐 Deployment
You can deploy this app easily on:

Streamlit Cloud → Upload repo, it auto‑detects requirements.txt.


✨ Future Improvements
Add probability/confidence scores in predictions.

Visualize decision boundaries.

Extend to other datasets for demo purposes.

👨‍💻 Author
Developed by Mukesh Prajapat Location: Rajasthan, India 🇮🇳 Focus: ANN projects, Streamlit dashboards, recruiter‑ready ML apps.
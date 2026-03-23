🎓 Student Performance Prediction System

🔗 GitHub Repository: View Project Repository

An end-to-end Machine Learning pipeline project that predicts student math performance using advanced regression models and a production-ready deployment with Flask.

🚀 Project Overview

This project demonstrates a complete ML lifecycle, from data preprocessing to model deployment:

📊 Achieved 88% R² accuracy using ensemble learning models
⚡ Improved model performance by ~12% with hyperparameter tuning
🌐 Built a Flask web application for real-time predictions
🔁 Designed a modular and scalable pipeline architecture
🧠 Machine Learning Pipeline

The project follows a structured pipeline approach inspired by real-world ML systems:

Data Ingestion → Load and validate dataset
Data Transformation → Feature engineering with ColumnTransformer
Model Training → Train multiple models (CatBoost, XGBoost, Random Forest)
Model Evaluation → Select best-performing model
Prediction Pipeline → Serve predictions via Flask

📌 This modular structure follows best practices used in production ML systems

🛠️ Tech Stack
🔹 ML & Data Processing
Python
Pandas, NumPy
Scikit-learn
CatBoost, XGBoost
🔹 Model Optimization
GridSearchCV
Cross-Validation
Hyperparameter Tuning
🔹 Deployment
Flask
HTML/CSS
🔹 Engineering Practices
OOP & Modular Architecture
Logging & Exception Handling
Model Serialization (Pickle)
Git & GitHub
📊 Key Features
✅ End-to-end ML pipeline (training → deployment)
✅ Handles 1000+ student records
✅ Automated preprocessing (encoding + scaling)
✅ Real-time prediction system (<1s latency)
✅ Clean, reusable, and scalable codebase
📈 Results
Metric	Value
R² Score	0.88
Performance Improvement	+12%
Response Time	< 1 second
Dataset Size	1000+ records
🖥️ Demo

Users can input student data through the web interface and instantly receive predicted performance scores.

📂 Project Structure
src/
│── components/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│
│── pipeline/
│   ├── train_pipeline.py
│   ├── predict_pipeline.py
│
│── utils/
│   ├── logger.py
│   ├── exception.py
│
templates/
artifacts/
app.py
requirements.txt
⚙️ Installation & Usage
# Clone the repository
git clone https://github.com/mosbahiibtihel/mlproject.git

# Navigate to project folder
cd mlproject

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py


👤 Author
Ibtihel Mosbahi
GitHub: https://github.com/mosbahiibtihel

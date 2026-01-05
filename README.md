# Production Grade ML Pipeline with ZenML ⚙️

An end-to-end production-style machine learning pipeline built using ZenML, with a primary focus on MLOps concepts and pipeline design rather than optimizing core machine learning performance. The objective of this project was to understand how to structure, orchestrate, and run reproducible machine learning workflows using modular pipeline steps. This pipeline was built by following the YouTube video [MLOps Course – Build Machine Learning Production Grade Projects](https://www.youtube.com/watch?v=-dJPoLm_gtE), published by [freeCodeCamp](https://www.youtube.com/@freecodecamp), and was adapted through hands-on experimentation and debugging.

---

## Pipeline Steps 🔄

1. **Data Ingestion**
   - Loads raw data from a CSV source

2. **Data Cleaning & Preprocessing**
   - Drops unused timestamp and identifier columns
   - Handles missing values
   - Filters numeric features
   - Splits data into train/test sets

3. **Model Training**
   - Trains a Linear Regression model using scikit-learn

4. **Model Evaluation**
   - Computes:
     - Mean Squared Error (MSE)
     - Root Mean Squared Error (RMSE)
     - R² Score

5. **Pipeline Orchestration**
   - Managed by ZenML

---

## Demo 🔮

<img width="823" height="312" alt="Screenshot 2026-01-05 at 12 25 01 pm" src="https://github.com/user-attachments/assets/0fa23176-3a24-4261-8694-56e44736b2c3" />
<img width="624" height="597" alt="Screenshot 2026-01-05 at 12 27 00 pm" src="https://github.com/user-attachments/assets/9f4e4a60-4dec-4da9-b403-101be6eff701" />


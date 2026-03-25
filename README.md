# 👶 Predicting Infant Survival & Causal Inference  
### Shaked Michaeli & Almog Vainshenker

---

## 📌 Project Overview

In this project, we analyzed large-scale real-world medical data in order to predict infant survival and explore causal relationships affecting infant outcomes.

The dataset was obtained from the **NCHS (National Center for Health Statistics, part of the CDC)**.

We used the dataset:  
**"Birth Cohort Linked Birth – Infant Death Data Files"**,  
which links birth certificate data with infant death records (within the first year of life).

These notebooks are continuation notebooks that work on the full cleaned dataset.

---

## 📊 Dataset

- Main dataset: 2015 data (used for model training and evaluation)  
- Additional dataset: 2014 data (used for robustness testing)  

The dataset is provided as a ZIP file in this repository.

⚠️ Important:  
Before running the notebooks, make sure to unzip the dataset.

---

## 📁 Project Structure

project/  
├── EDA Part Final.ipynb  
├── Model Part Final.ipynb  
├── README.md  
├── requirements.txt  
├── unzip_data.py  
├── data.zip  

After extracting:

data/  
├── final_data_df_2014.csv  
├── final_data_df_2015.csv  
├── manipulation_df_2014.csv
├── manipulation_df_2015.csv

---

## 📘 Notebooks Explanation

### 🔹 EDA Notebook
This notebook includes:
- Data loading  
- Data cleaning  
- Handling missing values  
- Feature exploration  
- Visualizations and insights  

---

### 🔹 Models Notebook
This notebook includes:
- Feature engineering  
- Model training  
- Hyperparameter tuning (GridSearch)  
- Model comparison  
- Robustness testing (noise injection, 2014 data)  
- Causal inference analysis:
  - Propensity Score  
  - T-Learner  
  - S-Learner  
  - Matching  

---

## 🤖 Models Used

We implemented and compared the following models:

- Logistic Regression  
- Random Forest Classifier  
- Neural Network (MLP)  
- XGBoost  

We also used:
- StandardScaler for preprocessing  
- GridSearchCV for hyperparameter tuning  

---

## 🏆 Final Model

The best-performing model was XGBoost, achieving:

- Recall: ~75.8%  
- Strong performance on imbalanced data  

Best hyperparameters:

- colsample_bytree = 0.8  
- learning_rate = 0.1  
- max_depth = 5  
- n_estimators = 200  
- subsample = 0.8  

---

## 📈 Evaluation Metrics

We evaluated models using:

- Accuracy  
- Precision  
- Recall (main focus due to class imbalance)  
- F1 Score  
- Log Loss  

Special emphasis was placed on Recall, since missing positive cases is critical in this domain.

---

## 🧪 Robustness & Stability

We tested the model using:

- Data from a different year (2014)  
- Noise injection experiments  
- Model stability across different data sizes  

These tests showed that the model is robust and stable, with only moderate performance degradation under noise.

---

## 🔍 Causal Inference

Beyond prediction, we explored causal relationships using:

- Propensity Score Modeling  
- T-Learner  
- S-Learner  
- Matching  

This allowed us to estimate the effect of smoking (CIG) on infant outcomes.

---

## ⚙️ How to Run the Project

### 1. Clone the repository

git clone <your-repo-link>  
cd <your-repo-folder>  

---

### 2. Install dependencies

pip install -r requirements.txt  

---

### 3. Unzip the dataset

python unzip_data.py  

---

### 4. Select the correct kernel

Open the notebook in Jupyter or VS Code and select the Python environment where the dependencies were installed.

---

### 5. Run the notebooks

Run all cells from top to bottom.

---

## 📚 Libraries Used

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- xgboost  
- statsmodels  
- jupyter  

---

## 📖 Learning Sources

- Causal Inference YouTube Series  
- scikit-learn documentation  
- XGBoost documentation  
- pandas documentation  
- statsmodels documentation  

---

## 👨‍💻 Authors

- Shaked Michaeli  
- Almog Vainshenker  

---

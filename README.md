# 👶 Predicting Infant Survival & Causal Inference

### Shaked Michaeli & Almog Vainshenker

---

## 📌 Project Overview

In this project, we analyzed large-scale real-world medical data in order to predict infant survival and explore causal relationships affecting infant outcomes.

The dataset was obtained from the [**NCHS ( National Center for Health Statistics, part of the CDC )**](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm).

We used the dataset:
**"Birth Cohort Linked Birth – Infant Death Data Files"**,
which links birth certificate data with infant death records (within the first year of life).

These notebooks are continuation notebooks that work on the full cleaned dataset. 

The target variable (Y) represents infant survival outcome.

---

## 📊 Dataset

* Main dataset: 2015 data (used for model training and evaluation)
* Additional dataset: 2014 data (used for robustness testing)

⚠️ **Important:**
Due to GitHub file size limitations, the dataset is **not included** in this repository.

You can download the dataset (ZIP file) from here:
👉 [Download Dataset](https://drive.google.com/file/d/1TMT003JsmqF49mMviKO6Z-J54S_i63b2/view?usp=sharing)

---

## 📥 Setup Instructions

After downloading:

1. Place the ZIP file inside the project folder (`infant-survival-project`)
2. Run the following command:

```bash
python unzip_data.py
```

This will automatically extract the dataset into a `data/` folder.

⚠️ Make sure that after extraction, the structure is:

```text
data/  
├── final_data_df_2014.csv  
├── final_data_df_2015.csv  
├── manipulation_df_2014.csv  
├── manipulation_df_2015.csv  
```

---

## 📁 Project Structure

```text
infant-survival-project/  
├── EDA Part Final.ipynb  
├── Model Part Final.ipynb  
├── README.md  
├── requirements.txt  
├── unzip_data.py  
├── data/  
│   ├── final_data_df_2014.csv  
│   ├── final_data_df_2015.csv  
│   ├── manipulation_df_2014.csv  
│   ├── manipulation_df_2015.csv  
```

---

## 📘 Notebooks Explanation

### 🔹 EDA Notebook

This notebook includes:

* Data loading
* Data cleaning
* Handling missing values
* Feature exploration
* Visualizations and insights

---

### 🔹 Models Notebook

This notebook includes:

* Feature engineering
* Model training
* Hyperparameter tuning (GridSearch)
* Model comparison
* Robustness testing (noise injection, 2014 data)
* Causal inference analysis:

  * Propensity Score
  * T-Learner
  * S-Learner
  * Matching

---

## 🤖 Models Used

We implemented and compared the following models:

* Logistic Regression
* Random Forest Classifier
* Neural Network (MLP)
* XGBoost

We also used:

* StandardScaler for preprocessing
* GridSearchCV for hyperparameter tuning

---

## 🏆 Final Model

The best-performing model was XGBoost, achieving:

* Recall: ~75.8%
* Strong performance on imbalanced data

Best hyperparameters:

* colsample_bytree = 0.8
* learning_rate = 0.1
* max_depth = 5
* n_estimators = 200
* subsample = 0.8

---

## 📈 Evaluation Metrics

We evaluated models using:

* Accuracy
* Precision
* Recall (main focus due to class imbalance)
* F1 Score
* Log Loss

Special emphasis was placed on Recall, since missing positive cases is critical in this domain.

---

## 🧪 Robustness & Stability

We tested the model using:

* Data from a different year (2014)
* Noise injection experiments
* Model stability across different data sizes

These tests showed that the model is robust and stable, with only moderate performance degradation under noise.

---

## 🔍 Causal Inference

Beyond prediction, we explored causal relationships using:

* Propensity Score Modeling
* T-Learner
* S-Learner
* Matching

This allowed us to estimate the effect of smoking (CIG) on infant outcomes.

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/almogvain11-beep/Predicting-infant-chances-of-survival-causal-inference---Shaked-Almog.git infant-survival-project
cd infant-survival-project
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Download and extract the dataset

Download from:
https://drive.google.com/file/d/1TMT003JsmqF49mMviKO6Z-J54S_i63b2/view?usp=sharing

Then run:

```bash
python unzip_data.py
```

---

### 4. Select the correct kernel

Open the notebook in Jupyter or VS Code and select the Python environment where the dependencies were installed.

---

### 5. Run the notebooks

Run all cells from top to bottom.

---

### 6. ⚠️Important note⚠️

The notebooks are computationally intensive and require sufficient system resources.

---

## 📚 Libraries Used

The project was implemented using the following Python libraries:
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* xgboost
* statsmodels

---

## Useful information

* If you would like to know more about the different variables, their meaning and the meaning of their encoding, please visit [this link](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/cohortlinked/LinkCO15Guide.pdf)

* Or find the 2015 User’s guide for the Birth Cohort Linked Birth files (Which are free for public use) in the [NCHS website](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm#:~:text=Birth%20%E2%80%93%20Infant%20Death%20Data%20Files-,User%E2%80%99s%20Guide%C2%A0(.pdf%20files),-U.S.%20Data%20(.zip%20files))

---
## 📖 Special Thanks

* To our project facilitator, who accompanied us throughout the entire project and program (the project is the final product of the 3-year program) and taught us about the world of data analysis, artificial intelligence, and machine learning, and helped us even late at night.
* 
* For Brady Neal for their Causal Inference Course - If you would like to know about the course [please follow this link](https://www.bradyneal.com/causal-inference-course)

---

## 👨‍💻 Authors

* Shaked Michaeli
* Almog Vainshenker

### About us👩‍🤝‍👨
```text
We are both 17 years old, and this project is the result of a 3-year after-school program.  
The program focused on data analytics, data science, machine learning,
and artificial intelligence, both theoretically and practically using Python.
```

---

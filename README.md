# Spam Detection Using Machine Learning

### Overview
This repository contains the implementation details and code for a spam detection system using machine learning. The project focuses on creating a reliable and effective model for identifying spam emails in a diverse dataset.

### Implementation Details

#### 4.1 Dataset
The dataset consists of email data with both spam and non-spam (ham) emails. It includes textual content along with corresponding categories. The balanced distribution of spam and non-spam emails allows effective learning, preventing bias towards one category.

- **File:** mail_data.csv
- **Columns:**
  1. **Category:** spam or ham
  2. **Message:** Mail or SMS

#### 4.2 Technology Used
**4.2.1 Machine Learning**
Machine learning, specifically logistic regression, is employed for spam email recognition due to its adaptability in handling evolving patterns.

#### 4.3 Code Implementation
**4.3.1 Libraries Used**
- NumPy
- Pandas
- scikit-learn (sklearn)
- Scipy
- Pickle
- Streamlit

#### 4.4 Implementation Steps
1. **Importing Libraries**
2. **Importing Dataset**
   - Dataset URL: [mail_data.csv](https://github.com/tejaschaudhari192/Spam-Email-Detection)
3. **Exploratory Data Analysis**
4. **Labelled Encoding**
5. **Feature Extraction**
6. **Training the Model - Logistic Regression**
7. **Evaluating the Trained Model**
8. **Building a Predictive System**
9. **Deployment of ML Model**

#### 4.5 Snapshots (Output)
After running `app.py`, the web application predicts whether an inputted message is classified as "Spam" or "Not Spam."
![image](https://github.com/tejaschaudhari192/Spam-Detection/assets/104405128/455b26f8-0f48-496a-8278-27123e5538b8)
![image](https://github.com/tejaschaudhari192/Spam-Detection/assets/104405128/e38fc665-cf27-4071-865d-cdb9fea54922)


### Conclusion
The project successfully implements a spam email detection system using machine learning, demonstrating practical application through a deployed web application.

### Bibliography
1. Kevin P. Murphy. "Machine Learning: A Probabilistic Perspective."
2. Andreas C. Miller and Sarah Guido. "Introduction to Machine Learning with Python: A Guide for Data Scientists."
3. [Dataset URL](https://raw.githubusercontent.com/tejaschaudhari192/Spam-Detection/master/dataset/mail_data.csv)
4. [Pickle Documentation](https://docs.python.org/3/library/pickle.html)
5. [Streamlit Documentation](https://docs.streamlit.io/)

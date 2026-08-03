# Blood Group Detection Using Fingerprints

A deep learning-based web application designed to predict a person's **blood group from fingerprint images**. The project combines image preprocessing, deep learning and a Django-based web interface to provide an end-to-end blood group classification workflow.

The system classifies fingerprint images into the eight major blood groups:

**A+, A-, B+, B-, AB+, AB-, O+, O-**

---

## 📌 Project Overview

Traditional blood group identification requires blood samples and laboratory testing. This project explores a machine learning-based approach for classifying blood groups using fingerprint images.

Fingerprint images are preprocessed to enhance important ridge patterns and then passed to a trained deep learning model for classification. The trained model is integrated into a Django web application where users can upload fingerprint images and obtain a predicted blood group.

> **Note:** This project is intended for educational and research purposes only and should not be used as a substitute for clinical blood-group testing.

---

## ✨ Key Features

- Fingerprint image-based blood group classification
- Classification into all 8 major blood groups
- Image preprocessing using CLAHE
- Deep learning-based image classification
- Web-based fingerprint image upload
- Automated blood group prediction
- Django-based backend
- SQLite database integration
- Simple and user-friendly web interface

---

## 🩸 Blood Groups Supported

| Blood Group | Classification |
|-------------|---------------|
| A+ | A Positive |
| A- | A Negative |
| B+ | B Positive |
| B- | B Negative |
| AB+ | AB Positive |
| AB- | AB Negative |
| O+ | O Positive |
| O- | O Negative |

---

## 🛠️ Technologies Used

### Programming & Machine Learning
- Python
- TensorFlow
- Keras
- NumPy
- OpenCV

### Image Processing
- OpenCV
- CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Pillow

### Web Development
- Django
- HTML
- CSS
- JavaScript

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 🧠 System Workflow

The application follows the following pipeline:

```text
Fingerprint Image
        ↓
Image Upload
        ↓
Image Preprocessing
        ↓
CLAHE Enhancement
        ↓
Image Resizing / Normalization
        ↓
Deep Learning Model
        ↓
Feature Extraction & Classification
        ↓
Blood Group Prediction
        ↓
Result Displayed on Web Application
```

---

## 📂 Project Structure

```text
Blood-Group-Detection-using-Fingerprints/
│
├── dataset_clahe/
│   └── dataset_clahe/
│       ├── A+/
│       ├── A-/
│       ├── AB+/
│       ├── AB-/
│       ├── B+/
│       ├── B-/
│       ├── O+/
│       └── O-/
│
├── fingerprint_ai/
│   ├── fingerprint_ai/
│   ├── predictor/
│   ├── media/
│   ├── db.sqlite3
│   └── manage.py
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📊 Dataset

The dataset contains fingerprint images organized according to their corresponding blood groups.

The eight classification categories are:

```text
A+
A-
B+
B-
AB+
AB-
O+
O-
```

The fingerprint images are processed using **CLAHE (Contrast Limited Adaptive Histogram Equalization)** to improve local contrast and enhance fingerprint ridge patterns before being used for model training.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sneha14jain/Blood-Group-Detection-using-Fingerprints-.git
```

### 2. Navigate to the Project

```bash
cd Blood-Group-Detection-using-Fingerprints-
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Navigate to the Django Application

```bash
cd fingerprint_ai
```

### 6. Run the Django Server

```bash
python manage.py runserver
```

### 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

Upload a fingerprint image through the application to generate a blood group prediction.

---

## 🔬 Model Pipeline

The overall machine learning pipeline consists of:

1. **Dataset Collection** – Fingerprint images categorized by blood group.
2. **Image Preprocessing** – Images are enhanced and prepared for training.
3. **CLAHE Enhancement** – Improves local contrast and fingerprint ridge visibility.
4. **Image Normalization** – Images are converted into a consistent format.
5. **Model Training** – A deep learning model learns patterns from the fingerprint dataset.
6. **Classification** – The model predicts one of eight blood-group classes.
7. **Web Integration** – The trained model is integrated with Django.
8. **Prediction** – Users upload fingerprint images and receive the predicted blood group.

---

## 🎯 Project Objective

The objective of this project is to explore the application of **deep learning and computer vision techniques to fingerprint image classification** and develop an end-to-end system combining:

- Data preprocessing
- Computer vision
- Deep learning
- Model inference
- Backend development
- Database management
- Web application development

---

## 🔮 Future Improvements

- Increase the size and diversity of the fingerprint dataset
- Experiment with additional CNN architectures
- Improve model generalization
- Add detailed model evaluation metrics
- Improve the web application's UI/UX
- Deploy the application to a cloud platform
- Develop an API for model inference

---

## ⚠️ Disclaimer

This project is developed for **academic, educational and research purposes only**.

Fingerprint-based blood group prediction is an experimental machine learning application and should **not be considered a medically validated method for determining blood type**. Blood groups should be confirmed using established clinical laboratory procedures before making any medical decision.

---

## 👩‍💻 Author

**Sneha Jain**

B.Tech – Computer Science and Engineering (Data Science)

Areas of Interest:
- Data Analytics
- Machine Learning
- Data Science
- Artificial Intelligence
- Web Development

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful or interesting, consider giving the repository a star.

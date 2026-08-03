import tensorflow as tf
from tensorflow.keras.preprocessing import image
import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "ml_model", "blood_group_fingerprint_model.keras")

model = tf.keras.models.load_model(model_path)

import cv2
import numpy as np

import cv2
import numpy as np

def preprocess(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    resized = cv2.resize(enhanced,(224,224))

    rgb = cv2.cvtColor(resized, cv2.COLOR_GRAY2RGB)

    img = np.expand_dims(rgb, axis=0)

    return img


def predict_blood_group(image_path):

    img = preprocess(image_path)

    pred = model.predict(img)[0]

    blood_groups = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']

    idx = np.argmax(pred)

    result = blood_groups[idx]

    confidence = round(pred[idx] * 100, 2)

    # top 3 predictions
    top3_idx = pred.argsort()[-3:][::-1]

    top3 = [(blood_groups[i], round(pred[i]*100,2)) for i in top3_idx]

    return result, confidence, top3
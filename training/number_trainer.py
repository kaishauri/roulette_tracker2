import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.preprocessing import LabelEncoder
import os

def load_data(data_dir="data/numbers"):
    images, labels = [], []
    for label in os.listdir(data_dir):
        for img_file in os.listdir(f"{data_dir}/{label}"):
            img = cv2.imread(f"{data_dir}/{label}/{img_file}")
            img = cv2.resize(img, (64, 64)) / 255.0
            images.append(img)
            labels.append(int(label))
    return np.array(images), np.array(labels)

def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
        MaxPooling2D((2,2)),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D((2,2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(37, activation='softmax')  # 0-36
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    X, y = load_data()
    model = build_model()
    model.fit(X, y, epochs=20, validation_split=0.2)
    model.save("models/number_model.h5")
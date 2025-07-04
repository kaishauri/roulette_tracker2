import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import os

def load_ball_data(data_dir="data/ball_positions"):
    images, coords = [], []
    for file in os.listdir(data_dir):
        img = cv2.imread(f"{data_dir}/{file}")
        img = cv2.resize(img, (128, 128)) / 255.0
        x, y = parse_coordinates(file)  # Extract (x,y) from filename
        images.append(img)
        coords.append([x, y])
    return np.array(images), np.array(coords)

def build_ball_model():
    model = Sequential([
        Conv2D(16, (3,3), activation='relu', input_shape=(128,128,3)),
        MaxPooling2D((2,2)),
        Conv2D(32, (3,3), activation='relu'),
        MaxPooling2D((2,2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2, activation='linear')  # Predicts (x,y)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

if __name__ == "__main__":
    X, y = load_ball_data()
    model = build_ball_model()
    model.fit(X, y, epochs=15, validation_split=0.2)
    model.save("models/ball_model.h5")
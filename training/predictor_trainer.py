import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def load_spin_data(csv_path="data/spin_history.csv"):
    df = pd.read_csv(csv_path)
    X = df[['wheel_speed', 'ball_speed', 'wheel_pos_x', 'wheel_pos_y']].values
    y = df['landing_number'].values
    return X, y

def build_predictor_model():
    model = Sequential([
        LSTM(64, input_shape=(10, 4)),  # 10 time steps, 4 features
        Dense(37, activation='softmax')  # Predicts 0-36
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    X, y = load_spin_data()
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Reshape for LSTM (samples, timesteps, features)
    X_reshaped = np.reshape(X_scaled, (-1, 10, 4))  # Assuming 10-step sequences
    
    model = build_predictor_model()
    model.fit(X_reshaped, y, epochs=30, validation_split=0.2)
    model.save("models/predictor_model.h5")
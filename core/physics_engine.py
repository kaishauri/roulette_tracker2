# Add to core/physics_engine.py
import numpy as np
from scipy import stats

class PhysicsPredictor:
    def __init__(self, wheel_diameter=0.27):  # Standard roulette wheel size
        self.wheel_diameter = wheel_diameter
        
    def calculate_angular_velocity(self, pixel_speeds, px_to_m=0.001): 
        """Convert pixel speeds to rad/s"""
        return (np.array(pixel_speeds) * px_to_m) / (self.wheel_diameter/2)
        
    def predict_using_physics(self, speeds, timestamps):
        # Add the physics calculations here
        pass
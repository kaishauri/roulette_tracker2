# Add to core/anti_detection.py
import random
import time
import pyautogui

class StealthModule:
    @staticmethod
    def random_actions():
        if random.random() < 0.01:
            pyautogui.moveRel(
                random.randint(-5,5),
                random.randint(-5,5),
                duration=0.2
            )
    
    @staticmethod
    def variable_delay():
        time.sleep(0.03 + random.random()*0.07)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Fixes core import

from core.physics_engine import PhysicsPredictor
from collections import deque
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import pyautogui
from threading import Thread
from queue import Queue
from core.anti_detection import StealthModule

class RouletteTracker:
    def __init__(self):
        self.physics = PhysicsPredictor()
        print("ტრეკერი წარმატებით ინიციალიზირდა!")

class CaptureThread(Thread):
    def __init__(self, output_queue):
        super().__init__()
        self.queue = output_queue
        
    def run(self):
        while True:
            frame = pyautogui.screenshot()
            self.queue.put(frame)

class ProcessingThread(Thread):
    def __init__(self, input_queue):
        super().__init__()
        self.queue = input_queue
        
    def run(self):
        while True:
            frame = self.queue.get()
            # Process frame here 
# while tracker:
#     StealthModule.random_actions()
#     # ... tracker logic ...
#     StealthModule.variable_delay()
class RouletteTracker:
    def __init__(self):
        self.models = self.load_models()
        self.speed_history = deque(maxlen=30)
        self.number_history = deque(maxlen=10)
        self.setup_gui()

    def load_models(self):
        # TODO: Implement model loading
        return None

    def setup_gui(self):
        """Initialize PyQt5 dashboard"""
        self.app = QApplication([])
        self.window = QMainWindow()
        self.setup_plots()
        self.setup_controls()

    # In your main application class:
    def start_threads(self):
        self.capture_queue = Queue()
        self.capture_thread = CaptureThread(self.capture_queue)
        self.processing_thread = ProcessingThread(self.capture_queue)
    
        self.capture_thread.start()
        self.processing_thread.start()
        
    def setup_plots(self):
        """Create real-time plots"""
        self.speed_plot = pg.PlotWidget(title="Speed Analysis")
        self.pred_plot = pg.PlotWidget(title="Predictions")
        
    def setup_controls(self):
        # TODO: Implement controls setup
        pass

    def run(self):
        """Main tracker loop"""
        timer = QTimer()
        timer.timeout.connect(self.update_tracker)
        timer.start(100)  # 10 FPS
        self.window.show()
        self.app.exec_()
        
    def update_tracker(self):
        """Single frame update"""
        wheel_img = self.capture(WHEEL_REGION)
        ball_img = self.capture(BALL_REGION)
        
        # Run predictions
        number = self.predict_number(wheel_img)
        ball_pos = self.predict_ball(ball_img)
        speed = self.calculate_speed(ball_pos)
        
        # Update displays
        self.update_speed_plot(speed)
        self.update_prediction_plot()

if __name__ == "__main__":
    from ui.Trackingdashboard import TrackingDashboard
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    tracker = RouletteTracker()
    dashboard = TrackingDashboard(tracker)
    dashboard.show()
    tracker.start_threads()
    app.exec_()
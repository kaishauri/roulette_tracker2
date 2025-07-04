# ui/Trackingdashboard.py
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QApplication
)
from PyQt5.QtCore import QTimer
from core.tracker import RouletteTracker

class TrackingDashboard(QMainWindow):
    def __init__(self, tracker):
        super().__init__()
        self.tracker = tracker
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Roulette Tracker")
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()
        
        self.speed_label = QLabel("Current Speed: ")
        self.pred_label = QLabel("Prediction: ")
        
        self.layout.addWidget(self.speed_label)
        self.layout.addWidget(self.pred_label)
        self.main_widget.setLayout(self.layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # 10 FPS
        self.setCentralWidget(self.main_widget)

def main():
    app = QApplication(sys.argv)
    tracker = RouletteTracker()
    dashboard = TrackingDashboard(tracker)
    
    dashboard.show()
    tracker.start_threads()
    app.exec_()

if __name__ == "__main__":
    main()
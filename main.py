# main.py (in project root)
import sys
from PyQt5.QtWidgets import QApplication
from core.tracker import RouletteTracker
from ui.Trackingdashboard import TrackingDashboard

def main():
    app = QApplication(sys.argv)
    tracker = RouletteTracker()
    dashboard = TrackingDashboard(tracker)
    
    dashboard.show()
    tracker.start_threads()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
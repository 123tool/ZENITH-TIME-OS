import threading
import time
import datetime
from utils.sound import play_alert

class AlarmScheduler:
    def __init__(self, db):
        self.db = db
        self._running = True

    def _monitor(self):
        while self._running:
            alarms = self.db.get_alarms()
            now = datetime.datetime.now().strftime("%H:%M")
            if now in alarms:
                play_alert()
                time.sleep(60)
            time.sleep(10)

    def start(self):
        threading.Thread(target=self._monitor, daemon=True).start()

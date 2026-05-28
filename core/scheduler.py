import threading, time, datetime
from utils.sound import play_alert
class AlarmScheduler:
    def __init__(self, db):
        self.db = db
    def _monitor(self):
        while True:
            if datetime.datetime.now().strftime("%H:%M") in self.db.get_alarms():
                play_alert()
                time.sleep(60)
            time.sleep(10)
    def start(self):
        threading.Thread(target=self._monitor, daemon=True).start()

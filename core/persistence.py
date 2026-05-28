import sqlite3, os
class DatabaseManager:
    def __init__(self, db_path="data/zenith.db"):
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()
    def create_tables(self):
        self.conn.executescript('''
            CREATE TABLE IF NOT EXISTS alarms (time TEXT, active INTEGER);
            CREATE TABLE IF NOT EXISTS stopwatch_logs (timestamp REAL);
            CREATE TABLE IF NOT EXISTS timer_logs (duration REAL);
        ''')
        self.conn.commit()
    def add_alarm(self, time_str):
        self.conn.execute("INSERT INTO alarms VALUES (?, 1)", (time_str,))
        self.conn.commit()
    def get_alarms(self):
        return [r[0] for r in self.conn.execute("SELECT time FROM alarms").fetchall()]
    def save_stopwatch(self, dur):
        self.conn.execute("INSERT INTO stopwatch_logs VALUES (?)", (dur,))
        self.conn.commit()

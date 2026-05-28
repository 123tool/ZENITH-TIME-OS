import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="data/zenith.db"):
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('CREATE TABLE IF NOT EXISTS alarms (time TEXT, active INTEGER)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS stopwatch_logs (timestamp REAL)')
        self.conn.commit()

    def add_alarm(self, time_str):
        self.conn.execute("INSERT INTO alarms VALUES (?, 1)", (time_str,))
        self.conn.commit()

    def get_alarms(self):
        return [r[0] for r in self.conn.execute("SELECT time FROM alarms").fetchall()]

    def save_stopwatch(self, duration):
        self.conn.execute("INSERT INTO stopwatch_logs VALUES (?)", (duration,))
        self.conn.commit()

import time
class TimeEngine:
    @staticmethod
    def format_duration(s):
        m, s = divmod(int(s), 60); h, m = divmod(m, 60)
        return f"{h:02}:{m:02}:{s:02}"

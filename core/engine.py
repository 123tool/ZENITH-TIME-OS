import time
class TimeEngine:
    @staticmethod
    def format_duration(seconds):
        mins, secs = divmod(int(seconds), 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"
    @staticmethod
    def countdown(seconds):
        while seconds >= 0:
            yield seconds
            time.sleep(1)
            seconds -= 1

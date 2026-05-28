import time
import datetime
from pynput import keyboard
from rich.live import Live
from core.renderer import Renderer
from core.persistence import DatabaseManager
from core.scheduler import AlarmScheduler
from core.engine import TimeEngine

class ZenithApp:
    def __init__(self):
        self.db = DatabaseManager()
        self.scheduler = AlarmScheduler(self.db)
        self.renderer = Renderer()
        self.mode = "MENU"
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_esc)
        self.listener.start()

    def on_esc(self, key):
        if key == keyboard.Key.esc: self.mode = "MENU"

    def run(self):
        self.scheduler.start()
        while self.running:
            if self.mode == "MENU":
                print("\n1. Clock | 2. Stopwatch | 3. Set Alarm | Q. Quit")
                choice = input("> ")
                if choice == '1': self.mode = "CLOCK"
                elif choice == '2': self.mode = "STOPWATCH"
                elif choice == '3': self.db.add_alarm(input("Time (HH:MM): "))
                elif choice.lower() == 'q': self.running = False
            
            elif self.mode == "CLOCK":
                with Live(refresh_per_second=1, screen=True) as live:
                    while self.mode == "CLOCK":
                        now = datetime.datetime.now().strftime("%H:%M:%S")
                        live.update(self.renderer.render_display(pyfiglet.figlet_format(now), "CLOCK"))
                        time.sleep(1)

            elif self.mode == "STOPWATCH":
                start = time.time()
                with Live(refresh_per_second=10, screen=True) as live:
                    while self.mode == "STOPWATCH":
                        elapsed = time.time() - start
                        live.update(self.renderer.render_display(TimeEngine.format_duration(elapsed), "STOPWATCH"))
                        time.sleep(0.1)
                self.db.save_stopwatch(time.time() - start)

if __name__ == "__main__":
    ZenithApp().run()

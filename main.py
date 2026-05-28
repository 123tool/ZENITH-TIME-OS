import time, datetime, pyfiglet, os, platform
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
        keyboard.Listener(on_press=self.on_esc).start()

    def on_esc(self, key):
        if key == keyboard.Key.esc: self.mode = "MENU"

    def run(self):
        self.scheduler.start()
        while self.running:
            os.system('cls' if platform.system() == "Windows" else 'clear')
            if self.mode == "MENU":
                print(f"=== ZENITH-TIME-OS | OS: {platform.system()} ===")
                print("1. Clock | 2. Stopwatch | 3. Timer | 4. Alarm | Q. Quit")
                c = input("> ")
                if c == '1': self.mode = "CLOCK"
                elif c == '2': self.mode = "STOPWATCH"
                elif c == '3': self.mode = "TIMER"
                elif c == '4': self.db.add_alarm(input("HH:MM: "))
                elif c.lower() == 'q': self.running = False
            
            if self.mode != "MENU":
                with Live(refresh_per_second=10, screen=True) as live:
                    while self.mode != "MENU":
                        if self.mode == "CLOCK":
                            data = pyfiglet.figlet_format(datetime.datetime.now().strftime("%H:%M:%S"))
                        elif self.mode == "STOPWATCH":
                            data = TimeEngine.format_duration(time.time() - self.start_t) if hasattr(self, 'start_t') else "00:00:00"
                        
                        live.update(self.renderer.render_display(data, self.mode))
                        if self.mode == "STOPWATCH" and not hasattr(self, 'start_t'): self.start_t = time.time()
                        time.sleep(0.5)
                    if hasattr(self, 'start_t'): del self.start_t

if __name__ == "__main__":
    ZenithApp().run()

import time, datetime, pyfiglet, os, platform, sys, select, tty, termios
from rich.live import Live
from core.renderer import Renderer
from core.persistence import DatabaseManager
from core.scheduler import AlarmScheduler
from core.engine import TimeEngine
from utils.helpers import clear_screen

class ZenithApp:
    def __init__(self):
        self.db = DatabaseManager()
        self.scheduler = AlarmScheduler(self.db)
        self.renderer = Renderer()
        self.mode = "MENU"
        self.running = True

    def is_esc_pressed(self):
        # Mengecek apakah user menekan tombol (non-blocking)
        if select.select([sys.stdin], [], [], 0)[0]:
            char = sys.stdin.read(1)
            if char == '\x1b': return True # \x1b adalah kode ASCII untuk ESC
        return False

    def run(self):
        self.scheduler.start()
        # Set terminal ke mode raw agar bisa deteksi input instan
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        
        try:
            while self.running:
                if self.mode == "MENU":
                    clear_screen()
                    print("=== ZENITH-TIME-OS (TERMINAL) ===")
                    print("1. Clock\n2. Stopwatch\n3. Add Alarm\nQ. Quit")
                    # Untuk menu, kita pakai input biasa
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
                    choice = input("> ")
                    tty.setcbreak(sys.stdin.fileno())
                    
                    if choice == '1': self.mode = "CLOCK"
                    elif choice == '2': self.mode = "STOPWATCH"
                    elif choice == '3': self.db.add_alarm(input("HH:MM: "))
                    elif choice.lower() == 'q': self.running = False
                
                if self.mode != "MENU":
                    with Live(refresh_per_second=5, screen=True) as live:
                        while self.mode != "MENU":
                            if self.is_esc_pressed(): self.mode = "MENU"; break
                            
                            if self.mode == "CLOCK":
                                data = pyfiglet.figlet_format(datetime.datetime.now().strftime("%H:%M:%S"))
                            elif self.mode == "STOPWATCH":
                                if not hasattr(self, 'start_t'): self.start_t = time.time()
                                data = TimeEngine.format_duration(time.time() - self.start_t)
                            
                            live.update(self.renderer.render_display(data, self.mode))
                            time.sleep(0.5)
                        if hasattr(self, 'start_t'): del self.start_t
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    ZenithApp().run()

import os
import platform

def play_alert():
    """Trigger alarm sound based on OS."""
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 2000) # 1000Hz, 2000ms
        elif system == "Darwin": # macOS
            os.system('afplay /System/Library/Sounds/Glass.aiff')
        else: # Linux
            print('\a') # Terminal bell character
    except Exception:
        print("\n[!] ALARM TRIGGERED: Please check your audio settings.")

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_app():
    print("\n[!] Shutting down ZENITH-TIME-OS...")
    sys.exit(0)

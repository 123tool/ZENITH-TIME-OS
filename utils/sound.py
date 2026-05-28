import platform, os
def play_alert():
    system = platform.system()
    if system == "Windows":
        import winsound; winsound.Beep(1000, 2000)
    elif system == "Darwin": # Mac
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    else: # Linux/Termux
        print('\a', end='', flush=True)

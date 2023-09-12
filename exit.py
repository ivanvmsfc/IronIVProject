import keyboard
import os
import signal


# Get PID of background process
pid = os.getpid()

# Define signal handler
def signal_handler(signum, frame):
    print("Stopping background process...")
    os.kill(pid, signal.SIGTERM)

# Register spacebar hotkey
keyboard.add_hotkey("F10", lambda: os.kill(pid, signal.SIGTERM))

# Set SIGTERM handler
signal.signal(signal.SIGTERM, signal_handler)
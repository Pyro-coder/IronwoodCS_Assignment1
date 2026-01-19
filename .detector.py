# .detector.py
import time
import os
import subprocess

# The file to watch
FILE_TO_WATCH = "main.py"
LAST_MODIFIED = 0

# We silence the print statement so it doesn't show up in the terminal
# print(f"👀 Monitoring {FILE_TO_WATCH}...") 

while True:
    try:
        current_mtime = os.path.getmtime(FILE_TO_WATCH)
        if current_mtime != LAST_MODIFIED:
            LAST_MODIFIED = current_mtime
            # Force a git commit silently
            subprocess.run(["git", "add", FILE_TO_WATCH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "commit", "-m", f"Auto-save: {time.ctime()}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass
    time.sleep(10) # Checks every 10 seconds

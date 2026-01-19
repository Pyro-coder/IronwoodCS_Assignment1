# .devcontainer/.detector.py
import time
import os
import subprocess

# 1. Calculate the absolute path to the workspace root
# This grabs the folder where THIS script lives (.devcontainer)
script_location = os.path.dirname(os.path.abspath(__file__))
# This goes up one level to the root folder (CS101-Assignment...)
workspace_root = os.path.dirname(script_location)

# 2. Target the file reliably
file_path = os.path.join(workspace_root, "main.py")
last_modified = 0

# 3. Ensure we run Git commands from the root directory
os.chdir(workspace_root)

while True:
    try:
        # Check if file exists to avoid crashing on start
        if os.path.exists(file_path):
            current_mtime = os.path.getmtime(file_path)
            
            # Initial setup: don't commit immediately on boot
            if last_modified == 0:
                last_modified = current_mtime
            
            elif current_mtime != last_modified:
                last_modified = current_mtime
                
                # Force Git commands
                subprocess.run(["git", "add", "main.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["git", "commit", "-m", f"Snapshot: {time.ctime()}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                # Note: 'git push' might fail if auth isn't cached yet, but commit will succeed
                subprocess.run(["git", "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
    except Exception:
        pass
        
    time.sleep(10)

# .devcontainer/.detector.py
import time
import os
import subprocess
import sys

# Force output to appear in the log immediately
def log(msg):
    print(f"[Detector] {msg}", flush=True)

try:
    # 1. Locate the workspace
    script_location = os.path.dirname(os.path.abspath(__file__))
    # Go up one level from .devcontainer to root
    workspace_root = os.path.dirname(script_location)
    
    log(f"Started. Script is at: {script_location}")
    log(f"Workspace root is: {workspace_root}")

    # 2. Target the file
    file_path = os.path.join(workspace_root, "main.py")
    log(f"Targeting file: {file_path}")

    # 3. Change directory so git commands work
    os.chdir(workspace_root)
    log(f"Changed working directory to: {os.getcwd()}")

    last_modified = 0

    while True:
        if os.path.exists(file_path):
            current_mtime = os.path.getmtime(file_path)
            
            if last_modified == 0:
                last_modified = current_mtime
                log("Initial timestamp set. Waiting for changes...")
            
            elif current_mtime != last_modified:
                last_modified = current_mtime
                log("Change detected! Committing...")
                
                # Run Git commands and CAPTURE errors
                try:
                    subprocess.run(["git", "add", "main.py"], check=True)
                    subprocess.run(["git", "commit", "-m", f"Snapshot: {time.ctime()}"], check=True)
                    log("Commit successful.")
                    
                    # Push separately (this is the most likely failure point)
                    subprocess.run(["git", "push"], check=True)
                    log("Push successful.")
                except subprocess.CalledProcessError as e:
                    log(f"Git Error: {e}")
        else:
            log("Waiting... main.py not found yet.")
            
        time.sleep(10)

except Exception as e:
    log(f"FATAL ERROR: {e}")

import tkinter as tk
import subprocess
import os
import time

def launch_exe():
    # Wait for 30 seconds
    time.sleep(15)
    
    # Replace 'your_exe_file.exe' with the actual path to your .exe file
    exe_path = "Spike.exe"
    print(exe_path)
    
    try:
        # Launch the .exe file using subprocess
        subprocess.Popen(exe_path, shell=True)
    except Exception as e:
        print(f"Error launching the .exe file: {e}")

# Create the main window
root = tk.Tk()
root.title("Spike Launcher")

# Create a label
label = tk.Label(root, text="Click 'Relaunch' to launch the .exe file after 30 seconds.")
label.pack(pady=10)

# Create a button to trigger the .exe launch
relaunch_button = tk.Button(root, text="Relaunch", command=launch_exe)
relaunch_button.pack()

# Start the main loop
root.mainloop()

Screen Recorder Application

A simple Python-based screen recorder that captures your screen activity and saves it as a video file. Designed with an intuitive GUI for ease of use.

Features
Start and Stop Recording: Initiate or end a recording session with GUI buttons or keyboard shortcuts.
Keyboard Shortcuts:
Press Shift + R to start recording.
Press Shift + S to stop recording.
Automatic File Naming: Saves recordings with a timestamped filename in the Desktop folder.
Customizable GUI: A responsive interface that moves to the bottom-left corner during recording.
Real-time Feedback: Visual and message-based confirmation of actions.
Cross-Platform Compatibility: Works on Windows, macOS, and Linux.

Installation

Requirements
Python 3.6 or higher
Required Python libraries:
numpy
pyautogui
opencv-python
keyboard
tkinter (built-in with Python)

Setup
Clone or download the repository.
Install the dependencies:
bash
Copy code
pip install numpy pyautogui opencv-python keyboard
Run the screen_recorder.py script:
bash
Copy code
python screen_recorder.py

Usage
Launch the application.
Use the Start Recording button or Shift + R to begin capturing your screen.
Use the Stop Recording button or Shift + S to stop and save the recording.
Files are saved automatically to your Desktop with names like recordingOutput_YYYY-MM-DD_HH-MM-SS.avi.

File Output
Videos are saved in AVI format with a frame rate of 15 FPS and resolution matching your screen size.

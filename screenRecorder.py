import numpy as np
import pyautogui
import cv2
import time
import keyboard
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import threading  

# global variables to control recording
isRecording = False
videoOutput = None
original_geometry = None  # to store original window position

# setting up window
root = tk.Tk()
root.title("Screen Recorder")
root.geometry("400x200")
root.config(bg='black')


def newFileName():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")  
    filename = os.path.join(desktopPath, f"recordingOutput_{timestamp}.avi")
    print(f"Saving file as: {filename}")
    return filename


def setUpVideoWriter():
    global videoOutput
    fps = 15.0
    screenshot = pyautogui.screenshot()
    frameSize = (screenshot.width, screenshot.height)
    
    # Video setup
    fourCharcode = cv2.VideoWriter_fourcc(*'XVID')
    videoOutput = cv2.VideoWriter(newFileName(), fourCharcode, fps, frameSize)

    if not videoOutput.isOpened():
        messagebox.showerror("Error", "Failed to initialize video writer. Recording will not be saved.")


def recordScreen():
    global isRecording
    fps = 15.0  
    frameDuration = 1 / fps  
    
    while isRecording:
        startTime = time.time()
        screenshot = pyautogui.screenshot()
        screenshotArray = np.array(screenshot)
        frameInBGR = cv2.cvtColor(screenshotArray, cv2.COLOR_RGB2BGR)
        
        if videoOutput:
            videoOutput.write(frameInBGR)

        endTime = time.time()
        timeTaken = endTime - startTime
        timeToSleep = frameDuration - timeTaken
        if timeToSleep > 0:
            time.sleep(timeToSleep)


def moveWindowToBottomLeft():
    """Move the root window to the bottom-left corner of the screen."""
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = 200
    windowHeight = 50
    x = 0  
    y = screenHeight - windowHeight - 100 
    root.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
    root.update_idletasks()


def startRecording():
    global isRecording, original_geometry
    if not isRecording:
        isRecording = True
        original_geometry = root.geometry()
        moveWindowToBottomLeft()
        setUpVideoWriter()
        updateGUIForRecording()
        threading.Thread(target=recordScreen, daemon=True).start()


def stopRecording():
    global isRecording, original_geometry
    if isRecording:
        isRecording = False
        if videoOutput:
            videoOutput.release()
        
        updateGUIForIdle()
        if original_geometry:
            root.geometry(original_geometry)
        messagebox.showinfo("Info", "Recording Stopped and Saved!")


def updateGUIForRecording():
    root.update_idletasks()
    startButton.pack_forget()
    guideButton.pack_forget()
    stopButton.pack(fill='both', expand=True)
    closeButton.pack_forget()
    root.attributes('-topmost', True)


def updateGUIForIdle():
    stopButton.pack_forget()
    startButton.pack(pady=10)
    guideButton.pack(pady=10)
    closeButton.pack(pady=10)


def showGuide():
    messagebox.showinfo("Guide", "Press Shift+R to start recording.\nPress Shift+S to stop recording.")
    
def closeApp():
    if isRecording:
        stopRecording()
    root.destroy()

# Hover functions to change the button background color on hover
def onStartEnter(event):
    event.widget.config(bg='lightblue')

def onGuideCloseEnter(event):
    event.widget.config(bg='lightgray')

def onLeave(event):
    if event.widget == startButton:
        event.widget.config(bg='green')
    elif event.widget == stopButton:
        event.widget.config(bg='red')    
    else:
        event.widget.config(bg='gray')


startButton = tk.Button(root, text="Start Recording", command=startRecording, font=('Helvetica', 12), bg='green', fg='black')
startButton.pack(pady=10)
startButton.bind("<Enter>", onStartEnter)
startButton.bind("<Leave>", onLeave)

guideButton = tk.Button(root, text='Guide', command=showGuide, font=('Helvetica', 12), bg='gray', fg='black')
guideButton.pack(pady=10)
guideButton.bind("<Enter>", onGuideCloseEnter)
guideButton.bind("<Leave>", onLeave)

stopButton = tk.Button(root, text="Stop Recording", command=stopRecording, font=('Helvetica', 12), bg='red', fg='black')
stopButton.bind("<Enter>", onStartEnter)
stopButton.bind("<Leave>", onLeave)

closeButton = tk.Button(root, text="Close", command=closeApp, font=('Helvetica', 12), bg='gray', fg='black')
closeButton.pack(pady=10)
closeButton.bind("<Enter>", onGuideCloseEnter)
closeButton.bind("<Leave>", onLeave)


def main():
    root.update()
    keyboard.add_hotkey('shift+r', startRecording)
    keyboard.add_hotkey('shift+s', stopRecording)
    root.mainloop()


main()

import sounddevice as sd
import numpy as np
import os
import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

duration = 1 
threshold = 0.3  
max_interval = 3  
clap_count_target = 3

clap_timestamps = []

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_app(app_name):
    if app_name == "chrome":
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Opening Chrome")
    else:
        speak("Command not recognized")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except:
            return ""

def execute_command(cmd):
    if "chrome" in cmd:
        open_app("chrome")
    elif "quit" in cmd or "exit" in cmd:
        speak("Goodbye!")
        exit()
    else:
        speak("Command not recognized")

while True:
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()
    volume_norm = np.linalg.norm(audio) * 10
    print("Volume:", volume_norm)
    
    current_time = time.time()
    
    
    clap_timestamps = [t for t in clap_timestamps if current_time - t < max_interval]
    
    if volume_norm > threshold:
        clap_timestamps.append(current_time)
        print(f"Claps detected: {len(clap_timestamps)}")
        
        if len(clap_timestamps) == clap_count_target:
            print("3 claps detected! Waking up...")
            open_app("chrome")
            clap_timestamps.clear()
    
    
    if len(clap_timestamps) == 0:
        command = listen()
        if command:
            execute_command(command)

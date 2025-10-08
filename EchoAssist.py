import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Network error")
            return ""

def execute_command(cmd):
    if "chrome" in cmd:
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        speak("Opening Chrome")
    elif "vs code" in cmd:
        os.startfile(r"C:\Users\vinay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
        speak("Opening Visual Studio Code")
    elif "quit" in cmd or "exit" in cmd:
        speak("Goodbye!")
        exit()
    else:
        speak("Command not recognized")

while True:
    command = listen()
    if command:
        execute_command(command)
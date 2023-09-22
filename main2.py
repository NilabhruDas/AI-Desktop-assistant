import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import numpy as np

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        audio = r.listen(source)  # Listen to audio from the microphone
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Sorry, I could not understand your request.")
        return ""

if __name__ == '__main__':
    print('Jarvis')
    engine = pyttsx3.init()
    engine.say('Hello, I am Jarvis.')
    engine.runAndWait()
    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["instagram", "https://www.instagram.com"]]
        for site in sites:
            if "hello" in query:
                engine.say("Hello! How can I assist you today?")
                engine.runAndWait()
            if f"Open {site[0]}".lower() in query.lower():
                engine.say(f'Opening {site[0]} sir')
                engine.runAndWait()
                webbrowser.open(site[1])
            if "play music" in query:
                musicPath = "D:/d drive files/think imp/ac.mp3"# not use this '\'  
                os.startfile(musicPath)
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%I:%M %p") # this is for 12 hour format
                engine.say(f'sir, the time is {strfTime}')
                engine.runAndWait()
                break
            # if "open torrent".lower() in query.lower():
                # os.system("C:/Users/Nilabhru Das/AppData/Roaming/uTorrent/uTorrent.exe")
            if "good bye" in query:
                engine.say("Goodbye! Have a great day.")
                engine.runAndWait()
                exit()
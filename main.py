import pyttsx3
import speech_recognition as sr
import os
import requests
import json
import webbrowser
import datetime

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

weatherurl = #add your api key
newsurl = #add your api key

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
                break
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
            if "weather" in query:
                r = requests.get(weatherurl)
                wdic = json.loads(r.text)
                t = (wdic["current"]["temp_c"])
                c = (wdic["current"]["condition"]["text"])
                h = (wdic["current"]["humidity"])
                msge = (f'The current weather in kolkata is {t} degree and humidity level is {h} percent with {c}')
                engine.say(msge)
                engine.runAndWait()
                break
            if "news" in query:
                r = requests.get(newsurl)
                ndic = json.loads(r.text)
                articles = ndic.get("articles", [])[:3]  # Get the first 3 news articles (if available)
                if articles:
                    engine.say("Here are the top three news headlines:")
                    engine.runAndWait()
                    for index, article in enumerate(articles, 1):
                        title = article.get("title", "")
                        description = article.get("description", "")
                        if title and description:
                            news_msg = f"News {index}: {title}. {description}."
                            engine.say(news_msg)
                            engine.runAndWait()
                        elif title:
                            news_msg = f"News {index}: {title}."
                            engine.say(news_msg)
                            engine.runAndWait()
                else:
                    engine.say("I couldn't fetch the news headlines at the moment. Please try again later.")
                    engine.runAndWait()
                break
            if "good bye" in query:
                engine.say("Goodbye! Have a great day.")
                engine.runAndWait()
                exit()

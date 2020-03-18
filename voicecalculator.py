import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am you Calculator Assistant")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listinging....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")    

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query   


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if '+' in query:
            num1=query.split(" + ")
            num2=int(num1[0])+int(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")
        
        elif '-' in query:
            num1=query.split(" - ")
            num2=int(num1[0])-int(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")

        elif ' / ' in query:
            num1=query.split("/")
            num2=float(num1[0])/float(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")

        elif '/' in query:
            num1=query.split("/")
            num2=float(num1[0])/float(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")
        
        elif 'divided by' in query:
            num1=query.split(" divided by ")
            num2=float(num1[0])/float(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")

        elif 'x' in query:
            num1=query.split(" x ")
            num2=float(num1[0])*float(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")
        elif 'into' in query:
            num1=query.split(" into ")
            num2=float(num1[0])*float(num1[1])
            print(f"answer is {num2}")
            speak(f"answer is {num2}")           

        elif 'exit' in query:
            exit(0)            
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from tkinter import *
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")

#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")

#     else:
#         speak("Good Evening!")
#     speak("I am you Calculator Assistant")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        label2.configure(text="Listinging....")
        print("Listinging.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize.....")
        label2.configure(text="Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 
        label2.configure(text=f"User said: {query}\n")   

    except Exception as e:
        print(e)
        label2.configure(text="Say that again please...")
        print("Say that again please...")
        return "None"
    return query   


def myThread2(num2):
    t2=threading.Thread(target=lambda : label3.configure(text=f"answer is {num2}"))
    t2.start()



def processCommand():
    query = takeCommand().lower()

    if '+' in query:
        num1=query.split(" + ")
        num2=int(num1[0])+int(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")

    elif '-' in query:
        num1=query.split(" - ")
        num2=int(num1[0])-int(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")

    elif ' / ' in query:
        num1=query.split("/")
        num2=float(num1[0])/float(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")

    elif '/' in query:
        num1=query.split("/")
        num2=float(num1[0])/float(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")

    elif 'divided by' in query:
        num1=query.split(" divided by ")
        num2=float(num1[0])/float(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")    

    elif 'x' in query:
        num1=query.split(" x ")
        num2=float(num1[0])*float(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")
        
    elif 'into' in query:
        num1=query.split(" into ")
        num2=float(num1[0])*float(num1[1])
        # print(f"answer is {num2}")
        myThread2(num2)
        speak(f"answer is {num2}")          
            
    elif 'exit' in query:
        exit(0)
    else:
        label2.configure(text="invalid command")      

def myThread():
    t1=threading.Thread(target=processCommand)
    t1.start()
frame=Tk()
frame.title("Calculator Assistant")
p1=PanedWindow(frame)
p2=PanedWindow(p1,orient=VERTICAL)
photo = PhotoImage(file = r"images.png")
photo1=PhotoImage(file=r"download.png")
label1=Label(p1,text="mywindow",bg="orange",image=photo)
label2=Label(p2,text="Tap listen to activate",bg="red",fg="white",height=2)
label3=Label(p2,text="Answer here",height=2,bg="green",fg="white")


p1.pack(fill=BOTH,expand=1)
p1.add(label1)
p1.add(p2)

    # e1 = Entry(p2)  
p2.add(label2)
p2.add(label3) 
btn1=Button(p2,text="Listen",image=photo1,height=3,width=3,command=myThread) 
p2.add(btn1)
                         
mainloop()   
              

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell How may I help you.")

def takeCommand():
        #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vidhikhobragade466@gmail.com', 'tyqrnaamdncekoze')
    server.sendmail('vidhikhobragade466@gmail.com, to, content')
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
     
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            strfTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Madam, the time is {strfTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        elif 'send email to Vidhi':
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vidhikhobragade466@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend..I am not able to send this email.")
        

        
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To covert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 3
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


#To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak(" Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am DOC Sir, Please tell me how can I help you")
    print("I am Doc Sir, Please tell me how can I help you")

#to send email
def sendEmail(to, content):
    print("Sending Email to", to)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gopiazad36@gmail.com', 'Gopibhai@900')
    print("Logged in successfully")
    server.sendmail('gopiazad12338@gmail.com', to, content)
    print("Email sent successfully")
    server.close()



if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open Command Prompt" in query or "open cmd" in query:
            os.system("start cmd")

        elif "open chrome" in query or "open chrome browser" in query:
            cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        # elif "Play Music" in query:
        #     music_dir = "D:\\my folder\\Music"
        #     song = os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, song[1]))
        elif "play music" in query or "open music" in query or "music" in query or "songs" in query:
            music_dir = "D:\\my folder\Music\\my music\\new"
            songs = os.listdir(music_dir)
            song = random.choice(songs) # If you wanna play random song then you can use this
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
                    break
        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(f"Your IP address is :",ip)

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            print("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 10)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening Youtube...")
            print('Opening youtube...')

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            speak("Opening facebook...")
            print('Opening facebook...')

        elif "open linkedin" in query or "Linkedin" in query:
            webbrowser.open("https://www.linkedin.com/feed/")
            speak("Opening linkedin...")
            print('Opening linkedin...')

        elif "open github" in query or "github" in query or " open git" in query or "hub" in query:
            webbrowser.open("https://github.com/")
            speak("Opening github...")
            print('Opening github...')

        elif "Send a Message" in query or "send message" in query:
            kit.sendwhatmsg(f"+918950007178", "Hello Doctor, I,m Jarvis, Gopi's assistant ", 12, 14)

        elif "open stackoverflow" in query or "Stack overflow" in query or "slow" in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("Opening stackoverflow...")
            print('Opening stackoverflow...')

        elif "open Google" in query:
            webbrowser.open("https://www.google.com/")
            speak("Sir, What should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        # elif "play video on YouTube" in query:
        #    kit.playonyt("see you again")

        elif "play video on youtube" in query:
            speak("Which video should I play on YouTube?")
            video = takecommand().lower()
            kit.playonyt(video)

        elif "email to Gopi" in query:
            try:
                speak("what should I say?")
                content = takecommand().lower()
                to = "gopiazad12338@gmail.com"
                sendEmail(to, content)
                speak("Email has been send successfully")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I'm not able to send this email to Gopi")

        elif "no thanks " in query:
            speak("Thanks for using me Sir, Have a Good day")
            sys.exit()
        speak("Do you have any other work")


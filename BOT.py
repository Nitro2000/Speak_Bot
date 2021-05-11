import pyttsx3  # Text to speak
import speech_recognition as sr # Speak to string(text)
from datetime import datetime  # For correct time and date
import wikipedia  # For search
import webbrowser  # For opening sites
import os  # For opnening inbuild platforms
import smtplib  # For mail (stands for simple mail transfer protocol library)
import time

ST = pyttsx3.init('sapi5')
voices = ST.getProperty('voices')
ST.setProperty('voice', voices[0].id)

def speak(audio):  # Func for text to speak 
    ST.say(audio)
    ST.runAndWait()

def Wish():  # Func for wishing the owner
    hr = int(datetime.now().hour)  # datetime return a string in 24 hr format
    if 6 <= hr < 12:
        speak("good morning! sir")  # no need for capital letters. it will speak same
    elif 12 <= hr < 16:
        speak("good afternoon! sir")
    elif 16 <= hr < 20:
        speak("good evening! sir")
    else:
        speak("good night! sir")
    speak("i am speak bot. please tell me how can i help you")

def takecommand():  # Func for speech to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 2  # for a pause 
        audio = r.listen(source)
    try:
        print("I am recognizing....")
        query = r.recognize_google(audio, language = "en - IN")  # To recognise your language usig google
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please......")
        return takecommand()
    else:
        return query

def sendmail(to, content):  # Func for sending mails
    server = smtplib.SMTP("smtp.gmail.com", 587)  # this is default smpt site and port
    server.starttls()
    server.login("rishabhyo456@gmail.com", "Rishi@654")
    server.sendmail("rishabhyo456@gmail.com", to, content)
    
if __name__ == "__main__":
    Wish()
    while True:
        a = takecommand().lower()
        if "wikipedia" in a:
            speak("Searching wikipedia")
            a = a.replace("wikipedia", "")
            result = wikipedia.summary(a, sentences = 4)
            speak("according to wikipedia")
            print("result")
            speak("result")
        elif "open youtube" in a:
            webbrowser.open("youtube.com")
            time.sleep(5)
        elif "open google" in a:
            webbrowser.open("google.com")
            time.sleep(5)
        elif "open stack overflow" in a:
            webbrowser.open("stackoveflow.com")
        elif "open data science guide" in a:
            webbrowser.open("datasciguide.com")
        elif "open insta" in a:
            webbrowser.open("instagram.com")
            time.sleep(5)
        elif "the time" in a:
            time = datetime.now().hour
            if 0 <= time < 12:
                time = datetime.now().strftime("%I:%M:%S")
                speak(f"sir, the time is {time} A M")
                print(time,"AM")
            else:
                time = datetime.now().strftime("%I:%M:%S")
                speak(f"sir, the time is {time} P M")
                print(time,"PM")
        elif "the day" in a:
            day = datetime.now().strftime("%A")
            speak(f"sir, today is {day}")
        elif "the month" in a:
            month = datetime.now().strftime("%B")
            speak(f"sir, it's {month}")
        elif "the date" in a:
            date = datetime.now().date()
            speak(f"sir, the date is {date}")
        elif "google search" in a:
            speak("what do you want to search on google")
            c = takecommand()
            try:
                from googlesearch import search
            except ImportError:
                print("no module named 'google' found")
            else:
                for i in search(c, tld= "co.in", num=10, stop=10, pause=2):
                    print(i)
                speak("following websites are the results based on your search")
        elif "open notepad" in a:
            print("opening notepad..")
            os.system("notepad.exe")
        elif "send mail" in a or "send a mail" in a:
            speak("please speak the email content")
            content = takecommand()
            speak("now tell me the receiver email account")
            to = takecommand()
            to = to.replace(" ", "")
            sendmail(to, content)
            speak("email has been sent!")
        elif "quit" in a:
            speak("it was nice talking to you sir. see you soon again")
            break
        elif "your specification" in a:
            speak("i have 8 g b ram 256 s s d with intel core i 5 8th generation") 
    exit()
                    
                    































    

import pyttsx3
import datetime

import speech_recognition as sr
import os 
import wikipedia
import smtplib
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import webbrowser 

# driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application")

webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
engine  =  pyttsx3.init('sapi5')

voices  = engine.getProperty('voices')


# print(voices[1].id)

engine.setProperty('voice',voices[1].id)


def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def wishME():

    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour<12:

        speak("HELLO SIR GOOD MORNING")

    elif hour >= 12 and hour<18:

        speak("HELLO SIR GOOD AFTERNOON")

    else:

        speak("HELLO SIR GOOD EVENING")

    speak(" MY NAME IS ALICE HOW MAY I HELP YOU ")

def takecommand():

    r =sr.Recognizer()

    # print(sr.Microphone.list_microphone_names())

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source,duration=1)

        # r.energy_threshold()

        print(f"At Your Command Sir : ")

        audio= r.listen(source)

        try:

            query = r.recognize_google(audio)

            print(f'Did you said:{query}\n ')

        except:

            print("Sorry, Could Not Recognise")

            return "None"

        return query
def sendEmail(to,content):
    server =  smptlib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("mufasakxnx@gmail.com","iboo@123")
    server.sendmail("mufasakxnx@gmail.com",to,content)
    server.close()
if __name__ == "__main__":

    wishME()

    while True:
        
        query = takecommand().lower()

        if 'wikipedia' in query:

            speak("Searching wikipedia...")

            query = query.replace('wikipedia','')

            result = wikipedia.summary(query,sentences = 2)

            speak("According to Wikipedia")

            print(result)

            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youTube.com")
            # driver.get("youTube.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open pi code' in query:
            pycod = r'C:\Users\SONY\Desktop\pycodes'
            ptt = os.listdir(pycod)
            # print(ptt)
            os.startfile(pycod)
        elif "how are you" in query:
            speak("I m Fine sir What about you")

        elif "the time" in query:
            srtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(srtime)
            speak(f'The time is {srtime}')
        elif 'open my project' in query:
            code = r"C:\Users\SONY\AppData\Local\JetBrains\PyCharm Community Edition 2021.1\bin\pycharm64.exe"
            os.startfile(code)
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif "send a mail" in query:
            re =sr.Recognizer()
            speak("To WHOM You want to send mail")
            with sr.Microphone() as source:
                re.adjust_for_ambient_noise(source,duration=1)
                audio= re.listen(source)
                speek =  re.recognize_google(audio,language = 'en-in')
                print("Did you said",speek)
                speak(f"Did you said {speek}")
                try:
                    speak("what should i say")
                    content = takecommand()
                    to = speek+'@gmail.com'
                    print(to)
                    sendEmail(to,content)
                    speak("Email has been sent")
            
                except:
                    print("Sorry Could Not Recognize")

        elif "gmail.com" in query:
            webbrowser.open("gmail.com")   

        elif "quit" in query:
            exit(0)
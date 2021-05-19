import pyttsx3
import datetime
import speech_recognition as sr




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
    speak(" MY NAME IS FRIDAY HOW MAY I HELP YOU ")
def takeCommand():
    #it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I M HEARING YOU SIR ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("RECOGNIZING.....")
        query = r.recognize_google(audio,language = 'en-in')
        print(f'USER SAID :{query}\n')
    except Exception as e:


        print("Say that again please")
        return "None"
    return query
if __name__ == "__main__":
    # wishME()
    takeCommand()
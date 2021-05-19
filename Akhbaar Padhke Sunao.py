import requests
import json

w = requests.get("http://newsapi.org/v2/everything?q=tesla&from=2021-02-13&sortBy=publishedAt&apiKey=064b8990db9d44159ea342c20b7f6f74")
wl = w.text
wl_jason = json.loads(wl)

s =  requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=064b8990db9d44159ea342c20b7f6f74")
sc = s.text
sc_jason = json.loads(sc)


tech = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=064b8990db9d44159ea342c20b7f6f74")
t = tech.text
t_jason = json.loads(t)

ent = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=064b8990db9d44159ea342c20b7f6f74")
e =ent.text
e_jason = json.loads(e)
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ =="__main__":
    ibrahim = input("ENTER THE NEWS YOU WANT TO HEAR\n").upper()
    if ibrahim =="WORLD":
        for i in range(0,11):
            speak(wl_jason['articles'][i]['title'])

    elif ibrahim =="BITCOIN":
        for i in range(0,11):
            speak(sc_jason['articles'][i]['title'])

    elif ibrahim =="TECH":
        for i in range(0,11):
            speak(t_jason['articles'][i]['title'])

    elif ibrahim =="ENT":
        for i in range(0,11):
            speak(e_jason['articles'][i]['title'])
            
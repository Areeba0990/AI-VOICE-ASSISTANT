import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import os


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good morning")
        speak("good morning")

    elif hour>=12 and hour<18:
        print("good afternoon")
        speak("good afternoon")

    else:
        print("good evening")
        speak("good evening")


    message = "hello I am voice assistant. how can i help you?"
    print(message)
    speak(message)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("recognizing...")
        query =  r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please..")
        return "none"
    return query


if __name__ == '__main__':
    wishme()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('searching wikipedia')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)


       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'play music' in query:
           speak('playing your music')
           print('playing your music')
           music = "C:\\Users\\PMYLS\\Desktop\\AI VOICE ASSISTANT\\myai\\music"
           songs = os.listdir(music)
           print(songs)
           os.startfile(os.path.join(music,songs[0]))

       elif 'the time' in query:
           strtime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strtime)
           speak(f"the time is {strtime}")

       elif 'open code' in query:
           path = "C:\\Users\\PMYLS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
           os.startfile(path)

       elif 'terminate' in query:
            speak("Terminating the program. Goodbye!")
            print("Terminating the program. Goodbye!")
            break

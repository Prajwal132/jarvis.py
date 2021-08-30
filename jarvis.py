import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    else:
        speak("Welcome Back sir!")
        speak("How may I help you sir!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'E:\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'open code ' in query:
            codePath = 'A:\\vs code\\Microsoft vs code\\Code.exe'
            os.startfile(codePath)

        elif 'open hotstar' in query:
            webbrowser.open("https:\\www.hotstar.com")

        elif 'open gmail' in query:
            webbrowser.open("https:\\mail.google.com/mail/u/0/#inbox")

        elif 'open classroom' in query:
            webbrowser.open("https:\\classroom.google.com/u/1/h")

        elif 'open black' in query:
            webbrowser.open("https:\\www.youtube.com/watch?v=EzKkl64rRbM")

        elif 'open match' in query:
            webbrowser.open("https:\\www.hotstar.com/in/sports/cricket/indian-premier-league/mumbai-indians-vs-royal-challengers-bangalore-m702890/match-clips/highlights-rcb-pip-mi-in-opener/1540006117")

        elif'open group' in query:
            webbrowser.open("https:\\groups.google.com/g/dsuece18b")

        elif'open song' in query:
            playsound('F:\\poco\\songs\\dheera.mp3')

        elif'open chat' in query:
            webbrowser.open("https:\\web.whatsapp.com")

        elif'open king' in query:
            os.startfile("F:\\WhatsApp Video")


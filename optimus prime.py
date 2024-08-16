import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon!")

    else:
        speak("Hello, Good Evening")

    speak(" Greetings, I am optimus prime. Please tell me how may I assist you sir rehaan!") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)
            print("Unable to Recognize your voice.")
            return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to the intel i've gathered")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Rehan Malik\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Rehan Malik\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open WhatsApp' in query:
            codePath = "C:\\Users\\Rehan Malik\\Desktop\\WhatsApp.lnk"
            webbrowser.open("WhatsApp.com")
            #os.startfile(codePath)

        elif 'quit' in query:
            speak("Goodbye master, have a nice day")
            exit()

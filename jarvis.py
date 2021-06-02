import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<16:
        speak("Goog Afternoon")

    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. How may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query
    


if __name__=="__main__":
    wishMe()

    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open mail' in query:
            webbrowser.open("mail.google.com")
           

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%Hhours%Mminutes%Sseconds")
            speak(f"The time is{strTime}")
            print(strTime)
            
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'open visual studio code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\vsrga\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)

        elif 'open arduino' in query:
            arduinoPath = "C:\\Users\\vsrga\\Desktop\\Arduino\\arduino.exe"
            os.startfile(arduinoPath)

        elif 'quit' in query:
            speak("ok shutting down Jarvis")
            quit()
           

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        
        
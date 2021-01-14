import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import wolframalpha #pip install wolframalpha
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('7VQT8V-E6EPVVUAWJ')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("AI:"+audio) 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Shaktimaan your digital assistant . Please tell me how may I help you")       

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
        print("I didn't understand what you said.")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manikantsangam.7@gmail.com', 'Manikant1998')
    server.sendmail('manikantsangam.7@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open("youtube.com")
             
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            speak('I am nice and full of energy') 

        elif 'open google' in query:
            speak('okay')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('okay')
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query or 'play song' in query:
            speak('Okay, here is your music! Enjoy!')
            music_dir = 'F:\\music\\New folder'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak('okay')
            codePath = "C:\\Users\\MANIKANT SANGAM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to alok' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sangam.manikant71@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                    print(e)
                    speak("Sorry my friend Manikant bro. I am not able to send this email")                
              
        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'quit' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query or 'hye' in query or 'hi' in query:
            speak('Hello Sir')  

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()  

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                speak('Try something different..!')
        
        speak('Next Command! Sir!')    
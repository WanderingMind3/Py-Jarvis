# program for shadow artificial intelligence.
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
from wikipedia import exceptions
# program for voice of shadow
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


# program for audio
def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 178)
    engine.runAndWait()    
# program for time wise wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon!")
    elif hour >= 15 and hour < 20:
        speak("good evening!")
    else:
        speak("Good Night!")
# program for greetings.
    speak("hello sir, I am shadow, your virtual private assistance. I am created by mister srivastava. Please tell me how may i help you?")
# program for taking orders through microphone.
import speech_recognition as sr
def takecommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        speak("recognizing...")
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        speak("Sorry sir, I am unable to understand what you have said.")
        print("Sorry Sir, I am unable to understand what you have said.")
        return "none"
    return query
# gmail id from which my shadow sends email.
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("iabhishek.4283@gmail.com", "why you want my gmail password?")
    server.sendmail("iabhishek.4283@gmail.com", to, content)
    server.close()

# program for taking orders
if __name__ == "__main__":
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()
        
 # program to search any topic in wikipedia.        
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("Alright")
            print("Alright")
            speak("According to wikipedia")
            print(results)
            speak(results)
# program to open google.
        elif 'open google' in query:
            print("Opening Google")
            speak("opening google")
            webbrowser.open("Google.com")
# program to open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("opening youtube")
            speak("opening youtube")
# program to open gmail
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            print("opening gmail")
            speak("opening gmail")
# program to open visual studio code
        elif 'code' in query:
            os.open("//home//abhishek//Desktop//visual studio code")
            print("opening code")
            speak("opening code")
# program to view time.
        elif 'the time' in query:
            strTime = datetime.datetime.strftime("%H:%M:%S")
            print(f"sir, The time is {strTime}")
            speak(f"sir, The time is {strTime}")
# program to translate in any language.
        elif 'translate' in query:
            webbrowser.open("translate.google.co.in")
            print("opening translator")
            speak("opening translator")
# program to open whatsapp.
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            print("opening whatsapp")
            speak("opening whatsapp")
        elif 'open game' in query:
            os.open("//home//abhishek//abhishek//space hero.py")

# program to send email to abhishek{it means me ;)}
        elif  'email to abhishek' in query:
            try:
                speak("what should i say?")
                print("What should I say?")
                content = takecommand()
                to = "iabhishek.4283@gmail.com"
                sendEmail (to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except exceptions as e:
                speak("Sorry Sir, I am not able to send this email")
                print("Sorry Sir, I am not able to send this email :(")
# program to stop shadow
        elif 'quit' in query or 'bye' in query:
            print("Thanks for your time sir, Have a good day!")
            speak("Thanks for your time sir, Have a good day!")
            exit
# speacial program only made to applause me.
        elif 'who are you' in query:
            print("I am just a small virtual assistant project created by mister srivastava, well known data scientist, hacker and developer. Mister Srivastava created me for helping others and making this world a good place. Thanks for showing your interest in me. Have a good day, Sir!") 
            speak("I am just a small virtual assistant project created by mister srivastava, well known data scientist, hacker and developer. Mister Srivastava created me for helping others and making this world a good place. Thanks for showing your interest in me. Have a good day, Sir!")
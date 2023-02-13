import pyttsx3 # pip install pyttsx3 (text to speech library, It can work offline)
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

#Initializing the pyttsx3
engine = pyttsx3.init()

# Changing the voice of the system and speak rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# speak rate fast control
newVoiceRate = 180
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)# It converts text to speech
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def greet():
    speak("Welcome back sir or ma'am!")
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<=22:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Monday at your servie. How Can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en=in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def Sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() 
    server.starttls() # we need to send the email
    # Above lines of code used to check our connection with gmail
    server.login("yourmail@gmail.com", "mail_Password")
    server.sendmail("youwanttosend@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\Downloads\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def yourself():
    speak("I am a AI Virtual Assistant, who provide few of the notable functionalities for humans to execute their tasks in easier way.")

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching....")
            query == query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'youwanttosend@gmail.com'
                Sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdowm" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = "C:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in  query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember"+data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything " in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
        elif "about yourself" in query:
            yourself()
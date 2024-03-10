import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

        
if __name__ == "__main__":
    wishMe()
    
    speak ("Allow me to introduce myself, I am Sherlock an ai assistant. ")
    voice = pyttsx3.init()
    In = input("Searching wikipedia/google: ")
    result = wikipedia.summary(In, sentences = 3)
    print(result)
    voice.say(result)
    voice.runAndWait()
    

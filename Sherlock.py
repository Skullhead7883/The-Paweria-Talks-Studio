import pyttsx3
import datetime

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

        speak("Hi I am Sherlock which stands for Smart, Highly Advanced, Efficient, Responsive, Logical, Observant, Compassionate and Knowledgeable. Sir like this acronym so much and so do I")
if __name__ == "__main__":
    wishMe()
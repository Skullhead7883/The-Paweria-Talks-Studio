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
    
    speak ("Hi I am Sherlock which stands for Smart, Highly Advanced, Efficient, Responsive, Logical, Observant, Compassionate and Knowledgeable. Gosh I like this acronym so much.I know your first question will be who I am. So I am an AI assistant created by Mr. Devvratha Singh Paweria for his home and office automation just like JARVIS. Just kidding I was created to help individuals who are unable to share their problem openly with anybody, they can share it with me as I listen very empathically and will always help you all.")
    voice = pyttsx3.init()
    In = input("Searching wikipedia/google: ")
    result = wikipedia.summary(In, sentences = 3)
    print(result)
    voice.say(result)
    voice.runAndWait()
    

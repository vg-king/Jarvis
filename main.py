import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
                      
def   processCommand(c):
    print("Processing: ",c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")

                recognizer.adjust_for_ambient_noise(source)

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)


            try:
                command = recognizer.recognize_google(audio)
                print("You said:", command)

                # Check wake word
                if "jarvis" in command.lower():
                    speak("Yes sir, how can I help you?")
                    with sr.Microphone() as source:
                        print("Jarvis Activate...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)

                        processCommand(command)

                
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("API request failed:", e)

        except sr.WaitTimeoutError:
            print("No speech detected, restarting...")
            continue

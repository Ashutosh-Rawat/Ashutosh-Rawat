import speech_recognition as sr
import os
import webbrowser
import pyttsx3

r = sr.Recognizer()
convert = pyttsx3.init()
convert.setProperty('rate', 160)
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
convert.setProperty('voice', voice_id)

with sr.Microphone() as source:
    try:
        print("Listening...")
        audio1 = r.listen(source, 2, 20)
        print("Speech done")

        command = r.recognize_google(audio1)

        if "notepad" in command.lower():
            pyttsx3.speak("Opening notepad")
            os.system("Notepad")
        elif "chrome" in command.lower():
            pyttsx3.speak("Opening chrome")
            url = 'https://pythonexamples.org'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
            print("chrome opened")
        elif "command prompt" in command.lower():
            pyttsx3.speak("Opening Command prompt")
            os.system("cmd")
        else:
            pyttsx3.speak("Sorry, I can't do that")
        print("Said command was:", command)

    except sr.UnknownValueError:
        pyttsx3.speak("I didn't get that")

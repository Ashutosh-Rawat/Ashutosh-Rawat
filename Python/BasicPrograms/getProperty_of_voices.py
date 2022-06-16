import pyttsx3
convert = pyttsx3.init()
voices = convert.getProperty('voices')
for voice in voices:
    # to get the info. about various voices in our PC
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)
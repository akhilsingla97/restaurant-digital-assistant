# import speech_recognition as sr
# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print("Say Something")
#     audio = r.listen(source)
#     print("Thanks")
#
# try:
#     print("text: "+ r.recognize_google(audio))
# except:
#     pass

""" IMPORTS """

# from PyDictionary import PyDictionary
import os
import speech_recognition as sr

""""""


def getWordFromMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        s = r.recognize_google(audio)
        print(s)
        return s
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def getSentence():
    s = "espeak '" + "Speak" + "'"
    os.system(s)
    In = getWordFromMic()
    return In


"""
	Using espeak : eSpeak is a compact open source software speech
	synthesizer for English and other languages, for Linux and Windows.
"""


def speak(s):
    s = "espeak '" + s + "'"
    os.system(s)


def start():
    s = getSentence()
    speak(s)


if __name__ == "__main__":
    start()

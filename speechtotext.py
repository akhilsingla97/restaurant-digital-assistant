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

# dictionary = PyDictionary()


# Print Meaning of a word

# def tellMeaning(s):
#     dic = dictionary.meaning(s)
#     print(dic)
#     twice = 0
#     for i in dic['Noun']:
#         twice += 1
#         speak(i.lower())
#         if twice == 2:
#             break
#
#
# def tellSynonym(s):
#     dic = dictionary.synonym(s)
#     print(dic)
#     for i in dic:
#         speak(i.lower())
#
#
# def tellAntonym(s):
#     dic = dictionary.antonym(s)
#     print(dic)
#     for i in dic:
#         speak(i.lower())


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


def getWord():
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
    s = getWord()
    speak(s)
    # if init == "meaning":
    #     tellMeaning(s)
    # elif init == "synonym":
    #     tellSynonym(s)
    # elif init == "antonym":
    #     tellAntonym(s)


if __name__ == "__main__":
    start()
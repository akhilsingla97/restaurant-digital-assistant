###For a naive approach we build several use case scenarios and map the user query to the one most suitable and reply accordingly
'''IMPORTS'''
import os
import spacy
import speech_recognition as sr

scenarios = ["Bring some food", "Clear the table", "Bring some water", "Can you tell me the main cuisines?", "Can I get the menu please?"]

food_items = {'burger':{'Cheese','Chicken'}, 'pizza':{'margharita', 'farm house'}, 'pasta':{'red-sauce', 'white-sauce'}, 'Chinese':{'noodles','momos'}}

chef_special = ['Chilly Rooster Burger', 'Red Wine Pasta']

espeak = "espeak '"

def responseToFoodItems():
    choice = input()
    if choice in food_items:
         print(choice, food_items[choice])
    else:
        os.system(espeak + "'Sorry, we don't have it. You can try" + )

def responseToQueries(s):
    if(s==0):
        osCommand = espeak + "What would you prefer to have?'"
    elif(s==1):
        osCommand = espeak + "Sending someone at your service, till then you can have a look at our menu'"
    elif(s==4):
        osCommand = "espeak -g 50 '"
        for food in food_items:
            osCommand += food + " ,"
        osCommand+="'"
        os.system(osCommand)
        responseToFoodItems()
    else:
        osCommand = espeak + "Sorry, I could not understand!'"
    os.system(osCommand)

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

def askForService():
    print("Enter Query: ")  #in the actual system this will be the voice input
    query = input()

    similarity = []
    max = 0.0
    query_index = -1
    i = 0
    nlp = spacy.load('en_core_web_sm')
    for scenario in scenarios:
        doc1 = nlp(query)
        doc2 = nlp(scenario)
        similarity.append(doc1.similarity(doc2))
        if similarity[i] > max :
            max = similarity[i]
            query_index = i
        i = i + 1

    print (similarity)
    if max<0.7:
        print("Sorry, I couldn't understand!")
        query_index = -1

    responseToQueries(query_index)

if __name__ == "__main__":
    #os.system(espeak + "Welcome to our restaurant! Can I know who I am supposed to serve?'")
    #name = input("Name: ")

    #os.system(espeak + "Greetings " + name + ". What would you like to have?'")
    askForService()

    #start()

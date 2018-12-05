###For a naive approach we build several use case scenarios and map the user query to the one most suitable and reply accordingly
'''IMPORTS'''
import os
import spacy
import random
import signal
import sys
from sshopen import openssh
import time
import datetime
from datetime import datetime
import speech_recognition as sr

#connection parameters
ip = '172.31.65.128'
usr = 'amrit'
psw = '1541'
remotePath = "/home/amrit/logs/convlog.txt"
#opening ssh connection
ssh = openssh(ip,usr,psw)

#array of scenario
scenarios = ["Bring some food", "Clear the table", "Bring some water", "Can you tell me the main cuisines?", "Get the menu please"]
food_items = {'burger':{'Cheese','Chicken'}, 'pizza':{'margharita', 'farm house'}, 'pasta':{'red-sauce', 'white-sauce'}, 'Chinese':{'noodles','momos'}}
chef_special = ['Chilly Rooster Burger', 'Red Wine Pasta']
flite = "flite -voice slt '"
espeak = "espeak '"
end = "'"


#logging of session
def appendToRemoteFile(message):
    ts = time.time()
    timestamp = datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
    cmd = "echo " + timestamp + ":" + message + " >> " + remotePath
    ssh.exec_command(cmd)

#triggered when asked for food items
def responseToFoodItems():
    choice = input()
    appendToRemoteFile(choice)
    if choice in food_items:
        print(choice, food_items[choice])
    else:
        message = "Sorry, we do not have it. You can try " + chef_special[random.randint(0,1)]
        os.system(espeak + message + end)
        appendToRemoteFile(message)

#responding to queries
def responseToQueries(s):
    message = ""
    if(s==0):
        message += "What would you prefer to have?"
        osCommand = espeak + message + end
        os.system(osCommand)
        appendToRemoteFile(message)

    elif(s==1 or s==2):
        message += "Sending someone at your service, till then you can have a look at our menu"
        osCommand = espeak + message + end
        os.system(osCommand)
        appendToRemoteFile(message)

    elif(s==3):
        message += "You can try " + chef_special[random.randint(0,1)]
        osCommand = espeak + message + end
        os.system(osCommand)
        appendToRemoteFile(message)

    elif(s==4):
        #osCommand = "espeak -g 50 '"
        osCommand = espeak
        for food in food_items:
            message += food + " , "
        osCommand += message + end
        os.system(osCommand)
        appendToRemoteFile(message)
        responseToFoodItems()

    else:
        message += "Sorry, I could not understand!"
        osCommand = espeak + message + end
        os.system(osCommand)
        appendToRemoteFile(message)


#getting word from Mic
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


"""def getWord():
    s = "espeak '" + "Speak" + "'"
    os.system(s)
    In = getWordFromMic()
    return In
"""

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
    appendToRemoteFile(query)

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

def closeConnection():
    ssh.close()

if __name__ == "__main__":
    #openConnection()
    welcomeMessage = "Welcome to our restaurant! Can I know who I am supposed to serve?"
    os.system(espeak + welcomeMessage + end)
    appendToRemoteFile(welcomeMessage)

    name = input("Name: ")
    appendToRemoteFile(name)

    os.system(espeak + "Greetings " + name + ". What would you like to have?'")
    appendToRemoteFile("Greetings " + name + ". What would you like to have?")

    askForService()
    closeConnection()


#signal handler
def signal_handler(sig, frame):
        print('You pressed Ctrl+C! Closing ssh connection')
        ssh.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

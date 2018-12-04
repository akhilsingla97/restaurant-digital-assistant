import os
import spacy
import json


def speak(s):
    s = "espeak '" + s + "'"
    os.system(s)

last_weight = 0

def debug(query, obj):
    # last_weight += 1
    global last_weight
    ok = input("Want to add this query with new answer in db? ")
    if ok is "y" or ok is "Y" or ok is "1":
        print("------------------------------------------------------------")
        solution = input("Write answer for this query: ")
        typeofquery = input("Enter type of the query: food or general? ")
        last_weight += 1
        obj["queries"].append({
            query : {
                "annotation": solution ,
                "type": typeofquery ,
                "weight": last_weight 
            } 
        })
        with open('database.json', 'w') as outfile:  
            obj = json.dumps(obj, indent=4)
            outfile.write(obj)
        print('-------------------------------------------------------------')
    else:
        return


def askForService():
    while True:
        query = input("Ask me anything: ")
        if "bye" in query:
            print("Thank you for visiting our restauarnt.. Have a good day.")
            break
        obj = {}
        with open('database.json', 'r') as fp:
            obj = json.load(fp)
        queries = obj["queries"]
        similarity = 0
        query_detail = "none"
        nlp = spacy.load('en_core_web_sm')
        foundAMatch = 0
        i=0
        solution = []
        for q in queries:
            for x, y in q.items():
                doc1 = nlp(query)
                doc2 = nlp(x)
                tmpSimilarity = doc1.similarity(doc2)
                details = {}
                if tmpSimilarity > similarity and tmpSimilarity > 0.5:
                    similarity = tmpSimilarity
                    details["answer"] = y["annotation"]
                    details["weight"] = y["weight"]
                    del solution[:]
                    solution.append(details)
                    foundAMatch = 1
                elif tmpSimilarity == similarity and tmpSimilarity > 0.5:
                    similarity = tmpSimilarity
                    details["answer"] = y["annotation"]
                    details["weight"] = y["weight"]
                    solution.append(details)
                    foundAMatch = 1
                

            i+=1
        if foundAMatch is 0:
            print("Sorry! I don't understand.")
            debug(query, obj)
        else:
            wt = 0
            finalAnswerToPrint = ""
            for details in solution:
                if wt < details["weight"]:
                    wt = details["weight"]
                    finalAnswerToPrint = details["answer"]
            print(finalAnswerToPrint)
            debug(query, obj)

def fetchWeight():
    global last_weight
    with open("config.txt", 'r') as config:
        obj = json.load(config)
        last_weight = obj["latest_weight"]
    return obj

def updateLastWeight(obj):
    with open('config.txt', 'w') as outfile:  
            obj["latest_weight"] = last_weight
            obj = json.dumps(obj, indent=4)
            outfile.write(obj)

if __name__ == "__main__":
    # speak("Welcome to our restaurant! Can I know who I am supposed to serve?")
    # name = input("Name: ")
    # speak("Greetings " + name + ". What would you like to have?")
    obj = fetchWeight()
    askForService()
    updateLastWeight(obj)
    
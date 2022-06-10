import requests
from random import sample

user = "4D_Potatoes"
response = requests.get("https://apps.runescape.com/runemetrics/quests?user=" + user).json()

def getEligibleQuests():
    quests = []
    exceptions = ["Recipe for Disaster", "Dimension of Disaster"]
    for quest in response["quests"]:
        eligible = quest["userEligible"]
        status = quest["status"]
        qp = quest["questPoints"]
        title = quest["title"]
        if eligible and status != "COMPLETED" and qp > 0 and title not in exceptions:
            quests.append(title)
    return quests

def getRandomQuests(quests, amount):
    randomQuests = sample(quests, amount)
    with open("Your new quests.txt", "w") as file:
        for quest in randomQuests:
            file.write(quest + "\n")
    with open("YNQ_Wikiguides.bat", "w") as file:
        file.write("@echo off\n")
        for index, quest in enumerate(randomQuests):
            start_ff = "start firefox " if index == 0 else ""
            file.write(start_ff + "\"https://runescape.wiki/w/" + quest + "/Quick_guide\" ")
    print("DONE!")

quests = getEligibleQuests()
getRandomQuests(quests, 5)

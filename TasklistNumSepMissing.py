import requests
import re

response = requests.get("https://taskman.rs/api/tasks").json()

def getNecessaryInfo(fields=["title", "description"], createLaunchers=False):
    re_exceptions = "9999"
    ids = []
    with open("Tasklist.txt", "w") as file:
        for task in response:
            desc = task["description"]
            if re.search("\d{4,}", desc) and not re.search(re_exceptions, desc):
                ids.append(task["id"])
                for f in fields:
                    file.write(f + ": " + task[f] + "\n")
                file.write("\n")
    if createLaunchers:
        counter = 0
        fileCounter = 0
        for index, taskID in enumerate(ids):
            if index % 15 == 0:
                fileCounter += 1
                with open("EditTasks_" + str(fileCounter) + ".bat", "w") as file:
                    file.write("@echo off\n")
            with open("EditTasks_" + str(fileCounter) + ".bat", "a") as file:
                start_ff = "start firefox " if index % 15 == 0 else ""
                file.write(start_ff + "\"URL REMOVED FOR PUBLIC" + str(taskID) + "URL REMOVED FOR PUBLIC\" ")
        print("DONE!")
                    

getNecessaryInfo(["title", "description"], True)

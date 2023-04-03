from db import *
from controller import *

devTeamMin = 8
qatTeamMin = 4
secTeamMin = 5
numInDevTeam = int((str(repo_db.numberInTeam("dev")))[2:-3])
numInQatTeam = int((str(repo_db.numberInTeam("qat")))[2:-3])
numInSecTeam = int((str(repo_db.numberInTeam("sec")))[2:-3])

devDiff = (devTeamMin - numInDevTeam)
qatDiff = (qatTeamMin - numInQatTeam)
secDiff = (secTeamMin - numInSecTeam)

class service():
    def selectComp(YoN):
        Yes = ["y","n"]
        while YoN not in Yes:
            YoN = input("Please try again (y/n): ")
        if YoN == "y":
            clause = input("Please input WHERE clause (WHERE...): ")
        elif YoN == "n":
            clause = " "
        return clause

print("==========================")
if numInDevTeam < devTeamMin:
    print(f"Number in dev: {numInDevTeam}")
    print(f"You need to hire {devDiff} developer(s)!")
elif numInDevTeam >= devTeamMin:
    print(f"Number in dev: {numInDevTeam}")
    print("Adequate developers in team")
print("")
if numInQatTeam < qatTeamMin:
    print(f"Number in QA: {numInQatTeam}")
    print(f"You need to hire {qatDiff} QA Tester(s)!")
elif numInQatTeam >= qatTeamMin:
    print(f"Number in QA: {numInQatTeam}")
    print("Adequate QA testers in team")
print("")

if numInSecTeam < secTeamMin:
    print(f"Number in Security: {numInSecTeam}")
    print(f"You need to hire {secDiff} security guard(s)!")
elif numInSecTeam >= secTeamMin:
    print(f"Number in Security: {numInSecTeam}")
    print("Adequate security guards")
print("")

toBeDone = ["read", "write", "exit"]
toDo = controller.RWE()

while toDo not in toBeDone:
    toDo = input("Please try again (read/write/exit): ")
again = "y"
while again == "y":
    if toDo == "read":
        specific = ["all","more"]

        howSpecific = controller.howSpec()
        while howSpecific not in specific:
            howSpecific = input("Please try again(all/more): ")

        if howSpecific == "all": 
            print(repo_db.readAllEmp())
            again = controller.useAgain()
            if again == "y":
                toDo = controller.RWE()
            else:
                break

        elif howSpecific == "more":
            print(repo_db.readSpecific(controller.whatToSelect(), service.selectComp(controller.whatWhere())))
            again = controller.useAgain()
            if again == "y":
                toDo = controller.RWE()
            else:
                break

    elif toDo == "write":
        actions = ["add", "edit", "delete"]
        action = controller.inputAction()

        while action not in actions:
            action = controller.whileInvalidAction()
        
        if action == "add":
            repo_db.addEmp(controller.getNewEmpName(),controller.getNewEmpTeam())
            conn.commit()
            print("Added colleague!")
            again = controller.useAgain()
            if again == "y":
                toDo = controller.RWE()
            else:
                break
        
        elif action == "edit":
            repo_db.updateEmpName(controller.getNewEmpName(), controller.getEmpId())
            conn.commit()
            print("Edited colleague information!")
            again = controller.useAgain()
            if again == "y":
                toDo = controller.RWE()
            else:
                break
        
        elif action == "delete":
            repo_db.delEmpData(controller.getEmpId())
            conn.commit()
            print("Deleted colleague information!")
            again = controller.useAgain()
            if again == "y":
                toDo = controller.RWE()
            else:
                break
    else:
        break

print("""

Terminating program
    
==========================""")
print("==========================")
conn.commit()

  

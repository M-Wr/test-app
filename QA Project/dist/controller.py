class controller:
    def RWE():
        toDo = input("Would you like to read/write a record or exit? (read/write/exit): ")
        toDo = toDo.lower()
        return toDo
    
    def howSpec():
        howSpecific = input("Would you like to read all or be more specific? (all/more): ")
        return howSpecific

    def whatToSelect():
        options = ["emp_id", "emp_name", "business_unit", "emp_active"]
        select = input("What would you like to select? (emp_id/emp_name/business_unit/emp_active): ")
        while select not in options:
            select = input("Please try again (emp_id/emp_name/business_unit/emp_active): ")
        return select

    def whatWhere():
        YoN = input("Would you like a WHERE clause? (y/n): ")
        YoN = YoN.lower()
        return YoN
             
    def inputAction():
        action = input("What action would you like make? (add/edit/delete): ")
        return action
    
    def whileInvalidAction():
        action = input("Please type valid input (add/edit/delete): ")
        return action
    
    def getNewEmpName():
        emp_name = input("What is the employee's new name?: ")
        return emp_name

    def getNewEmpTeam():
        business_unit = input("What is there business unit?: ")
        return business_unit
    def getEmpId():
        emp_id = input("What is the employee's emp id?: ")
        return emp_id

    def useAgain():
        again = input("Would you like to do anything else? (y/n): ")
        return again

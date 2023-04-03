import _sqlite3 as sql
conn = sql.connect("roster.db")
#conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

class repo_db:
    def CreatingTable():
        sql_file = open("roster.sql")
        sql_string = sql_file.read()
        cursor.executescript(sql_string)
        return True

    def selectQuery(query):
        return cursor.execute(query).fetchall()

    def dataQuery(query):
        cursor.execute(query)
        return True

    def readAllEmp():
        query = "SELECT * FROM employees"
        return repo_db.selectQuery(query)
    
    def readSpecific(select,clause):
        query = f'SELECT {select} FROM employees {clause};'
        return repo_db.selectQuery(query)

    def addEmp(emp_name, business_unit):
        query = f'INSERT INTO employees(emp_name, business_unit) VALUES ("{emp_name}", "{business_unit}")'
        return repo_db.dataQuery(query)

    def updateEmpName(name, emp_id):
        query = f"UPDATE employees SET emp_name = '{name}' WHERE emp_id = '{emp_id}';"
        return repo_db.dataQuery(query)
    
    def delEmpData(emp_id):
        query = f'DELETE FROM employees WHERE emp_id = "{emp_id}";'
        return repo_db.dataQuery(query)
    
    def numberInTeam(team):
        query = f'SELECT COUNT(*) FROM employees WHERE business_unit = "{team}";'
        return repo_db.selectQuery(query)
    
conn.commit()



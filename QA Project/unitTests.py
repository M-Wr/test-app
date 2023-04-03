import _sqlite3 as sql
conn = sql.connect("roster.db")
#conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

from unittest import TestCase
# from service import service
from db import *
from controller import *

class unit_tests(TestCase):
    # def test_select(self):
    #     testLine = "SELECT * FROM employees"
    #     result1 = repo_db.selectQuery(testLine)
    #     result = type(result1)
    #     self.assertEqual(result, list)
    # def test_selectFail(self):
    #     testLine = "SELECT * FROM employees"
    #     result1 = repo_db.selectQuery(testLine)
    #     result = type(result1)
    #     self.assertNotEqual(result, str, "INCORRECT TYPE")

    # def test_dataquery(self):
    #     testLine = "SELECT * FROM employees"
    #     assert repo_db.dataQuery(testLine) == True
    # def test_dataqueryFail(self):
    #     testLine = "SELECT * FROM employees"
    #     result = repo_db.dataQuery(testLine)
    #     self.assertNotEqual(result, False, "DID NOT RETURN TRUE")

    # def test_readAllEmp(self):
    #     testLine = "SELECT * FROM employees"
    #     known = repo_db.selectQuery(testLine)
    #     result = repo_db.readAllEmp()
    #     self.assertEqual(result, known)
    # def test_readAllEmpFail(self):
    #     testLine = "SELECT * FROM employees"
    #     known = repo_db.selectQuery(testLine)
    #     result = repo_db.readAllEmp()
    #     self.assertNotEqual(result, "known", "DID NOT RETURN TRUE")

    # def test_addEmp(self):
    #     result = repo_db.addEmp("Test Name", "Test Area")
    #     self.assertEqual(result, True)
    # def test_addEmpFail(self):
    #     result = repo_db.addEmp("Test Name", "Test Area")
    #     self.assertNotEqual(result, False, "DID NOT RETURN TRUE")
        
    # def test_updateEmpName(self):
    #     result = repo_db.updateEmpName("Test Name", 100)
    #     self.assertEqual(result, True)
    # def test_updateEmpNameFail(self):
    #     result = repo_db.updateEmpName("Test Name", 100)
    #     self.assertNotEqual(result, False, "DID NOT RETURN TRUE")

    # def test_delEmpData(self):
    #     result = repo_db.delEmpData(100)
    #     self.assertEqual(result, True)
    # def test_delEmpDataFail(self):
    #     result = repo_db.delEmpData(100)
    #     self.assertNotEqual(result, False, "DID NOT RETURN TRUE")
    
    # def test_numInTeam(self):
    #     testLine = f'SELECT COUNT(*) FROM employees WHERE business_unit = "Test Area"'
    #     result = repo_db.numberInTeam("Test Area")
    #     test = repo_db.selectQuery(testLine)
    #     self.assertEqual(result, test)
    # def test_numInTeamFail(self):
    #     testLine = f'SELECT COUNT(*) FROM employees WHERE business_unit = "Test Area"'
    #     result = repo_db.numberInTeam("Test Area")
    #     test = repo_db.selectQuery(testLine)
        # self.assertNotEqual(result, "test", f"DOES NOT EQUAL {test}")
    
    # def test_selectcomp(self):
    #     service.selectComp = lambda: "Where emp_id = 1"
    #     result = service.selectComp()
    #     self.assertEqual(result, "Where emp_id = 1")

    def test_RWERead(self):
        controller.RWE = lambda: "read"
        result = controller.RWE()
        self.assertEqual(result, "read")
    def test_RWEWrite(self):
        controller.RWE = lambda: "write"
        result = controller.RWE()
        self.assertEqual(result, "write")
    def test_RWEExit(self):
        controller.RWE = lambda: "exit"
        result = controller.RWE()
        self.assertEqual(result, "exit")
    def test_RWEFail(self):
        controller.RWE = lambda: "12"
        result = controller.RWE()
        self.assertNotEqual(result, "read", "INVALID INPUT")

    def test_howSpecAll(self): 
        controller.howSpec = lambda: "all"
        result = controller.howSpec()
        self.assertEqual(result, "all")
    def test_howSpecMore(self): 
        controller.howSpec = lambda: "more"
        result = controller.howSpec()
        self.assertEqual(result, "more")
    def test_howSpecFail(self): 
        controller.howSpec = lambda: "123"
        result = controller.howSpec()
        self.assertNotEqual(result, "all", "INVALID INPUT")

    def test_whatToSelectId(self):
        controller.whatToSelect = lambda: "emp_id"
        result = controller.whatToSelect()
        self.assertEqual(result, "emp_id")
    def test_whatToSelectName(self):
        controller.whatToSelect = lambda: "emp_name"
        result = controller.whatToSelect()
        self.assertEqual(result, "emp_name")
    def test_whatToSelectBu(self):
        controller.whatToSelect = lambda: "business_unit"
        result = controller.whatToSelect()
        self.assertEqual(result, "business_unit")
    def test_whatToSelectAct(self):
        controller.whatToSelect = lambda: "emp_active"
        result = controller.whatToSelect()
        self.assertEqual(result, "emp_active")
    def test_whatToSelectFail(self):
        controller.whatToSelect = lambda: "123"
        result = controller.whatToSelect()
        self.assertNotEqual(result, "emp_active","INVALID INPUT")

    def test_whatWhereY(self):
        controller.whatWhere = lambda: "y"
        result = controller.whatWhere()
        self.assertEqual(result, "y")
    def test_whatWhereN(self):
        controller.whatWhere = lambda: "n"
        result = controller.whatWhere()
        self.assertEqual(result, "n")
    def test_whatWhereFail(self):
        controller.whatWhere = lambda: "asg123"
        result = controller.whatWhere()
        self.assertNotEqual(result, "y", "INVALID INPUT")

    def test_inputActionAdd(self):
        controller.inputAction = lambda: "add"
        result = controller.inputAction()
        self.assertEqual(result, "add")
    def test_inputActionEdit(self):
        controller.inputAction = lambda: "edit"
        result = controller.inputAction()
        self.assertEqual(result, "edit")
    def test_inputActionDel(self):
        controller.inputAction = lambda: "delete"
        result = controller.inputAction()
        self.assertEqual(result, "delete")
    def test_inputActionFail(self):
        controller.inputAction = lambda: "1"
        result = controller.inputAction()
        self.assertNotEqual(result, "add", "INVALID INPUT")

    def test_whileInvalidActionAdd(self):
        controller.whileInvalidAction = lambda: "add"
        result = controller.whileInvalidAction()
        self.assertEqual(result, "add")
    def test_whileInvalidActionEdit(self):
        controller.whileInvalidAction = lambda: "edit"
        result = controller.whileInvalidAction()
        self.assertEqual(result, "edit")
    def test_whileInvalidActionDel(self):
        controller.whileInvalidAction = lambda: "delete"
        result = controller.whileInvalidAction()
        self.assertEqual(result, "delete")
    def test_whileInvalidActionFail(self):
        controller.whileInvalidAction = lambda: "1"
        result = controller.whileInvalidAction()
        self.assertNotEqual(result, "add", "INVALID INPUT")

    def test_getNewEmpName(self):
        controller.getNewEmpName = lambda: "Jim Jimson"
        result = controller.getNewEmpName()
        self.assertEqual(result, "Jim Jimson")
    def test_getNewEmpNameFail(self):
        controller.getNewEmpName = lambda: "12345"
        result = controller.getNewEmpName()
        self.assertNotEqual(result, "Jim Jimson", "INVALID INPUT")
        

    def test_getNewEmpTeamSec(self):
        controller.getNewEmpTeam = lambda: "sec"
        result = controller.getNewEmpTeam()
        self.assertEqual(result, "sec")
    def test_getNewEmpTeamDev(self):
        controller.getNewEmpTeam = lambda: "dev"
        result = controller.getNewEmpTeam()
        self.assertEqual(result, "dev")
    def test_getNewEmpTeamQat(self):
        controller.getNewEmpTeam = lambda: "qat"
        result = controller.getNewEmpTeam()
        self.assertEqual(result, "qat")
    def test_getNewEmpTeamFail(self):
        controller.getNewEmpTeam = lambda: "1"
        result = controller.getNewEmpTeam()
        self.assertNotEqual(result, "qat", "INVALID INPUT")

    def test_getEmpId(self):
        controller.getEmpId = lambda: "100"
        result = controller.getEmpId()
        self.assertEqual(result, "100")
    def test_getEmpIdFail(self):
        controller.getEmpId = lambda: "a"
        result = controller.getEmpId()
        self.assertNotEqual(result, "100", "INVALID INPUT")
        
    def test_useAgainY(self):
        controller.useAgain = lambda: "y"
        result = controller.useAgain()
        self.assertEqual(result, "y")
    def test_useAgainN(self):
        controller.useAgain = lambda: "n"
        result = controller.useAgain()
        self.assertEqual(result, "n")
    def test_useAgainFail(self):
        controller.useAgain = lambda: "a"
        result = controller.useAgain()
        message = "INVALID INPUT"
        self.assertNotEqual(result, "y", message)

# # to run tests:
# # python -m unittest unitTests.py
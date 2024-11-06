from Employee import Employee

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def displayAllEmployees(self):
        if not self.employees:
            print("Brak pracowników.")
        for employee in self.employees:
            print(employee.describeEmployee())

    def removeEmployeesInAgeRange(self, minAge, maxAge):
        self.employees = [emp for emp in self.employees if not (minAge <= emp.age <= maxAge)]
        print(f"Pracownicy w przedziale wiekowym {minAge}-{maxAge} zostali usunięci.")

    def findEmployeeByName(self, name):
        foundEmployee = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        if foundEmployee:
            for employee in foundEmployee:
                print(employee.describeEmployee())
        else:
            print(f"Nie znaleziono pracownika o nazwisku {name}.")

    def updateEmployeeSalary(self, name, newSalary):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.updateSalary(newSalary)
                print(f"Wynagrodzenie pracownika {name} zostało zaktualizowane.")
                return
        print(f"Pracownik o nazwisku {name} nie został znaleziony.")

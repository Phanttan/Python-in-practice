# Encapsulation.py

# https://pynative.com/python-encapsulation/

class Company:
    def __init__(self) -> None:
        # protected data member
        self._project ='OOP'


class Employee(Company):
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary
        Company.__init__(self)

    # Create a public method to access private methods
    def getSalary(self):
        print("Salary:", self.__salary)

    def setSalary(self):
        self.__salary = max(self.__salary, 20000)
        print("Salary:", self.__salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# access directly public data member 
print(emp.name)
# accessing directly private data members
# print('Salary:', emp.__salary)
# --> AttributeError: 'Employee' object has no attribute '__salary'

# Accessing Private data member from method
print(emp.getSalary())
print(emp.setSalary())

# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)

# access protected data access
print(emp._project)
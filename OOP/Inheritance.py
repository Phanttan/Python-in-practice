class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):


    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName,lastName,idNumber, numScores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.numScores = numScores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        self.scores = scores
        sum = 0
        for ind in self.scores:
            sum += ind
        a = int(sum/numScores)

        if a < 40:
            return "T"
        if a >= 40 and a < 50:
            return "D"
        if a >= 55 and a < 70:
            return "P"
        if a >= 70 and a < 80:
            return "A"
        if a >= 80 and a < 90:
            return "E"
        if a >= 90 and a <= 100:
            return "O"



line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()


# Input
# Heraldo Memelli 8135627
# 2
# 100 80

# Output
# Name: Memelli, Heraldo
# ID: 8135627
# Grade: O
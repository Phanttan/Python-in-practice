# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:18:07 2019

@author: Phan Thanh Tan
"""

class Student:
    """
    Define Student Class with property decorator
    """
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.got_marks = f'{self.name} obtained {self.marks} marks'

    def got_marks1(self):
        """
        Got marks Method
        """
        return print(
            f'First Round (No Using Property Decorator):{cyan(self.name)} obtained {magenta(self.marks)} marks'
        )

    @property
    def got_marks2(self):
        res = cyan(self.name) + ' obtained ' + magenta(self.marks) + ' marks'
        print('Second Round (Using Property Decorator):' + res)

    @got_marks2.setter
    def got_marks2(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks

    @got_marks2.deleter
    def got_marks2(self):
        self.name = None
        self.marks = 0


# Define an First Student
st = Student('An', '25')
print("The First Student's Name : {}".format(red(st.name)))
print("The First Student's Marks: {}".format(red(st.marks)))
print('First Student Information: {}'.format(red(st.got_marks)))
# Test with some methods
st.got_marks1  # No change
st.got_marks1()
st.name = 'Ba'
print('After Change Name: {}'.format(cyan(st.name)))
st.got_marks1()
# Beginning using Property Decorator
st.got_marks2  # Working because of property
#############################
st.got_marks2 = 'Tuan is 36' # Using .setter
# st.got_marks2
print('Name after using .setter: {}'.format(blue(st.name)))
print('Marks after using .setter: {}'.format(blue(st.marks)))
#############################
del st.got_marks2
print('Name after using .deleter : {}'.format(green(st.name)))
print('Marks after using .deleter: {}'.format(green(st.marks)))

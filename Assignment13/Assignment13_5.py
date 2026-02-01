"""
Question: Write a program which accepts marks and displays grade.
Condition Example:
≥ 75 → Distinction
≥ 60 → First Class
• ≥ 50 → Second Class
• < 50 → Fail

"""
from enum import Enum

class Grade(Enum):
    DISTINCTION = "Distinction"
    FIRST_CLASS = "First Class"
    SECOND_CLASS = "Second Class"
    FAIL = "Fail"

from math import pi

def getGradesFrom(marks):
    if marks >= 75:
        return Grade.DISTINCTION.value
    elif marks >= 60:
        return Grade.FIRST_CLASS.value
    elif marks >= 50:
        return Grade.SECOND_CLASS.value
    else:
        return Grade.FAIL.value


def main():
    marks = int(input("Enter marks: "))
    print("Result is: ", getGradesFrom(marks))


if __name__ == "__main__":
    main()
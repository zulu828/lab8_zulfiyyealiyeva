"""Main solutions for Laboratory 8: Functions."""

from utils import add_vat, build_username, add_bonus, with_bonus, average, make_course


# Task 1
def print_student_card(name, group, year):
    """Print a student's name, group, and year."""
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))


print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
# print_student_card("Ali", "CE-101")  # Intentionally missing one argument


# Task 2 (function is in utils.py)
print(add_vat(100))
print(add_vat(50, 10))
print(add_vat(vat_percent=5, price=80))


# Task 3 (function is in utils.py)
print(build_username("Aysel", "Mammadova"))
print(build_username("Kamran", "Aliyev", 2005))


# Task 4
def make_student(name, score, group=""):
    """Return a student dictionary; include group only when provided."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student


print(make_student("Kamran", 61, "CE-101"))

students = []
while True:
    name = input("Name (quit to stop): ")
    if name.lower() == "quit":
        break
    score = int(input("Score: "))
    students.append(make_student(name, score))

for student in students:
    print(student["name"] + ": " + str(student["score"]))


# Task 5 (functions are in utils.py)
scores = [70, 95, 88, 100]
print(with_bonus(scores, 10))
print(scores)
add_bonus(scores[:], 10)
print(scores)
add_bonus(scores, 10)
print(scores)


# Task 6 (functions are in utils.py)
print(average(70, 80, 90))
print(average(100))
print(average())
print(make_course("CE101", title="Fundamentals of Programming", credits=6))


# Task 7: import examples
import utils
from utils import average
from utils import build_username as make_user
import utils as u

print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))

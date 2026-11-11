import utils
from utils import average
from utils import build_username as make_user
import utils as u


def print_student_card(name, group, year):
    """Print a student card."""
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))


def make_student(name, score, group=""):
    """Return a dictionary describing a student."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student


#Tapshiriq 1
print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")


#Tapshiriq 4
print(make_student("Kamran", 61, "CE-101"))

students = []
while True:
    name = input("Name (quit to stop): ")
    if name == "quit":
        break
    score = int(input("Score: "))
    students.append(make_student(name, score))

for student in students:
    print(student["name"] + ": " + str(student["score"]))

#Tapshiriq 5
scores = [70, 95, 88, 100]
print(utils.with_bonus(scores, 10))
print(scores)
utils.add_bonus(scores[:], 10)
print(scores)
utils.add_bonus(scores, 10)
print(scores)

#Tapshiriq 6
print(average(70, 80, 90))
print(average(100))
print(average())
print(utils.make_course("CE101", title="Fundamentals of Programming", credits=6))

#Tapshiriq 7
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))
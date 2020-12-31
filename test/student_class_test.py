from services import StudentService
from model import IntroToPython, Statistics

student = StudentService()
itp_id = student.register(IntroToPython)
stat_id = student.register(Statistics)

student.start_assignment("Tammy", itp_id)
print("Tammy's Lesson:", student.get_lesson("Tammy"))
print(
    "Tammy's check:",
    student.check_assignment("Tammy", "a = 1 ; b = 'hello'"),
)
print(
    "Tammy's other check:",
    student.check_assignment("Tammy", "a = 1\nb = 'hello'"),
)

print(student.assignment_summary("Tammy"))

student.start_assignment("Tammy", stat_id)
print("Tammy's Lesson:", student.get_lesson("Tammy"))
print("Tammy's check:", student.check_assignment("Tammy", "avg=5.25"))
print(
    "Tammy's other check:",
    student.check_assignment(
        "Tammy", "avg = statistics.mean([1, 5, 18, -3])"
    ),
)

print(student.assignment_summary("Tammy"))

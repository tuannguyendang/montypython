from uuid import uuid4

from services import StudentAssignmentService
from services.abstract import Assignment


class StudentService:
    def __init__(self):
        self.student_graders = {}
        self.assignment_class = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError("Your class does not have the right methods")
        id = uuid4()
        self.assignment_class[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        self.student_graders[student] = StudentAssignmentService(
            student, self.assignment_class[id]
        )

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
                {student}'s attempts at {grader.assignment.__class__.__name__}:

                attempts: {grader.attempts}
                correct: {grader.correct_attempts}

                passed: {grader.correct_attempts > 0}
                """

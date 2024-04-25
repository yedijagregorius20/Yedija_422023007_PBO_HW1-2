from base.User import User
from grade import Grade
from attendance import Attendance

class Professor(User):
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.faculty_id = faculty_id
        self.courses_taught = []  # List of Course objects

    def upload_grades(self, student, course, grade):
        grade_obj = Grade(student._user_id, course.course_id, grade['letter_grade'], grade['numeric_score'])
        student.grades.append(grade_obj)
        print(f"Grade uploaded for {student._name} in {course.name}.")

    def monitor_attendance(self, student, course, date):
        attendance = Attendance(student._user_id, course.course_id, date)
        attendance.record_absence()
        print(f"Attendance recorded for {student._name}.")

    def teach_course(self, course):
        self.courses_taught.append(course)
        print(f"{self._name} now teaching {course.name}.")

    def view_courses_taught(self):
        print(f"Courses taught by {self._name}:")
        for course in self.courses_taught:
            print(f"- {course.name}")


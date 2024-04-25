import datetime

from admin import Admin
from course import Course
from parent import Parent


def main():
    # Create an admin user
    admin = Admin(user_id=1, name="Admin", email="admin@gmail.com", password="admin123")

    # Create users using the admin
    student1 = admin.create_user_account("student", "S01", "Roy", "roy@gmail.com", "roy123", "S101")
    student2 = admin.create_user_account("student", "S02", "Samuel", "samuel@gmail.com", "samuel123", "S102")
    professor1 = admin.create_user_account("professor", "S03", "Pak Leo", "leo@gmail.com", "leo123", "F201")

    # Create courses
    course1 = Course(course_id="C101", name="Pemrograman Berorientasi Objek", description="Learn OOP.")
    course2 = Course(course_id="C102", name="PWL", description="Learn Laravel.")

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course2)

    # Teach courses
    professor1.teach_course(course1)
    professor1.teach_course(course2)

    # Upload grades
    professor1.upload_grades(student1, course1, {"letter_grade": "A", "numeric_score": 95})
    professor1.upload_grades(student2, course2, {"letter_grade": "B", "numeric_score": 85})

    # Monitor attendance
    professor1.monitor_attendance(student1, course1, datetime.datetime.now())

    # View courses taught
    professor1.view_courses_taught()

    # View students enrolled in a course
    course1.view_students_enrolled()

    # View child progress for a parent
    parent = Parent(user_id=301, name="Ortu", email="ortu@example.com", password="ortu123")
    parent.add_child(student1)
    parent.view_child_progress(student1)

    # Track child attendance
    parent.track_child_attendance(student1, course1, datetime.datetime.now())

    # View children
    parent.view_children()

if __name__ == "__main__":
    main()

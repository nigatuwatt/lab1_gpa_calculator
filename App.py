
from students.StudentService import Students
from courses.CourseService import Courses
from results.ResultService import Results
from gradereports.GradeReport import GradeReport

students = Students()
courses = Courses()
results = Results()

def main_menu():
    while True:
        print("\n===== GPA CALCULATOR MENU =====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            students_menu()
        elif choice == "2":
            courses_menu()
        elif choice == "3":
            results_menu()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            print("Exiting program…")
            break
        else:
            print("Invalid choice!")

def students_menu():
    while True:
        print("\n---- Students Menu ----")
        print("1. Register Student")
        print("2. View Students")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            students.register_student()
        elif choice == "2":
            students.list_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def courses_menu():
    while True:
        print("\n---- Courses Menu ----")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            courses.add_course()
        elif choice == "2":
            courses.list_courses()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def results_menu():
    while True:
        print("\n---- Results Menu ----")
        print("1. Record Result")
        print("2. View Results")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            results.add_result(students, courses)

        elif choice == "2":
            results.list_results(students)   # <-- FIXED HERE

        elif choice == "3":
            break

        else:
            print("❌ Invalid choice. Try again.")


def report_menu():
    grade_report = GradeReport(students, courses, results)
    grade_report.calculate_gpa()

if __name__ == "__main__":
    main_menu()

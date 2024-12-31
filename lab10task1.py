import json

try:
    with open('Task01.json', 'r') as file:
        courses_data = json.load(file)
except FileNotFoundError:
    courses_data = {}

def display_menu():
    print("\nMenu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("1) List of  All")
    print("e) Edit")
    print("q) Quit")

def add_course():
    course_code = input("Enter course code : ")
    course_title = input("Enter course title: ")
    course_credits = int(input("Enter credits hour.....: "))
    semester = int(input("Enter default semester: "))
    course_type = input("Enter course type (core or elective): ")

    if len(course_code) > 8 or len(course_title) > 40 or type(course_credits) != int or type(semester) != int:
        print("There is an error")

    courses_data[course_code] = {
        'title': course_title,
        'credits': course_credits,
        'semester': semester,
        'type': course_type
    }
    save_data()

def search_course():
    c = input("Enter course code you want to search: ")
    if c in courses_data:
        print("Course found:")
        print(courses_data[c])
    else:
        print("Course not found.")

def delete_course():
    c = input("Enter course code you want to delete: ")
    if c in courses_data:
        del courses_data[c]
        print("Course deleted.")
        save_data()
    else:
        print("Course not found.")

def list_all_courses():
    if not courses_data:
        print("No courses available.")
    else:
        print("List of all courses:")
        for code, course in courses_data.items():
            print(f"{code}: {course['title']}")

def edit_course():
    code = input("Enter course code to edit: ")
    if code in courses_data:
        print("Enter new details:")
        add_course()
    else:
        print("Course not found.")

def save_data():
    with open('Task01.json', 'w') as file:
        json.dump(courses_data, file)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == 'a':
            add_course()
        elif choice == 's':
            search_course()
        elif choice == 'd':
            delete_course()
        elif choice == '1':
            list_all_courses()
        elif choice == 'e':
            edit_course()
        elif choice == 'q':
            save_data()
            print("Exiting program.")
            break
        else:
            print("Invalid input. Choose from the mentioned options.")

if __name__ == "__main__":
    main()

all_students = []

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))
        student_name = input("Name: ")
        student_age = int(input("Age: "))
        student_grade = input("Grade: ")
        student_dob = input("Date of Birth (YYYY-MM-DD): ")

        subjects = set(
            subject.strip()
            for subject in input("Subjects (comma-separated): ").split(",")
        )

        student = {
            "Student_Info": (student_id, student_dob),
            "Student_Name": student_name,
            "Student_Age": student_age,
            "Student_Grade": student_grade,
            "Student_Subject": subjects
        }

        all_students.append(student)

        print("\nStudent Added Successfully!\n")

    elif choice == 2:
        print("\n--- Display All Students ---")

        for data in all_students:
            print(f"Student ID: {data['Student_Info'][0]}")
            print(f"Name: {data['Student_Name']}")
            print(f"Age: {data['Student_Age']}")
            print(f"Grade: {data['Student_Grade']}")
            print(f"Date of Birth: {data['Student_Info'][1]}")
            print("Subjects:", ", ".join(sorted(data["Student_Subject"])))
            print()

    elif choice == 3:
        user_data = int(input("\nEnter Student ID: "))
        for data in all_students:
            if user_data == data["Student_Info"][0]:
                print("1. Update ID")
                print("2. Update Name")
                print("3. Update Age")
                print("4. Update Grade")
                print("5. Update Subjects")

                update_choice = int(input("Enter your choice: "))

                if update_choice == 1:
                    data["Student_Info"] = (
                        int(input("New ID: ")),
                        data["Student_Info"][1]
                    )

                elif update_choice == 2:
                    data["Student_Name"] = input("New Name: ")

                elif update_choice == 3:
                    data["Student_Age"] = int(input("New Age: "))

                elif update_choice == 4:
                    data["Student_Grade"] = input("New Grade: ")

                elif update_choice == 5:
                    data["Student_Subject"] = set(
                        subject.strip()
                        for subject in input(
                            "New Subjects (comma-separated): "
                        ).split(",")
                    )

                else:
                    print("Invalid update choice!")
                    break

                print("\nUpdated Successfully!\n")
                break
        else:
            print("\nStudent not found!\n")

    elif choice == 4:
        user_data = int(input("Enter Student ID: "))

        for data in all_students:
            if user_data == data["Student_Info"][0]:
                del all_students[all_students.index(data)]
                print("\nData Deleted Successfully!\n")
                break
        else:
            print("\nStudent not found!\n")

    elif choice == 5:
        all_subjects = set()

        for data in all_students:
            all_subjects.update(data["Student_Subject"])

        print("\nSubjects Offered:", sorted(all_subjects))
        print()

    elif choice == 6:
        print("Thank you for using the Student Data Organizer!")
        print("Exiting the program. Goodbye!")
        break

    else:
        print("\nPlease enter a valid choice!\n")
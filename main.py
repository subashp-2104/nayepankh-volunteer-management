import csv
import os

FILE_NAME = "volunteers.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Phone", "Email", "Skill"])


def add_volunteer():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    skill = input("Enter Skill: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, phone, email, skill])

    print("\nVolunteer Registered Successfully!\n")


def view_volunteers():
    print("\n===== Volunteer Records =====")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def search_volunteer():
    keyword = input("\nEnter Volunteer Name: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if keyword in row[0].lower():
                print(row)
                found = True

    if not found:
        print("Volunteer Not Found")


def filter_by_skill():
    skill = input("\nEnter Skill: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 4 and skill in row[4].lower():
                print(row)
                found = True

    if not found:
        print("No Volunteers Found")


def generate_report():
    count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            count += 1

    print("\n===== REPORT =====")
    print("Total Volunteers:", count)


while True:

    print("\n====== NAYEPANKH FOUNDATION ======")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Filter By Skill")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_volunteer()

    elif choice == "2":
        view_volunteers()

    elif choice == "3":
        search_volunteer()

    elif choice == "4":
        filter_by_skill()

    elif choice == "5":
        generate_report()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

print("Name: Elena Dementieva")
print("Class: Information Systems 25 A")
print("NIM: 2509116008")
print("Mini Project 1 - Schedule Management System Cougar Basketball Club")
print("="*80)

from datetime import datetime
from prettytable import PrettyTable
from pwinput import pwinput

# ===== Validation Functions =====
def date_valid(s):
    try:
        datetime.strptime(s, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def time_valid(s):
    try:
        a, b = s.split("-")
        start = datetime.strptime(a.strip(), "%H:%M")
        end = datetime.strptime(b.strip(), "%H:%M")
        return start < end
    except Exception:
        return False

# ===== Initial Schedule =====
Schedule = [
    ("15-09-2025","17:00-18:00","Physical Exercise","PKK field"),
    ("16-09-2025","16:30-18:00","Skill Training","Youth and Sports Agency field"),
    ("17-09-2025","17:00-20:00","Fun game match","Youth and Sports Agency field"),
    ("18-09-2025","16:30-18:00","Physical Exercise","Gor Kadrie Oening"),
    ("19-09-2025","17:00-19:00","Skill Training","Perbama field"),
]

# ===== Display Schedule =====
def show():
    table = PrettyTable()
    table.field_names = ["No", "Date", "Time", "Activity", "Location"]
    for i, (tgl, wkt, keg, lok) in enumerate(Schedule, start=1):
        table.add_row([i, tgl, wkt, keg, lok])
    print(table)

# ===== Change Schedule =====
def change():
    show()
    try:
        no = int(input("Enter schedule number to change: "))
        if 1 <= no <= len(Schedule):
            tgl = input("Enter new date (DD-MM-YYYY): ")
            if not date_valid(tgl):
                print("Invalid date format!")
                return
            wkt = input("Enter new time (HH:MM-HH:MM): ")
            if not time_valid(wkt):
                print("Invalid time format!")
                return
            keg = input("Enter new activity: ")
            lok = input("Enter new location: ")
            Schedule[no-1] = (tgl, wkt, keg, lok)
            print("\nSchedule updated successfully!")
        else:
            print("Invalid schedule number.")
    except ValueError:
        print("Input must be a number.")

# ===== Add Schedule =====
def create():
    tgl = input("Enter date (DD-MM-YYYY): ")
    if not date_valid(tgl):
        print("Invalid date format!")
        return
    wkt = input("Enter time (HH:MM-HH:MM): ")
    if not time_valid(wkt):
        print("Invalid time format!")
        return
    keg = input("Enter activity: ")
    lok = input("Enter location: ")
    Schedule.append((tgl, wkt, keg, lok))
    print("\nNew schedule added successfully!")

# ===== Delete Schedule =====
def delete():
    show()
    try:
        no = int(input("Enter schedule number to delete: "))
        if 1 <= no <= len(Schedule):
            Schedule.pop(no-1)
            print("\nSchedule deleted successfully!")
        else:
            print("Invalid schedule number.")
    except ValueError:
        print("Input must be a number.")

# ===== Users and Roles =====
user = {
    "Admin": {"Password": "admin123", "Role": "Admin"},
    "Coach": {"Password": "coach456", "Role": "Coach"},
    "Athlete": {"Password": "athlete789", "Role": "Athlete"},
}

# Function For Admin
def menu_admin():
    while True:
        print("\n===== Schedule Management System Cougar Basketball Club =====")
        print("1. View Schedule")
        print("2. Change Schedule")
        print("3. Add Schedule")
        print("4. Delete Schedule")
        print("5. Exit")
        try :
            Choose = int(input("Choose Menu: "))
            if Choose == 1:
                show()
            elif Choose == 2:
                change()
            elif Choose == 3:
                create()
            elif Choose == 4:
                delete()
            elif Choose == 5:
                print("program completed, thank you for using the cougar basketball club schedule management system")
                break
            else:
                print("Invalid!")
        except ValueError :
            print("Invalid!")

# Function For Coach
def menu_Coach():
    while True:
        print("\n===== Schedule Management System Cougar Basketball Club =====")
        print("1. View Schedule")
        print("2. Add Schedule")
        print("3. Exit")
        try :
            Choose = int(input("Choose Menu: "))
            if Choose == 1:
                show()
            elif Choose == 2:
                create()
            elif Choose == 3:
                print("program completed, thank you for using the cougar basketball club schedule management system")
                break
            else:
                print("Invalid!")
        except ValueError :
            print("Invalid!")

# Function for Athlete
def menu_athlete():
    while True:
        print("\n===== Schedule Management System Cougar Basketball Club =====")
        print("1. View Schedule")
        print("2. Exit")
        try :
            Choose = int(input("Choose Menu: "))
            if Choose == 1:
                show()
            elif Choose == 2:
                print("program completed, thank you for using the cougar basketball club schedule management system")
                break
            else:
                print("Invalid!")
        except ValueError :
            print("Invalid!")


# ===== Login =====
def login():
    print("\n=== LOGIN ===")
    while True: 
        username = input("Username: ")
        password = pwinput("Password: ")
        if username in user and password == user[username]["Password"]:
            print(f"\nLogin successful!! WELCOME TO COUGAR BASKETBALL {role}.")
            return user[username]["Role"]
        else:
            print("\nLogin failed!! Wrong username or password!.")

while True:
    print("\n===== Schedule Management System Cougar Basketball Club =====")
    print("1. Admin")
    print("2. Coach")
    print("3. Athlete")
    print("4. Exit")

    try :
        role = int(input("Choose Role: "))
        if role == 1:
            login()
            menu_admin()
            break
        elif role == 2:
            login()
            menu_Coach()
            break
        elif role == 3:
            login()
            menu_athlete()
            break
        elif role == 4:
            print("program completed, thank you for using the cougar basketball club schedule management system")
            break
        else:
            print("Invalid!")
    except ValueError :
        print("Invalid")


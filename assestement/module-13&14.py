attendanceData = {}

# ---------------- Student Management ----------------
def add_student():
    print("***** Add New Student *****")
    roll = input("Enter Roll Number: ")
    if roll in attendanceData:
        print(" Student already exists.")
    else:
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        attendanceData[roll] = {"Name": name, "Course": course, "Attendance": {}}
        print(" Student added successfully.")

def view_students():
    print("******* Student List ***********")
    if not attendanceData:
        print("No students found.")
    else:
        for roll, details in attendanceData.items():
            print(f"Roll: {roll}, Name: {details['Name']}, Course: {details['Course']}")

# ---------------- Attendance Management ----------------
def mark_attendance():
    print("********* ATTENDANCE MARKING **********")
    roll = input("Enter Roll Number: ")
    if roll not in attendanceData:
        print(" Student not found. Please add first.")
        return
    
    date = input("Enter Date (YYYY-MM-DD): ")
    if date in attendanceData[roll]["Attendance"]:
        print(" Attendance already marked for this date.")
    else:
        status = input("Enter Attendance(P=Present, A=Absent): ").upper()
        if status not in ["P", "A"]:
            print("Invalid status! Use P or A.")
        else:
            attendanceData[roll]["Attendance"][date] = status
            print(f" Attendance marked for {attendanceData[roll]['Name']} on {date} as {status}")

# ---------------- Reports ----------------
def student_report():
    roll = input("Enter Roll Number: ")
    if roll not in attendanceData:
        print(" Student not found.")
        return
    
    student = attendanceData[roll]
    total_days = len(student["Attendance"])
    present_days = sum(1 for d in student["Attendance"].values() if d == "P")
    absent_days = total_days - present_days
    attendance_pct = (present_days / total_days * 100) if total_days > 0 else 0

    print(f"\n Report for {student['Name']} (Roll: {roll}, Course: {student['Course']})")
    print(f"   Total Days: {total_days}")
    print(f"   Present: {present_days}")
    print(f"   Absent: {absent_days}")
    print(f"   Attendance %: {attendance_pct:.2f}%")
    if attendance_pct < 75:
        print("⚠ Defaulter (Below 75%)")

def class_report():
    print("******* Full Class Report ***********")
    for roll, student in attendanceData.items():
        total_days = len(student["Attendance"])
        present_days = sum(1 for d in student["Attendance"].values() if d == "P")
        absent_days = total_days - present_days
        attendance_pct = (present_days / total_days * 100) if total_days > 0 else 0

        print(f"\n {student['Name']} (Roll: {roll}, Course: {student['Course']})")
        print(f"   Total Days: {total_days}, Present: {present_days}, Absent: {absent_days}, %: {attendance_pct:.2f}")
        if attendance_pct < 75:
            print("⚠ Defaulter")

# ---------------- Main Menu ----------------
def student_management():
    s_cont = 'y'
    while s_cont != 'n':
        print("********* STUDENT MANAGEMENT **********")

        print("""
                1 : Add New Student
                2 : View Students
              """)
        s_choice = int(input("Enter your choice: "))

        if s_choice == 1:
            add_student()
        elif s_choice == 2:
            view_students()
        else:
            print("Invalid choice")

        s_cont = input("Do you want to continue with Student Management? (y/n): ")

def attendance_marking():
    a_cont = 'y'
    while a_cont != 'n':
        mark_attendance()
        a_cont = input("Do you want to continue with Attendance Marking? (y/n): ")

def reports():
    r_cont = 'y'
    while r_cont != 'n':
        print("********* REPORTS **********")
        print("""
                1 : Individual Student Report
                2 : Full Class Report
              """)
        r_choice = int(input("Enter your choice: "))

        if r_choice == 1:
            student_report()
        elif r_choice == 2:
            class_report()
        else:
            print("Invalid choice")

        r_cont = input("Do you want to continue with Reports? (y/n): ")

# ---------------- EduTrack App ----------------
def coaching():
    cont = 'y'
    while cont != 'n':
        print("""
        **************** Welcome to EduTrack ****************
            Choose Operation:
            1 : Student Management
            2 : Attendance Marking
            3 : Reports
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_management()
        elif choice == 2:
            attendance_marking()
        elif choice == 3:
            reports()
        else:
            print("Invalid choice")

        cont = input("Do you want to continue with EduTrack? (y/n): ")

coaching()
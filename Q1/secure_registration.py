# PSHS Secure Club Registration System

def register_student():
    # Predefined valid choices
    VALID_SECTIONS = ["Dahlia", "dahlia", "Ilang-Ilang", "ilang-ilang", "Sampaguita", "sampaguita", "Rosal", "rosal", "Emerald", "emerald", "Sapphire", "sapphire", "Jade", "jade", "Diamond", "diamond", "Magnesium", "magnesium", "Silicon", "Platinum", "Beryllium", "Electron", "Gluon", "Graviton", "Photon", "Biology", "Chemistry", "Physics", "Bio-Chemistry", "Chemistry", "Physics"]
    VALID_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
    VALID_ATTENDANCE = ["Present", "Absent", "Late"]

    # 1. Student Name Input & Validation
    name = input("Enter Student Name: ").strip()
    if not name:
        print("Error: Student name is required.")
        return

    # 2. Section Input & Validation
    section = input("Enter Section: ").strip()
    if section not in VALID_SECTIONS:
        print("Error: Please select a valid section.")
        return

    # 3. Club Choice Input & Validation
    club = input("Enter Club Choice: ").strip()
    if club not in VALID_CLUBS:
        print("Error: Please choose a valid club.")
        return

    # 4. School Email Input & Validation
    email = input("Enter School Email: ").strip()
    if "@" not in email or "." not in email:
        print("Error: Invalid email address format.")
        return

    # 5. Attendance Status Input & Validation
    attendance = input("Enter Attendance Status (Present/Absent/Late): ").strip()
    if attendance not in VALID_ATTENDANCE:
        print("Error: Invalid attendance status.")
        return

    # Success Output
    print("\nREGISTRATION ACCEPTED")
    print(f"Student: {name}")
    print(f"Section: {section}")
    print(f"Club: {club}")
    print(f"Email: {email}")
    print(f"Attendance: {attendance}")

if __name__ == "__main__":
    register_student()


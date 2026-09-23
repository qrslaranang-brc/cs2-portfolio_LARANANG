# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** [Qien Rafhael S. Laranang{
**Section:** [8 - Dahlia]
**Quarter:** 1

## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct, expected, and appropriate input.

# Part A - Cybersecurity Threat Analysis
## Assigned Case
**Case Number:** Case 1
**Case Title:** Fake Login Alert
> A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

### 1. What cybersecurity threat is shown?
The threat present is **Phishing** (specifically Credential Harvesting). The message attempts to trick the user into revealing sensitive login details by creating false urgency.

### 2. What warning signs make the situation suspicious?
* **Urgency/Fear Tactics:** Threats of immediate account suspension/disabling if action isn't taken immediately.
* **Unsolicited Request for Credentials:** Asking the user to click an external link to re-enter sensitive account details.
* **External/Unverified Link:** The link likely leads to an unofficial domain mimicking the PSHS login portal.

### 3. What may be affected?
- [x] Data
- [x] Account
- [ ] Application
- [ ] Device
- [ ] Network
- [ ] Financial information

> **Explanation:** By capturing the user's username and password, the attacker gains direct access to the student's school account, exposing personal school data, emails, and internal systems connected to that account.

### 4. What information could be exposed or misused?
* The student's username, email, and account password.
* Private emails, academic records, and personal documents stored in the school Google Workspace/portal.
* Account access could be hijacked to send spam or additional phishing emails to other PSHS students and faculty.

### 5. What should the user do to reduce the risk?
* **Do not click** the link or enter any credentials.
* Verify the sender's actual email address.
* Directly navigate to the official school portal via bookmarked URLs or official PSHS channels instead of email links.
* Report the suspicious message to the school’s IT administrator or system security team.

---

# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information. Determine whether each item is really necessary.

| Information | Collect / Do Not Collect | Reason |
| :--- | :--- | :--- |
| **Student Name** | COLLECT | Needed to identify who is joining the club. |
| **Section** | COLLECT | Needed to organize student listings and verify eligibility. |
| **Club Choice** | COLLECT | Essential to assign the student to their desired club. |
| **School Email** | COLLECT | Necessary for sending club updates and verifying school membership. |
| **Attendance Status** | COLLECT | Required to track registration or meeting participation. |
| **Password** | DO NOT COLLECT | Completely unnecessary for a registration form; poses severe security risk. |
| **OTP** | DO NOT COLLECT | Irrelevant for static registration and compromises multi-factor authentication security. |
| **Home Address** | DO NOT COLLECT | Excessive personal information not required for club participation. |
| **Parent Bank Account** | DO NOT COLLECT | Financial data is completely irrelevant and creates a severe financial privacy/data risk. |

## Privacy Question
### Why is it safer to collect only information that the program actually needs?
Collecting only necessary information follows the principle of **Data Minimization**. It reduces exposure to security risks; if a database is breached or compromised, sensitive details like passwords, addresses, or banking information cannot be stolen if they were never collected in the first place.

---

# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Student Name** | Non-empty string (e.g., "Maria Santos") | Anonymous or empty submissions breaking records. | `[blank]` | Check if string is non-empty after stripping whitespace. | `Student name is required.` |
| **Section** | Pre-approved section name (e.g., "Dahlia") | Out-of-scope sections or rogue inputs causing sorting errors. | `Rose` | Check if input exists in valid section list. | `Please select a valid section.` |
| **Club Choice** | Pre-approved club (e.g., "Programming") | Invalid club choices overloading non-existent clubs. | `Gaming` | Check if input exists in fixed club list. | `Please choose a valid club.` |
| **School Email** | Email string containing `@` and `.` | Invalid contact info preventing communication. | `studentpshs.edu.ph` | Ensure string contains both `@` and `.` characters. | `Invalid email address format.` |
| **Attendance Status** | "Present", "Absent", or "Late" | Inconsistent status values corrupting attendance records. | `Excused` | Check if input matches allowed status values. | `Invalid attendance status.` |

## Secure Data Capture Questions
### 1. What should your program accept?
Inputs that exactly match expected values, non-empty fields, valid email structures containing both `@` and `.`, and specific choices from predefined lists (e.g., valid sections, approved clubs, and valid attendance statuses).

### 2. What should your program reject?
Blank or whitespace-only inputs, non-existent clubs, unapproved section names, emails without `@` or `.`, and any unrecognized attendance status values.

### 3. How do your validation rules help reduce incorrect or unsafe input?
They enforce strict boundaries on input before processing occurs, preventing empty data entries, malformed strings, and unexpected values that could disrupt system logic or lead to corrupted records.

---

# Part D - Secure Program Implementation

## Program
Created a simple **PSHS Club Registration System** validating all inputs prior to processing.

## Source Code File
[secure_registration.py](secure_registration.py)

## Final Code
```python
# PSHS Secure Club Registration System

def register_student():
    # Predefined valid choices
    VALID_SECTIONS = ["Dahlia", "Adelfa", "Camia", "Ilang-Ilang"]
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

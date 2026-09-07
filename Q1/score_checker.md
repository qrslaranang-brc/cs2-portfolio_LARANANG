markdown
# Clean Decision Code Makeover: Student Score Checker
**Name:** [Qien Rafhael S. Laranang]
**Section:** [8 - Dahlia]

## Activity Overview
in this activity, I improved a student score checker program by applying proper coding standards and selection structures. The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score Classification | Result |
|—--:|——-|
|90-100 | outstanding |
|80-89 |  Very Satisfactory
|75-79 | Satisfactory
|0-74 | Needs Improvement

Scored below 0 or above 100 are considered invalid.

---

# Part 1 - Analyze the Logic

## Input
**What information does the program need?**
> The program needs an integer value representing a student score.

## Valid Range
* **Minimum valid score:** 0
* **Maximum valid score:** 100

## Possible Outputs
1. Invalid Score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

## Boundary Condition
**What condition will you use to determine whether the score is valid?**
> `student_score < 0 or student_score > 100`

## Multiple Decision Paths
**Explain how the program decides which classification should be displayed.**
> The program uses an `if-elif-else` chain. It first checks if the score is out of bounds. If valid, it evaluates the score from highest to lowest threshold (>=90, >=80, >=75) to assign the correct classification.

---

# Part 2 - Program Code

```python
# Student Score Checker
# Program to validate and classify student test scores

# Ask the user to enter a student score
student_score = int(input("Enter student score: "))

# Range validation: Check if score is outside 0 to 100
if student_score < 0 or student_score > 100:
    print("Invalid Score.")

# Grade classification for valid scores
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")

---

# Part 3 - Reflection Questions

## 1. How does boundary checking prevent invalid data from affecting the output?
> Boundary checking ensures that inputs outside the allowed range (0 to 100) are flagged immediately before any grade calculations occur. This prevents impossible grades from producing misleading results.

## 2. Why is the order of conditions in an `if-elif-else` structure important?
> Python evaluates conditions sequentially from top to bottom. Checking higher thresholds first ensures that scores fall into the highest bracket they qualify for without overlapping lower conditions incorrectly.



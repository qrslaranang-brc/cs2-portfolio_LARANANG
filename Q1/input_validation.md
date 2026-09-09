# Input Validation and Output Verification

**Activity:** PSHS Workshop Registration Validator[span_1](start_span)[span_1](end_span)  
**Name:** [Qien Rafhael S. Laranang]  
**Section:** [Dahlia]  
**Quarter:** 1[span_2](start_span)[span_2](end_span)  

---

## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration system[span_3](start_span)[span_3](end_span). The program checks whether user input satisfies specific requirements before accepting the registration[span_4](start_span)[span_4](end_span). The program validates student name, age, grade level, email address, and registration code[span_5](start_span)[span_5](end_span).

---

## Part A - Validation Requirements

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Text / String | Presence | `""` (blank) | Must not be empty | Student name is required. |
| Age | Whole Number (11–18) | Data Type & Range | `"fourteen"`, `25` | Must be an integer from 11 to 18 | Age must be a number. / Age must be from 11 to 18. |
| Grade Level | Whole Number (7–12) | Acceptable Value | `13` | Must be 7, 8, 9, 10, 11, or 12 | Invalid grade level. |
| Email Address | Text with `@` | Simple Pattern | `studentpshs.edu.ph` | Must contain `@` | Invalid email format. |
| Registration Code | 6-character text | Length | `A123` | Must be exactly 6 characters | The registration code must contain exactly 6 characters. |

### Validation Questions

#### 1. Why should the student name not be blank?
> A student name should not be blank to ensure that every registration record is attached to an identifiable individual and to prevent empty or anonymous entries in the database.

#### 2. Why should age be checked for both data type and range?
> Data type validation ensures the program can parse the input as an integer without crashing, while range validation guarantees that the student meets the eligible PSHS age requirement (11 to 18 years old).

#### 3. Why should grade level only accept specific values?
> Grade level must be restricted to 7–12 to align with the high school grade levels offered at PSHS and prevent invalid inputs such as elementary grades or non-existent high school levels.

#### 4. What format requirements did you use for the email address?
> A simple pattern check was used to verify that the string contains the `@` symbol, ensuring the minimum structure of a valid email address.

#### 5. What length requirement did you use for the registration code?
> The registration code requires an exact length of 6 characters to match the standardized format issued for the workshop.

---

## Part B - Program Design

### Pseudocode
```text
START
  INPUT name
  INPUT age_input
  INPUT grade_input
  INPUT email
  INPUT reg_code

  IF name is empty THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Student name is required."
  ELSE IF age_input is not an integer THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Age must be a number."
  ELSE IF age < 11 OR age > 18 THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Age must be from 11 to 18."
  ELSE IF grade_input is not an integer THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Invalid grade level."
  ELSE IF grade NOT IN [7, 8, 9, 10, 11, 12] THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Invalid grade level."
  ELSE IF email does not contain "@" THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "Invalid email format."
  ELSE IF length of reg_code != 6 THEN
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT "The registration code must contain exactly 6 characters."
  ELSE
    PRINT "REGISTRATION ACCEPTED"
    PRINT name, age, grade, email, reg_code
  ENDIF
END


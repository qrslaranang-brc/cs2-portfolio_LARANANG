student_score = int(input("Enter student score: "))
if student_score < 0 or student_score > 100:
  print("Invalid Score.")
elif student_score >= 90:
  print("outstanding")
elif student_score >=80:
  print("very satisfactory")
elif student_score >=75:
  print("satisfactory")
else:
  print("needs improvement")

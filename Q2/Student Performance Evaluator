def calculate_average(score1, score2, score3):   
  return (score1 + score2 + score3) / 3

def get_performance(average):
    if average >= 85:
      return "Mastery"
    elif average >= 70:
      return "Developing"
    else:
      return "Needs Review"

def is_eligible(average, completed_tasks):
        if average >= 85 and completed_tasks >= 3:
          return True
        else:
          return False

score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))
          
avg = calculate_average(score1, score2, score3)
perf = get_performance(avg)
elig = is_eligible(avg, completed_tasks)

print(f"Average: {avg:.2f}")
print(f"Performance: {perf}")
print(f"Eligible for Challenge: {elig}")

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score < 70:
        student_grades[student] = "Fail"
    elif 70 < score < 80:
        student_grades[student] = "Acceptable"
    elif 80 < score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif 90 < score < 100:
        student_grades[student] = "Outstanding"
        # 🚨 Don't change the code below 👇
print(student_grades)

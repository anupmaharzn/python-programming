
score = float (input('Enter the students score:'))

if score >=90:
    grade = 'A'
elif 80<= score < 90:
    grade = 'B'
elif 70<= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"the student's grade is: {grade}")
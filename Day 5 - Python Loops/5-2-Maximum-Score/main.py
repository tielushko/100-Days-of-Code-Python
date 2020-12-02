# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max = student_scores[0]

for student in student_scores:
  if student >= max:
    max = student

print(f"The maximum score in the class is {max}")



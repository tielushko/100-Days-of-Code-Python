#Write your code below this row 👇
sum_evens = 0

for i in range(1, 101):
  if i % 2 == 0:
    sum_evens += i

sum_evens2 = 0
#alternative solution
for i in range(2,101,2):
  sum_evens2 += i

print(sum_evens)
print(sum_evens2)

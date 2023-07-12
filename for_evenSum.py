sum = 0
for i in range(101):
    if i % 2 == 1 :
        continue
    sum += i
print("짝수의 합 :", sum)
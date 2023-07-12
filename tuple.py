t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t5[0])
print(t5[2][1])

# indexing
t1 = (1, 2, 'a', 'b')
print(t1[0])

# slicing
t1 = (1, 2, 'a', 'b')
print(t1[1:3])

t1 = (1, 2, 'a', 'b', 'c')
print(t1[1:])
print(t1[:3])
print(t1[-2:])
print(len(t1))

for i in range(len(t1)):
    print(t1[i])
    print("안녕하세요")





t2 = (1,2,'a','b','c')
t3 = (4,5,'d','e','f')

# tuple 더하기
t4 = t2 + t3
print(t4)

# tuple 곱하기
t5 = t2 * 3
print(t5)



print(tuple([1,2,3]))
print(list[(1,2,3)])
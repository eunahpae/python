a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


# 중첩된 리스트에서 슬라이싱하기
f = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(f[2:5])
print(f[3][:2])


# 리스트 더하기
g = [1, 2, 3]
h = [4, 5, 6]
print(g + h)

# 리스트 반복하기
k = [1, 2, 3]
print(k * 3)

# 리스트 길이 구하기
m = [1, 2, 3]
print(len(m))


# 리스트의 값 수정
n = [1, 2, 3]
n[2] = 4
print(n)

# del 함수를 사용해 리스트 요소 삭제
p = [1, 2, 3]
del p[1]
print(p)

# 리스트 요소 제거 - remove
q = [1, 2, 3, 1, 2, 3]
q.remove(3)
print(q)
q.remove(3)
print(q)

# 리스트 요소 끄집어 내서 삭제 - pop
# pop() 빈칸으로 넣으면 마지막 요소 삭제, 뒤에 숫자를 넣을때는 인덱싱으로 적용삭제.
r = [1, 2, 3]
print(r.pop())

# 리스트에 요소 추가하기 - append / 리스트 맨 뒤에 추가됨
s = [1, 2, 3]
s.append(4)
print(s)

# 리스트에 요소 삽입 - insert / 원하는 인덱싱 위치에 추가
t = [1, 2, 3]
t.insert(0, 4)
print(t)

# 리스트에 요소 삽입 - extend([])
nums = [1,2,3]
nums.extend(['a','b'])
print(nums)

# sort(*, key=None, reverse=False) / 여기서 reverse=True사용시 정렬 후 뒤집기
u = [5, 2, 3, 1, 4]
u.sort()
x = sorted(['f','b'])
print(u)
print(x)

u.sort(reverse=True)
y = sorted(x, reverse=True)
print(u)
print(y)


# key
''' 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
 key 값을 기준으로 정렬되고 기본값은 오름차순이다 '''
str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))
print(sorted(str_list, key=len, reverse=True))


# 리스트 순서 뒤집기 = reverse()
z = ['a', 'g', 1, 3, 2, 'd']
z.reverse()
print(z)

# 인덱스 반환
aa = [ 1, 2, 3, 'a', 'a']
print(aa.index(2))

# 원하는 요소의 개수 찾기 - count()
print(aa.count('a'))

# 리스트 요소 전부 삭제 - clear
aa.clear()
print(aa)




#  추가하기 연습
aa.append(5)
print(aa)

aa.extend([3,4])
print(aa)

aa.append([3,4])
print(aa)

aa.insert(0,[3,4])
print(aa)
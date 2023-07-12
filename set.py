# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).


s1 = set([1, 1, 1, 1, 1, 1, 1, 2, 3])
print(s1)

s2 = set("Hello World")
print(s2)

s3 = list("Hello World")
print(s3)

s4 = tuple("Hello World")
print(s4)


# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#  교집합
print(s1 & s2)
print(s1.intersection(s2))

s3 = s1 & s2
s4 = s1.intersection(s2)
print(s3)
print(s4.intersection(s3))

# 합집합
s3 = s1 | s2
print(s3)
s4 = s1.union(s2)
print(s4)


# 차집합
s3 = s1 - s2
print(s3)
print(s1.difference(s2))

s4 = s2 - s1
print(s4)
print(s2.difference(s1))



# 집합 자료형 관련 함수 -이미 만들어진 set 자료형에 값을 추가할 수 있다.

# 값 1개 추가하기 - add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
s1.update([1, 2, 4, 5, 6])
print(s1)




# 특정 값 제거하기 - remove / 인덱싱 아니고 삭제원하는 요소값을 직접 입력
s1 = set([1, 2, 3])
s1.remove(3)
print(s1)
# [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]

list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 리스트 안에서 for 문 사용하기
list_1 = [num * 3 for num in list]
print(list_1)

# 리스트 안에서 for 문 사용하기 2: if 문 사용 
list_2 = [ num * 3 for num in list if num % 2 == 1 ]
print(list_2)
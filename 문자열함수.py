str = "Hello"

for i in range(0, len(str)):
    print(f'{str[i]}_', end="\n")

str_1= "   Hello World   "
# str_2 = str_1.upper()

# 모든 문자를 대문자로 변경
print(str_1.upper())

# 해당 문자가 전부 대문자인지 bool
print(str_1.isupper())

# 모든 문자를 소문자로 변경
print(str_1.lower())

# 해당 문자가 전부 소문자인지 bool
print(str_1.islower())

# 대문자는 소문자로, 소문자는 대문자로 변경
print(str_1.swapcase())

# 문자 첫 시작을 대문자로 변경
print(str_1.title())

# 해당 요소 개수 확인
print(str_1.count("l"))

# 해당 요소 위치 찾음/ 없어도 에러가 나지않음.
print(str_1.find("W"))

# 해당 요소 위치(인덱스) 찾음 / 없으면 에러발생
print(str_1.index("d"))

# 왼쪽 공백 삭제
print(str_1.lstrip())

# 오른쪽 공백 삭제
print(str_1.rstrip())

# 양쪽 공백 삭제
print(str_1.strip())

# 특정 문자를 원하는 문자로 치화
print(str_1.replace('Hello','Hi,'))

# 문자열을 값으로 구분하여 나눔
a = " Hello Hi 안녕" 
print(a.split(","))
# str.split(sep=None, maxsplit=- 1)

# splitlines()
str = '''안녕하세요.
어서오세요.
반갑습니다.
'''

result=str.splitlines()
print(result)
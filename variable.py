a = 10
b = "Hello"

print(type(a))
print(type(b))

a = True
print(type(a))

c = d = e = 10
f, g, h = 11, 3.14, "hi"

print(c, d, e)
print(f, g, h)
print(c, d, e, f, g, h)

str = "안녕하세요,'배은아'님"
print(str)
str_literal = '''
sdlsdfkl;sdf\n
sldkf;slkdf
lsdkf;lskddfl;'''
print(str_literal)


# 리터럴 표기 방법
name = "배은아"
literal_1="안녕하세요!!" + name + "님"
print(literal_1)

literal_2 = f'안녕하세요!!!  {name}  님' 
print(literal_2)
# 띄어쓰기 하고 싶을 때는 f'띄어쓰기 포함한 전체 내용' 사용

print(3==3.0)

print(3==3 and 3>5)
print(3==3 & 3>5)
print(3==3 or 3>5)

print(not False)

print(not 3>5)
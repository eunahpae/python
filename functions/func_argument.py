#  a,b,c 매개변수
def multiple_add(a,b,c):
    num = a*b+c
    return num

# result = multiple(2,3,4)

a = 2
b = 3
c = 4

#  a,b,c 위치인자로 전달
result=multiple_add(a,b,c)
print(result)

# a,b,c 를 키워드 인자로 전달 /키워드인자로 전달하려면 매개변수명을 그대로 가져와서 값 입력해야함.
# 키워드 인자는 위치를 바꿔도 된다.
result_keywords = multiple_add(c=4,a=2,b=3)
print(result_keywords)

# 섞어쓰고싶다면...위치인자부터 먼저 호출하고 나중에 키워드 인자를 호출한다.
result_keywords_1 = multiple_add(2,3,c=4)
print(result_keywords_1)

# 매개변수 키워드 값을 부여하면 인자값으로 전달 받지 않아도 된다.
def multiple_add_keywords(alpa,beta,gama=100):
    num = alpa*beta+gama
    return num

result_1 = multiple_add_keywords(10,20)
print(result_1)

result_2 = multiple_add_keywords(10,20,500)
print(result_2)

result_3 = multiple_add_keywords(gama=10,alpa=20,beta=5)
print(result_3)

result_4 = multiple_add_keywords(alpa=20,beta=500)
print(result_4)
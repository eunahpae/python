def hello_name(*args):
    print(type(args))
    for name in args:
        print(f'{name}님 안녕하세요!')
    
hello_name("배은아","김연주","김태경")

# 원하는 숫자를 나열하면 다 더하는 함수
def add(*args):
    num = 0
    for i in args:
        num += i
    return num

result=add(1,5,6,7,8,100)
# print(result)

# def input_sum(*args):
#     args = input("원하는 숫자를 , 기준으로 적어주세요.")
#     num = 0
#     for i in args:
#         num += int(i)
#     return num

# data = input_sum()
# print(data)


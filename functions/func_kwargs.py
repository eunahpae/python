def keywords_method(**kwargs):
    print(type(kwargs))
    num = 0
    print(kwargs.values())
    for i in kwargs.values():
        num += i
    return num

result=keywords_method(a=1,b=3,c=5)
print(result)

def name_hello(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # hello = kwargs[]
    # for i in kwargs:
    #     print(type(i))
    #     print(f'{kwargs[i]}님 안녕하세요.')
    for i in kwargs.values():
        print(type(i))
        print(f'{i}님 안녕하세요.')

result=name_hello(a="김태경",b="배은아",c="김연주")
# print(result)
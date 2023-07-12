a = 3
b = 5

def local_variable():
    # a=5
    global a
    b = 4
    a=a+b
    print(a)
    
# print(a)


# def local_variable_error():
#     print(b)

local_variable()






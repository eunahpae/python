# dict {}

# immutable 예 / 키 값에는 문자,숫자,튜플,불린 가능 ( 변경이 불가능한 경우만 가능 )
a = {1: 5, 2: 3}   # int 사용
print(a)

a = {(1,5): 5, (3,3): 3} # tuple사용
print(a)

a = { 3.6: 5, "abc": 3} # float 사용
print(a)

a = { True: 5, "abc": 3} # bool 사용
print(a)


# mutable 예 / 키 값에 셋,딕셔너리,리스트 사용불가 ( 변경이 가능한 것들은 불가)
# a = { {1, 3}: 5, {3,5}: 3}     #set 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'
# a = {[1,3]: 5, [3,5]: 3}     #list 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# a = { {"a":1}: 5, "abc": 3}     #dict 사용 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'dict'


# 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워짐
b = {"a": 1, "a": 2, "b": 3}
print(b)

# 순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있ek.
print(b[("b")])

# keys(), values(), items()
print(b.keys())
print(b.values())
print(b.items())


# dict 만들기
result = dict([('a',1),('b',2),('c',3),('d',4)])
print(result)

# mutable 한 객체이므로 키로 접근하여 값을 변경할 수 있다.
d = {'abc': 3,'def': 2}
d['abc'] = 5
print(d)

# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
d['ghi'] = 999
print(d)

# dict constructor를 통해서 아래와 같이 바로 키와 값을 할당하며 선언할 수 있다
newdict = dict(alice = 5, bob = 20, tony= 15, suzy = 30)
print(newdict)



# dictionary(딕셔너리) 변환
# 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있다.
name_and_ages = [['alice', 5], ['Bob', 13]]
print(dict(name_and_ages))
name_and_ages = [('alice', 5), ('Bob', 13)]
print(dict(name_and_ages))
name_and_ages = (('alice', 5), ('Bob', 13))
print(dict(name_and_ages))
name_and_ages = (['alice', 5], ['Bob', 13])
print(dict(name_and_ages))

# # dictionary(딕셔너리) 복사
# # 얕은 복사(shallow copy) 1
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# b =a.copy()
# b['alice'].append(5)
# print(b)
# print(a)

# # 얕은 복사(shallow copy) 2
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# b = dict(a)
# print(a)
# print(b)
# print(id(a))
# print(id(b))


# dictionary update
# 여러값 수정은 update 메소드를 사용. 키가 없는 값이면 추가
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})
print(a)


# dictionary(딕셔너리) for문
# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됨.
# 순서는 임의적이고,같은 순서를 보장할 수 없다.
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for key in a:
    print(key)

# value값으로 for문을 반복하기 위해서는 values() 를 사용
for val in a.values():
    print(val)
  
# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용
for key, val in a.items():
    print("key = {key}, value={value}".format(key=key,value=val))

key_list= []
values_list = []
for key, val in a.items():
    key_list.append(key)
    values_list.append(val)
print(key_list)
print(values_list)


print(20 in a.values())
print('alice' in a)
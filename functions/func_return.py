def odd_sum():
    num = 0
    for i in range(11):
        if i % 2 == 0:
            continue
        num += i
    print(f'0부터 10까지 홀수의 합은 {num} 입니다.')
    return num
    
    
result = odd_sum()
# print(f'0부터 10까지 홀수의 합은 {result} 입니다.')
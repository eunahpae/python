import math

def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round
a = int(input("반지름의 길이를 적으세요."))
square, round = circle_square_round(a)
print(f'넓이 = {square}, 둘레의 길이 = {round}')
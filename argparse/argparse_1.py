import argparse
import math
import numpy as np

def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round

def parsing_argument():
    parser = argparse.ArgumentParser(description='Process some Argument Parsing',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   
    # positional arguments
    parser.add_argument(
        'title',
        metavar='str',
        type=str,
        help="Write your message at positional arguments."
    )
    # args = parser.parse_args()
    # print(args)
    # print(f'지금 수업은 {args.title}입니다.')

    parser.add_argument(
        'radius',
        metavar='integers',
        type=int,
        help="Write radius od Circle."
    )
    args = parser.parse_args()

    return args

def main():
    args = parsing_argument()
    print('지금 실행하는 코드는 argparse 기초 1 입니다.')
    print(f'옵션으로 받은 반지름 "{args.radius}" 으로 구한 {args.title}는 다음과 같습니다.')
    square, round = circle_square_round(args.radius)
    print(f'넓이 = {square}, 둘레의 길이 = {round}')

main()

# print(args)
# print(f'{args.title}입니다.')
# print(args.radius)

# square, round = circle_square_round(args.radius)
# print(f'넓이 = {square}, 둘레의 길이 = {round}')

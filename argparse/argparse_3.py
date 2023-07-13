import argparse
import math

def quadratic_equation_roots(a,b,c):
    if b**2 - 4*a*c<0:
        print(f'실근이 없습니다.')
    else:
        x = b**2  -4*a*c
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
        
        if b**2 - 4*a*c == 0:
            print(f'방정식의 해는 중근 {x1}입니다.')
        else:
            print(f'x1={x1} or x2={x2}')            

def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round
            
def parsing_argument():
    parser = argparse.ArgumentParser(description='Process some Argument Parsing',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   
    parser.add_argument(
        'title',
        metavar='str',
        type=str,
        help="Write your message at positional arguments."
    )
    
    parser.add_argument(
        'num',
        metavar='integers',
        nargs='+',
        type=float,
        help="이차항의 개수를 정할 숫자"
    ) 

    args = parser.parse_args()
    print(args)
    return args
    
def main():    
    args = parsing_argument()
    if args.title == "1":
        square, round = circle_square_round(args.num[0])
        print(f'넓이 = {square}, 둘레의 길이 = {round}')
    elif args.title == "2":
        quadratic_equation_roots(args.num[0],args.num[1],args.num[2])
    
    # print(f'{args.title}는 다음과 같습니다.')
    # quadratic_equation_roots(args.a,args.b,args.c)
    
main()
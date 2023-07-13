import argparse


class Car:
    def __init__(self, door_number, brand, color, speed):
        self.door_number = door_number
        self.brand = brand
        self.color = color
        self.speed = speed

    def __str__(self):
        return f'Car(door_number={self.door_number}, brand={self.brand}, color={self.color})'

    def rapid(self):
        print(
            f'문이 {self.door_number} 개인 {self.brand} 회사의 {self.color} 차가 시속 {self.speed}km로 달립니다.')


def parsing_argument():
    parser = argparse.ArgumentParser(description="Sample for using argparse",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--car',
        metavar='Car option',
        type=str,
        nargs='+',
        help="Write door_number, brand, color, speed ",
        default=["door_number", "brand", "color", "speed"]
    )

    args = parser.parse_args()
    print(args)
    return args


def main():
    args = parsing_argument()
    car = Car(args.car[0], args.car[1], args.car[2], args.car[3])
    car.rapid()


main()

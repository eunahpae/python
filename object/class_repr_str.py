class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    # def __str__(self):
    #     return f'{self.year}-{self.month}-{self.day}'

    # `repr()`과 함께 사용
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
    
obj = Date(2023,7,14)
print(obj)

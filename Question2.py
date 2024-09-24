# Integer to Roman 

roman_num = [
    
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]

num = int(input("Enter an int: "))

result = ""

for symbol, value in roman_num:
    while num >= value:
        result += symbol
        num -= value


print(f"The Roman numeral is {result}")
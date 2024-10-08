# Roman to Integer

roman_to_int_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman = input("Enter a Roman numeral: ")

result = 0
prev_value = 0

for char in reversed(roman):
    value = roman_to_int_map[char]
    
    if value < prev_value:
        result -= value
    else:
        result += value

    prev_value = value

print(f"The integer value of the Roman numeral {roman} is {result}")


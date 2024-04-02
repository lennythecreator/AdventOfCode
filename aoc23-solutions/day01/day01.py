def calculate_calibration_value(line):
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
    
    for char in reversed(line):
        if char.isdigit():
            last_digit= int(char)
            break
    
    if first_digit is not None and last_digit is not None:
        calibration_value = first_digit * 10 + last_digit
        return calibration_value
    else:
        return 0
    


calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

total_calibration_sum = 0

for line in calibration_document:
    calibration_value = calculate_calibration_value(line)
    total_calibration_sum += calibration_value

print("Total sum of calibration values:", total_calibration_sum)

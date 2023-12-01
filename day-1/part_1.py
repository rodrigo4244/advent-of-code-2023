import re

def main ():
    file1 = open('puzzle-input.txt', 'r')
    lines = file1.readlines()

    calibration_numbers = []
    for line in lines:
        all_integers = re.findall(r'\d{1}', line)
        calibration_numbers.append(int(f'{all_integers[0]}{all_integers[-1]}'))

    return sum(calibration_numbers)

print(main())

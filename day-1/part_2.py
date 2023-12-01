import re

map_numbers = {
    'zero': 'z0o',
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

def rreplace(s, old, new, occurrence):
  li = s.rsplit(old, occurrence)
  return new.join(li)

def main ():
    file1 = open('calibration-part-2.txt', 'r')
    # file1 = open('puzzle-input.txt', 'r')
    lines = file1.readlines()

    calibration_numbers = []
    pattern = r'|'.join(map_numbers.keys())
    for line in lines:
        new_line_left_most = re.sub(pattern, lambda match: map_numbers[match.group(0)], line, count=1)
        last_digit_search = list((new_line_left_most.rfind(i), i) for i in map_numbers.keys())
        last_digit_without_negative = list(filter(lambda x: x[0] != -1, last_digit_search))
        last_digit_without_negative.sort(key=lambda tup: tup[0], reverse=True)
        new_line_left_and_right_most = new_line_left_most
        if len(last_digit_without_negative) != 0:
            (last_index, replacer) = last_digit_without_negative[0] 
            new_line_left_and_right_most = rreplace(new_line_left_most, replacer, map_numbers[replacer], last_index)

        all_integers = re.findall(r'\d{1}', new_line_left_and_right_most)
        calibration_numbers.append(int(f'{all_integers[0]}{all_integers[-1]}'))

    return sum(calibration_numbers)

print(main())

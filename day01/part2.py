from input import input_data

def check_string(current_string, letters):
    for letter in letters:
        if current_string.endswith(letter):
            print(f"Current string ends with {letter}")
            return letter
    print(f"Current string doesn't end with any letter")
    return ''

def find_first_last_numbers(line):
    numbers = []
    current_number = ''
    letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    current_string = ''

    for char in line:
        if char.isdigit():
            current_number = char
            numbers.append(int(current_number))
            current_number = ''
        elif char.isalpha():
            current_string += char
            print(f"Current string : {current_string}")
            current_letter = check_string(current_string, letters)
            if current_letter:
                current_number = letters.index(current_letter) + 1
                numbers.append(int(current_number))
                current_number = ''

    print(f"Numbers for {line} : {numbers}")
    if numbers:
        return numbers[0], numbers[-1]
    else:
        return None, None

lines = input_data.split('\n')
result_final = 0

for line in lines:
    first_number, last_number = find_first_last_numbers(line)

    if first_number is None or last_number is None:
        continue

    result_nb = first_number * 10 + last_number
    print(f"Résultat pour {line} : {result_nb}")

    result_final += result_nb

print(f"Résultat final : {result_final}")

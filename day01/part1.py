from input import input_data

def find_first_last_numbers(line):
	numbers = []
	current_number = ''

	for char in line:
		if char.isdigit():
			current_number = char
			numbers.append(int(current_number))
			current_number = ''
	

	if current_number:
		numbers.append(int(current_number))

	if numbers:
		return numbers[0], numbers[-1]
	else:
		return None, None


# Diviser les lignes
lines = input_data.split('\n')

result_final = 0

# Trouver le premier et le dernier nombre pour chaque ligne
for line in lines:
	first_number, last_number = find_first_last_numbers(line)
	print(f"Premier nombre : {first_number}, Dernier nombre : {last_number}")

	if first_number is None or last_number is None:
		continue

	result_nb = first_number * 10 + last_number
	print(f"Résultat : {result_nb}")

	result_final += result_nb

print(f"Résultat final : {result_final}")



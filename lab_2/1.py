import math


letter_frequencies = {
    'Ч': 1,
    'Е': 2,
    'Р': 1,
    'С': 2,
    'П': 1,
    'О': 2,
    'Л': 1,
    'И': 1,
    'Ц': 1,
    'А': 1
}

all_letters = list(letter_frequencies.keys())

total_word_count = 0

# Рекурсивная функция для перебора всех возможных способов выбрать 6 букв
# i — текущий индекс в списке all_letters
# letters_used_so_far — сколько букв уже выбрано
# current_selection — список, показывающий, сколько раз взята каждая буква до текущего момента
def explore_all_combinations(i, letters_used_so_far, current_selection):
    global total_word_count

    if i == len(all_letters):
        if letters_used_so_far == 6:
            # Формула: 6! / (k1! * k2! * ... * km!), где ki — количество повторов i-й буквы
            denominator = 1
            for count in current_selection:
                factorial_of_count = math.factorial(count)
                denominator = denominator * factorial_of_count

            numerator = math.factorial(6)
            number_of_permutations = numerator // denominator

            total_word_count = total_word_count + number_of_permutations
        return

    current_letter = all_letters[i]
    max_available = letter_frequencies[current_letter]
    max_we_can_take = 6 - letters_used_so_far 
    max_to_take = min(max_available, max_we_can_take)

    take = 0
    while take <= max_to_take:
        current_selection.append(take)
        explore_all_combinations(i + 1, letters_used_so_far + take, current_selection)
        current_selection.pop()
        take = take + 1


explore_all_combinations(0, 0, [])

print(total_word_count)
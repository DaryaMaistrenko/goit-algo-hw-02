def is_balanced(input_string):
    # Словник для відповідності пар дужок
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    # Стек для зберігання відкритих дужок
    stack = []

    # Проходимо по кожному символу рядка
    for char in input_string:
        if char in '({[':  # Якщо це відкрита дужка
            stack.append(char)
        elif char in ')}]':  # Якщо це закрита дужка
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Витягуємо з стека відповідну відкриту дужку
            else:
                return "Несиметрично"

    # Якщо стек порожній, усі дужки збалансовані
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"

# Приклади використання
test_string_1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
test_string_2 = "( 23 ( 2 - 3);"
test_string_3 = "( 11 }"

print(f'"{test_string_1}": {is_balanced(test_string_1)}')
print(f'"{test_string_2}": {is_balanced(test_string_2)}')
print(f'"{test_string_3}": {is_balanced(test_string_3)}')

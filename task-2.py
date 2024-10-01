from collections import deque

def is_palindrome(input_string):
    # Очищаємо рядок: переводимо в нижній регістр і видаляємо всі пробіли
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створюємо двосторонню чергу
    char_deque = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        front = char_deque.popleft()  # Видаляємо символ з початку черги
        back = char_deque.pop()       # Видаляємо символ з кінця черги
        if front != back:             # Якщо символи не рівні, це не паліндром
            return False
    
    return True  # Якщо всі символи співпадають, рядок є паліндромом

# Приклад використання
input_string = "My name is Daria"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

input_string = "Hello, World!"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

input_string = "was it me or not me"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')    

input_string = "python"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')    
# Задача №1.
# Написать функцию, которая проверяет, является ли переданное число или строка палиндромом и возвраащет True.
# В противном случаи возвращает False.
# Палиндром - это число или текст, который читается одинаково и слева, и справа: 939; 49094; 11311.

def palindrome(text):
    b = text[::-1]
    if b == text:
        return True
    else:
        return False


a = palindrome(input('Строка ввода: ')) # Для того чтобы убедиться, что возвращается
print(a)
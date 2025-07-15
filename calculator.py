import math

def calculate_factorial():
    try:
        n = int(input("Введите положительное целое число:"))
        if n < 0:
            raise ValueError("Не может быть отрицательным")
        result = math.factorial(n)
        print(f"Факториал числа {n} равен: {result}")
    except ValueError:
        print(f"Ошибка: { 'Некорректные данные, введите положительное целое число.' }")

calculate_factorial()

input("Готово, нажмите любую клавишу, чтобы выйти")

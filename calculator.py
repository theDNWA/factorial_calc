import math

def calculate_factorial():
    try:
        n = int(input("Введите положительное целое число: "))
        if n < 0:
            raise ValueError("Число не может быть отрицательным")
        result = math.factorial(n)
        print(f"Факториал числа {n} равен: {result}")
    except ValueError as e:
        print(f"Ошибка: {str(e) or 'Введены некорректные данные. Требуется положительное целое число.'}")

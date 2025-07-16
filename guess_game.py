import random


def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
# Загадываем случайное число от 1 до 100

    print("Это игра 'Угадай число'")
    print(f"Загадано число от 1 до 100. Есть {max_attempts} попыток, чтобы угадать его.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка #{attempts + 1}. Введи число:"))
        except ValueError:
            print("Ошибка, введите целое число.")
            continue


        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100!")
            continue
            # Проверка диапазона

        attempts += 1
        
        if guess < secret_number:
            print("Больше!")
        elif guess > secret_number:
            print("Меньше!")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            return
        # Сравнение с загаданным числом


    print(f"\nУвы, попытки закончились! Я загадал число: {secret_number}")
    # 0 попыток

guess_the_number()

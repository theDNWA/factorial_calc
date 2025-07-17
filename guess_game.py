import random

retry = "Y"
def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
# Загадываем случайное число от 1 до 100

    print("\nЭто игра 'Угадай число'")
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

def show_instructions():
    print("=== ИНСТРУКЦИЯ ===")
    print("1. Я загадываю число в выбранном диапазоне, по умолчанию 1-100")
    print("2. У вас есть ограниченное число попыток, по умолчанию 10")
    print("3. Вводите числа, получайте подсказки")
    print("4. Команды: Y - продолжить")
    print("5. Старайтесь угадать за минимальное число попыток!")
show_instructions()

while retry == 'Y':
    guess_the_number()
    retry = str(input('Введите Y если хотите ещё раз\n'))

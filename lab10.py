
import logging 

# Работа с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создан файл для логирования
file_handler = logging.FileHandler("log")
# Создание форматера отображающего дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

print('''Программа создана для жеребьёвки методом генерации случайных чисел.
Первым делом необходимо ввести целое, положительное, натуральное число, обозначающее количество бочоноков для жеребьёвки.
Далее при нажатии клавиши будет выводится число, обозначающее непосредственно номер жеребьёвки.''')

while True:
    logger.info('Start of the program')
    # Ввод и проверка данных
    try:
        n = int(input('Введите количество бочонков: '))
    except ValueError:
        print('Данные введены некорректно. Попробуйте снова.')
        logger.error('The data is entered incorrectly. Try again.')
        continue
    if n <= 0:
        print('Введены некорректные значения. Попробуйте снова.')
        logger.error('The data does not match the condition. Try again.')
        continue

    # Создание списка чисел от 1 до n
    a = list()
    for i in range(n):
        a.append(i+1)

    import random
    # Вывод случайных чисел
    for i in range(n):
        r_number = random.randint(0, len(a) - 1)
        print(a[r_number])
        logger.info(f'Random number is output: {a[r_number]}')
        a.pop(r_number)
        print('Оставшиеся варианты:', a, '. ', end='')
        logger.info(f'The remaining options are displayed: {a}')
        if len(a) != 0:
            input('Для вывода следующего числа нажмите Enter.')
        else:
            print('\nЕсли хоитите продолжить нажмите Enter, если нет, введите "нет".\n')
            logger.info(f'Continue\ Finish program')
    vibor = input()
    if vibor == 'нет':
        break
logger.info('The program is completed')
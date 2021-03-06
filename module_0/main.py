import numpy as np
def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    count = 1
    a = 1
    b = 100
    predict = (a + b) // 2
    while number != predict:
        count += 1
        if number > predict:
            a = predict + 1
        elif number < predict:
            b = predict - 1
        predict = (a + b) // 2

    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    max_score = int(np.max(count_ls))
    min_score = int(np.min(count_ls))
    print(f"Алгоритм {game_core} угадывает число в среднем за {score} попыток (мин {min_score}, макс {max_score})")
    return (score)


# запускаем
score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
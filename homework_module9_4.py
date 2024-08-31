from random import choice

# Задание 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов по позициям
result = list(map(lambda f, s: f == s, first, second))
print(result)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Задание 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# После выполнения этого кода, файл example.txt будет содержать указанные строки


# Задание 3: Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования метода __call__
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Вывод случайного слова из: Да, Нет, Наверное
print(first_ball())
print(first_ball())

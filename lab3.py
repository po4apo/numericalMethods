import math
import copy


def printAnswer(name: str):
    def wrapper(func):
        def decorator(*args, **kwargs):
            result = func(*args, **kwargs)
            print("-------------------------------")
            print(name.upper())
            print(f"Ответ:{result}")
            print(f"Точность:{0.0001}")
            print("-------------------------------")
        return decorator
    return wrapper


# Метод Гаусса
def is_correct_array(a, b):
    for row in range(0, len(a)):
        if len(a[row]) != len(b):
            print('Не соответствует размерность')
            return False

    for row in range(0, len(a)):
        if a[row][row] == 0:
            print('Нулевые элементы на главной диагонали')
            return False
    return True


def is_need_to_complete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2

    return math.sqrt(sum_up / sum_low) < eps


def solve_jacobi(a, b):
    if not is_correct_array(a, b):
        print('Ошибка в исходных данных')
    else:
        count = len(b)  # количество корней

        x = [1 for k in range(0, count)]  # начальное приближение корней

        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = 100  # максимально допустимое число итераций
        while numberOfIter < MAX_ITER:

            x_prev = copy.deepcopy(x)

            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if j != k: S = S + a[k][j] * x[j]
                x[k] = b[k] / a[k][k] - S / a[k][k]

            if is_need_to_complete(x_prev, x):  # проверка на выход
                break

            numberOfIter += 1

        return x


# Метод Гаусса-Зейделя
def bubble_max_row(a, col):
    max_element = a[col][col]
    max_row = col
    for i in range(col + 1, len(a)):
        if abs(a[i][col]) > abs(max_element):
            max_element = a[i][col]
            max_row = i
    if max_row != col:
        a[col], a[max_row] = a[max_row], a[col]


def solve_gauss(a,b):
    """Solve linear equations system with gaussian method.
    :param m: matrix (list of lists)
    :return: None
    """
    n = len(a)
    # forward trace
    for k in range(n):
        bubble_max_row(a, k)
        for i in range(k + 1, n):
            div = a[i][k] / a[k][k]
            b[i] -= div * b[k]
            for j in range(k, n):
                a[i][j] -= div * a[k][j]

    if is_singular(a):
        return

    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - sum([a[k][j] * x[j] for j in range(k + 1, n)])) / a[k][k]

    return x


def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False



@printAnswer('Метод гаусса')
def solve_gauss_for_user(eps):
    a = [[14.7, 0.0635, 0.0765, 0.0895],
         [0.0452, 13.8, 0.0714, 0.0844],
         [0.04, 0.0531, 12.9, 0.0793],
         [0.0349, 0.0479, -.061, 12.0]]

    b = [20.9985,
         22.4406,
         23.5192,
         24.2353]

    return solve_gauss(a, b)

@printAnswer('Метод холецкого')
def solve_jacobi_for_user(eps):
    a = [[14.7, 0.0635, 0.0765, 0.0895],
         [0.0452, 13.8, 0.0714, 0.0844],
         [0.04, 0.0531, 12.9, 0.0793],
         [0.0349, 0.0479, -.061, 12.0]]

    b = [20.9985,
         22.4406,
         23.5192,
         24.2353]

    return solve_jacobi(a, b)

if __name__ == '__main__':
    a = [[14.7, 0.0635, 0.0765, 0.0895],
         [0.0452, 13.8, 0.0714, 0.0844],
         [0.04, 0.0531, 12.9, 0.0793],
         [0.0349, 0.0479, -.061, 12.0]]

    b = [20.9985,
         22.4406,
         23.5192,
         24.2353]

    print('Решение: ', solve_jacobi(a, b))
    print('Решение: ', solve_gauss(a, b))



    gauss = solve_gauss(a, b)
    print('Результат подстановки:', end=' ')
    for i in range(4):
        line = 0
        for j in range(4):
            line += (a[i][j] * gauss[j])
        print(line, end=", ")


    print('\n','Вектор b:', b)

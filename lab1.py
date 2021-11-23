from sympy import diff, Symbol, lambdify
from math import inf

EPS = 0.0001


#  Найти один из корней уравнения   методом половинного деления, методом хорд и методом касательных.

def printAnswer(name: str):
    def wrapper(func):
        def decorator(*args, **kwargs):
            result = func(*args, **kwargs)
            print("-------------------------------")
            print(name.upper())
            print(f"Ответ:{result}")
            print(f"Точность:{EPS}")
            print("-------------------------------")


        return decorator

    return wrapper


def funk(x):
    x = float(x)
    return (x ** 3) - (0.2 * x ** 2) + (0.5 * x) + 1.5


def average(x, y):
    return (x + y) / 2


def closeEnough(x, y, eps):
    return abs(abs(x) - abs(y)) <= eps


def search(negPoint, posPoint, eps):
    midPoint = average(negPoint, posPoint)
    if closeEnough(negPoint, posPoint, eps):
        return midPoint
    testValue = funk(midPoint)
    if testValue < 0:
        return search(midPoint, posPoint, eps)
    elif testValue > 0:
        return search(negPoint, midPoint, eps)
    else:
        raise RuntimeError('Видимо testValue равно нулю')


def half_interval_method(first_point, second_point, eps = EPS):
    firstValue = funk(first_point)
    secondValue = funk(second_point)
    if firstValue > 0 and secondValue < 0:
        x = search(second_point, first_point, eps)
        return x
    elif secondValue > 0 and firstValue < 0:
        return search(first_point, second_point, eps)
    else:
        raise RuntimeError("Знаки не различные!")


def derivative(point):
    x = Symbol('x')
    f = (x ** 3) - (0.2 * x ** 2) + (0.5 * x) + 1.5
    result = f.diff(x)
    return lambdify(x, result)(point)


def chord_method(first_point, second_point, eps = EPS):
    last_test_point = first_point
    while True:
        first_value = funk(first_point)
        second_value = funk(second_point)
        if first_value * second_value >= 0:
            raise f'Произведение двух значений равно:{first_value * second_value} > 0'

        test_point = first_point - (first_value / (second_value - first_value)) * (second_point - first_point)
        test_value = funk(test_point)
        if abs(last_test_point - test_point) <= eps / 100:
            return test_point
        else:
            last_test_point = test_point
        if first_value * test_value < 0:
            second_point = test_point
        if second_value * test_value < 0:
            first_point = test_point


def tangent_method(point, eps = EPS):
    while True:
        if derivative(point) != 0:
            result_point = point - funk(point) / derivative(point)
        else:
            raise 'Дифференциал равен нулю'
        if abs(point - result_point) < eps:
            return result_point
        point = result_point

@printAnswer('Метод половинных интервалов')
def half_interval_method_for_user(eps):
    while True:
        try:
            first_point, second_point = input('Введите две числа через пробел:').split()
            return half_interval_method(float(first_point), float(second_point), eps)
        except:
            print('Введеные числа не подходят')

@printAnswer('Метод хорд')
def chord_method_for_user(eps):
    while True:
        try:
            first_point, second_point = input('Введите два числа через пробел:').split()
            return chord_method(float(first_point), float(second_point), eps)
        except:
            print('Введеные числа не подходят')

@printAnswer('Метод касательных')
def tangent_method_for_user(eps):
    while True:
        try:
            first_point = input('Введите число:')
            return tangent_method(float(first_point), eps)
        except:
            print('Введеное число не подходит')


def print_all_answer(eps):
    half_interval_method_for_user(eps)
    chord_method_for_user(eps)
    tangent_method_for_user(eps)

if __name__ == '__main__':
    half_interval_method(-2, 0, EPS)

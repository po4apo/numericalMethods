from lab1 import EPS
from tokenize import String


class Interface:
    def __init__(self, *functions):
        '''

        :param functions: принимает картежи из двух элементов. Первый элемент функция, второй название на русском.
        '''
        self.functions = functions
        self.eps = EPS

    def start(self):
        while True:
            print('Выбирете метод:')
            i = 1
            funcs = []
            for func, name in self.functions:
                print(f'{i}.{name}')
                i += 1
                funcs.append(func)
            while True:
                try:
                    num_func = int(input('Введите номер:')) - 1
                    if len(funcs) > num_func >= 0:
                        funcs[num_func](self.eps)
                        break
                    else:
                        print('Нет такой команды!')
                except:
                    print('Нужно ввести число')

    def change_eps(self, eps: float):
        self.eps = eps

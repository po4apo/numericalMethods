from Interface import Interface
from lab1 import half_interval_method_for_user, chord_method_for_user, tangent_method_for_user, print_all_answer
from  lab3 import solve_gauss_for_user, solve_jacobi_for_user
interface = Interface((half_interval_method_for_user, 'Метод половинных интервалов'),
                      (chord_method_for_user, 'Метод хорд'),
                      (tangent_method_for_user, 'Метод касательных'),
                      (solve_jacobi_for_user, 'Метод Якоби'),
                      (solve_gauss_for_user, 'Метод Гауса')
                      )
interface.change_eps(float(0.0001))
interface.start()

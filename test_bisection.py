from Bisection import Bisection
'''
f1 = lambda x: x**2 -x -1
bis = Bisection(f1)
print(bis)
bis.find_root(start_interval = 1, end_interval= 2, num_iter= 25)
bis.find_root(start_interval = -1, end_interval= 0, num_iter= 25)
bis.plot()
'''

f1 = lambda x: x**2 -x -1
bis = Bisection(f1)
print(bis.function_string)
bis2 = Bisection(lambda x: x**3 -x -1)
print(bis2.function_string)
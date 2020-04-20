from Secant import Secant

p = lambda x: x**3 - x**2 - 1
sec = Secant(p)
approx = sec.find_root(start_interval=1, end_interval=2, num_iter=20)
print(sec)
print(approx)
sec.plot()

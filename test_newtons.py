from Newtons import Newtons

p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = Newtons(p, Dp)
approx.find_root(initial_x=1)
print(approx.status)
print(approx.xn)

f = lambda x: x**(1/3)
Df = lambda x: (1/3)*x**(-2/3)
approx2 = Newtons(f, Df)
approx2.find_root(0.1, 1e-2, 100)
print(approx2.status)
print(approx2.xn)

approx.plot()
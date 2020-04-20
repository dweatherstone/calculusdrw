from Generalroots import RootStatus, Root

class Newtons(Root):
#class Newtons:
    """Newton's method is a root finding method that uses linear approximation. 
    In particular we initialise a solution x0 of the equation f(x) = 0, compute
    the linear approximation of f(x) at x0 and then find the x-intercept of the 
    linear approximation.

    Attributes:
        f (function) representing the function f(x)
        d_f (function) representing the first differential of f(x)
    """

    def __init__(self, func, d_func):
        """Initialising an object to calculate the root of a function using Newton's
        method.

        Parameters
        ----------
        func : function
                Function for which we are searching for a solution f(x) = 0
        d_func : function
                First derivative of f(x).
        """
        super().__init__(func)
        self.d_f = d_func
        self.x0 = None
        self.epsilon = None

    def find_root(self, initial_x = 0, epsilon = 1e-10, max_iter = 100):
        """Approximate solution of f(x) = 0 by Newton's method.

        Parameters
        ----------
        initial_x : number
                Initial guess for a solution to f(x) = 0
        epsilon : number
                Stopping criteria such that abs(f(x)) < epsilon
        max_iter : integer
                Maximum number of iterations of Newton's method.

        Returns
        -------
        xn : number
            Result of Newton's method.
            If df(xn) == 0, return None
            If iterations > max_iter, return None
        """
        assert max_iter > 0
        assert epsilon > 0
        self.x0 = initial_x
        self.epsilon = epsilon
        self.max_iter = max_iter
        xn = self.x0
        for _ in range(0, self.max_iter):
            fxn = self.f(xn)
            if abs(fxn) < self.epsilon:
                if self.xn == None:
                    self.xn = [xn]
                else:
                    self.xn.append(xn)
                self.status = RootStatus.root_found
                return xn
            dfxn = self.d_f(xn)
            if dfxn == 0:
                self.status = RootStatus.zero_derivative
                return None
            xn = xn - fxn/dfxn
        self.status = RootStatus.exceeded_max_iter
        return None
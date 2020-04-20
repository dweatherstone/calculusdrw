from Generalroots import RootStatus, Root

class Bisection(Root):
    """The simplest root finding algorithm is the bisection method. The 
    algorithm applies to any continuous function  on an interval  where 
    the value of the function  changes sign from  to . The idea is simple: 
        divide the interval in two, a solution must exist within one 
        subinterval, select the subinterval where the sign of  changes 
        and repeat.
    """
    def __init__(self, func):
        """ Initialising an object to calculate the root of a function using
        the Bisection method.

        Parameters
        ----------
        func (function): The function for which we are trying to approximate a
                        solution.
        """
        super().__init__(func)

    def find_root(self, start_interval, end_interval, num_iter = 100):
        """ Approximate solution of f(x) = 0 on interval [a, b] using the
        bisection method.

        Parameters
        ----------
        start_interval (number): The lower bound of the interval in which to
                    search for a solution.
        end_interval (number): The upper bound of the interval in which to
                    search for a solution.
        num_iter (positive integer): The number of iterations to implement.

        Returns
        -------
        xn (number): Result of Bisection method. The midpoint of the Nth interval
                    computed by the bisection method. The intial interval
                    [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
                    midpoint m_n = (a_n + b_n)/2, then the function returns this
                    solution. If all signs of values f(a_n), f(b_n) and f(m_n) 
                    are the same at any iteration, the bisection methode fails
                    and returns None.
        """
        assert num_iter > 0
        assert end_interval > start_interval
        if self.f(start_interval)*self.f(end_interval) >= 0:
            self.status = RootStatus.method_fails
            return None
        a_n = start_interval
        b_n = end_interval
        for _ in range(1, num_iter+1):
            m_n = (a_n + b_n)/2
            f_m_n = self.f(m_n)
            if self.f(a_n)*f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif self.f(b_n)*f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                self.status = RootStatus.root_found
                self.xn.append(m_n)
                return self.xn
            else:
                self.status = RootStatus.method_fails
                return None
        m_n = (a_n + b_n)/2
        self.xn.append(m_n)
        self.status = RootStatus.exceeded_max_iter
        return self.xn
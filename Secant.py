from Generalroots import RootStatus, Root

class Secant(Root):

    def __init__(self, func):

        super().__init__(func)

    def find_root(self, start_interval, end_interval, num_iter = 100):

        assert num_iter > 0
        assert end_interval > start_interval

        if self.f(start_interval)*self.f(end_interval) >= 0:
            self.status = RootStatus.method_fails
            return None

        a_n = start_interval
        b_n = end_interval
        for _ in range(num_iter):
            m_n = a_n - self.f(a_n)*(b_n - a_n)/(self.f(b_n) - 
                                    self.f(a_n))
            f_m_n = self.f(m_n)
            if self.f(a_n)*f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif self.f(b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                self.status = RootStatus.root_found
                self.xn.append(m_n)
                return m_n
            else:
                self.status = RootStatus.method_fails
                return None

        m_n = a_n - self.f(a_n)*(b_n - a_n)/(self.f(b_n) - self.f(a_n))
        self.xn.append(m_n)
        self.status = RootStatus.exceeded_max_iter
        return m_n
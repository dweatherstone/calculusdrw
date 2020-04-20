import enum
import inspect
import numpy as np
import matplotlib.pyplot as plt

class RootStatus(enum.Enum):
    pending = "Pending: find_root not yet run"
    root_found = "Roots found"
    exceeded_max_iter = "Exceeded maximum iterations"
    zero_derivative = "Zero derivative encountered"
    method_fails = "method fails"

class Root:

    def __init__(self, func):
        self.f = func
        self.max_iter = None
        self.xn = []
        self.status = RootStatus.pending
        self.function_string = self._get_function_string(inspect.getsource(func))

    def _get_function_string(self, original_function_string):
        fs = original_function_string
        find_string = 'lambda x: '
        fs = fs[fs.find(find_string) + len(find_string):]
        fs = 'f(x) = ' + fs.replace('(', '').replace(')', '')
        return fs.strip()

    def plot(self):
        x = np.arange(-10, 10, 0.01)
        y = self.f(x)
        plt.plot(x, y)
        plt.axhline(color='black')
        plt.axvline(color='black')
        for x in self.xn:
            plt.axvline(x, color='red',  label='x={}'.format(round(x, 3)))
        plt.title(self.function_string)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.show()

    def __repr__(self):
        return self.function_string

    def print_status(self):
        print(self.status.value)

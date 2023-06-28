import numpy as np

class YagiYunes:
    def __init__(self, q):
        self.q = q

        self.b = np.array([-27.7408, 8.42358, 122.686, -19.7551, -175.496, 133.708])
        self.c = np.array([-25.5593, 5.58527, 92.0337, 26.8586, -70.247, -56.3076])

        self.b = np.reshape(self.b, newshape=(3, 2))
        self.c = np.reshape(self.c, newshape=(3, 2))

        self.n = 0.743

    def f(self, q): # not sure if should pass q upon init or only in f
        numerator = 1 - q**(10 / (3 - self.n))
        denominator = 1 + q**(10 / (3 - self.n))
        return numerator / denominator

    def function(self, lambda_s):
        numerator_sum = 0
        denominator_sum = 0
        for i in range(1, 4):
            for j in range(1, 3):
                numerator_sum += (self.b[i-1, j-1] * self.q**j * lambda_s**(-i / 5))
                denominator_sum += (self.c[i-1, j-1] * self.q**j * lambda_s**(-i / 5))

        fraction = (1 + numerator_sum) / (1 + denominator_sum)
        result = self.f(self.q) * lambda_s * fraction
        return result

    def plot(self, ax, lims, **kwargs):
        lambda_s = np.linspace(*lims, 1000, dtype=complex) # complex for fractional root in numpy
        lambda_a = self.function(lambda_s)

        lambda_s = np.real(lambda_s) # imaginary parts should be all zero
        lambda_a = np.real(lambda_a)

        ax.plot(lambda_s, lambda_a, label='Yagi & Yunes fit for q=' + str(self.q), color='black', **kwargs)

        text_x = np.min(lambda_s) / 1.5
        text_y = np.min(lambda_a) * 1.5
        ax.text(text_x, text_y, 'q=' + str(self.q))
import numpy as np

class YagiYunes:
    def __init__(self):

        self.b = np.array([-27.7408, 8.42358, 122.686, -19.7551, -175.496, 133.708])
        self.c = np.zeros([-25.5593, 5.58527, 92.0337, 26.8586, -70.247, -56.3076])

        self.b = np.reshape(self.b, shape=(3, 2))
        self.c = np.reshape(self.c, shape=(3, 2))

        self.n = 0.743

    def f(self, q):
        numerator = 1 - q**(10 / (3 - self.n))
        denominator = 1 + q**(10 / (3 - self.n))
        return numerator / denominator

    def __call__(self, lambda_s, q):
        numerator_sum = 0
        denominator_sum = 0
        for i in range(1, 4):
            for j in range(1, 4):
                numerator_sum += self.b[i-1, j-1] * q**j * lambda_s**(-i / 5)
                denominator_sum += self.c[i-1, j-1] * q**j * lambda_s**(-i / 5)

        fraction = (1 + numerator_sum) / (1 + denominator_sum)
        result = self.f(q=q) * lambda_s * fraction
        return result
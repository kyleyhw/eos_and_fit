import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class EOS:
    def __init__(self, data, name, q):
        self.name = name
        self.q = q
        self.ms = data.ms
        self.Lambdas = data.Lambdas
        self.f = sp.interpolate.interp1d(x=self.ms, y=self.Lambdas)

        self.m1 = np.linspace(1, 2, 10000)
        self.m2 = self.q * self.m1

        lambda_m1 = self.f(self.m1)
        lambda_m2 = self.f(self.m2)

        self.lambda_s = (lambda_m1 + lambda_m2) / 2
        self.lambda_a = (lambda_m1 - lambda_m2) / 2

    def plot(self, ax, **kwargs):
        ax.plot(self.lambda_s, self.lambda_a, label=self.name, **kwargs)
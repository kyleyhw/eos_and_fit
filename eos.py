import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class EOS:
    def __init__(self, data, name, q):
        self.name = name
        self.q = q
        self.ms = data.ms
        self.Lambdas = data.Lambdas
        self.lambda_f = sp.interpolate.interp1d(x=self.ms, y=self.Lambdas)

        m1 = np.linspace(np.min(self.ms), np.max(self.ms), 10000)
        m2 = m1 / self.q

        filter = (m2 > np.min(self.ms)) & (m2 < np.max(self.ms)) # so that lambda can be interpolated over m2

        self.m1 = m1[filter]
        self.m2 = m2[filter]

        lambda_m1 = self.lambda_f(self.m1)
        lambda_m2 = self.lambda_f(self.m2)

        self.lambda_s = (lambda_m1 + lambda_m2) / 2
        self.lambda_a = (lambda_m1 - lambda_m2) / 2

    def plot(self, ax, **kwargs):
        ax.plot(self.lambda_s, self.lambda_a, label=self.name + ' q=' + str(self.q), **kwargs)

    def plot_raw(self, ax, **kwargs):
        ax.plot(self.ms, self.Lambdas, label=self.name, **kwargs)
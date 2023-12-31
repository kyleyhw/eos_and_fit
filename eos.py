import numpy as np
import scipy as sp

from data_loader import DataLoader

class EOS:
    def __init__(self, name, q):
        self.name = name
        self.q = q

        data = DataLoader('data/macro-' + name + '.csv')

        self.ms = data.ms
        self.Lambdas = data.Lambdas

        self.lambda_f = sp.interpolate.interp1d(x=self.ms, y=self.Lambdas)

        m1 = np.linspace(np.min(self.ms), np.max(self.ms), 10000)
        m2 = m1 * self.q

        filter = (m2 > np.min(self.ms)) & (m2 < np.max(self.ms)) # so that lambda can be interpolated over m2

        self.m1 = m1[filter]
        self.m2 = m2[filter]

        lambda_m1 = self.lambda_f(self.m1)
        lambda_m2 = self.lambda_f(self.m2)

        self.lambda_s = (lambda_m2 + lambda_m1) / 2
        self.lambda_a = (lambda_m2 - lambda_m1) / 2

        self.lower_lim = np.min(self.lambda_s)
        self.upper_lim = np.max(self.lambda_s)

    def plot(self, ax, **kwargs):
        ax.plot(self.lambda_s, self.lambda_a, **kwargs)

    def plot_raw(self, ax, **kwargs):
        ax.plot(self.ms, self.Lambdas, **kwargs)
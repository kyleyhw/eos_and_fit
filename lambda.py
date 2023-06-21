import scipy as sp

class Lambda:
    def __init__(self, data):
        self.ms = data.ms
        self.Lambdas = data.Lambdas
        self.f = f = sp.interpolate.interp1d(x=self.ms, y=self.Lambdas)

    
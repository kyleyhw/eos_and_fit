import csv
import numpy as np

class DataLoader:
    def __init__(self, filename):
        ms = []
        Lambdas = []

        with open(filename) as file:
            raw_read = csv.reader(file)
            next(raw_read)
            for row in raw_read:
                ms.append(float(row[2]))
                Lambdas.append(float(row[3]))

        ms = np.array(ms)
        Lambdas = np.array(Lambdas)

        injectivity_index = np.nonzero(ms == np.max(ms))[0][0]

        self.ms = ms[:injectivity_index]
        self.Lambdas = Lambdas[:injectivity_index]
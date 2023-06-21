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

        self.ms = np.array(ms)
        self.Lambdas = np.array(Lambdas)
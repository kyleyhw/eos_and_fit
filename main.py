import matplotlib.pyplot as plt

from data_loader import DataLoader
from eos import EOS

data = DataLoader('data/macro-alf2cr.csv')
alf2cr = EOS(data, name='alf2cr', q=1)

fig, ax = plt.subplots(1, 1)
alf2cr.plot(ax=ax)

plt.savefig('plot.png')
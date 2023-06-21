import matplotlib.pyplot as plt

from data_loader import DataLoader
from eos import EOS

fig, ax = plt.subplots(1, 1)

names = ['alf2cr', 'alf4cr', 'bsk20cr']
qs = [0.5, 0.75, 0.9]
for name in names:
    for q in qs:
        data = DataLoader('data/macro-' + name + '.csv')
        eos = EOS(data, name=name, q=q)
        eos.plot(ax=ax)

ax.set_ylim((10, 10000))
ax.set_xlim((10, 10000))

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'\Lambda_s')
ax.set_ylabel(r'\Lambda_a')
plt.legend()

plt.savefig('plot.png')
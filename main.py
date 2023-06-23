import matplotlib.pyplot as plt

from data_loader import DataLoader
from eos import EOS
from fits import YagiYunes

# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "Helvetica"
# })

def plot_main(names, qs):
    fig, ax = plt.subplots(1, 1)
    for q in qs:
        for name in names:
            data = DataLoader('data/macro-' + name + '.csv')
            eos = EOS(data, name=name, q=q)
            eos.plot(ax=ax)

        fit = YagiYunes(q=q)
        fit.plot(ax=ax)

    ax_min = 1e1
    ax_max = 1e4

    ax.set_ylim((ax_min, ax_max))
    ax.set_xlim((ax_min, ax_max))

    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xlabel(r'\Lambda_s')
    ax.set_ylabel(r'\Lambda_a')

    # plt.legend()

    plt.savefig('plots/plot.png')

def plot_raw(names):
    fig, ax = plt.subplots(1, 1)
    for name in names:
        data = DataLoader('data/macro-' + name + '.csv')
        eos = EOS(data, name=name, q=1)
        eos.plot_raw(ax=ax)

    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xlabel(r'm')
    ax.set_ylabel(r'\Lambda(m)')
    fig.suptitle('Raw plot for lambda(m) vs m for various EOS')
    plt.legend()

    plt.savefig('plots/raw_plot.png')


names = ['alf2cr', 'alf4cr', 'bsk20cr']
qs = [0.5, 0.75, 0.9]

plot_main(names=names, qs=qs)
plot_raw(names=names)
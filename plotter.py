import numpy as np
import matplotlib.pyplot as plt

from data_loader import DataLoader
from eos import EOS

class Plotter:
    def __init__(self, qs, names, Fit):
        self.qs = qs
        self.names = names
        self.Fit = Fit

        self.qs_dict = {}

        for q in self.qs:
            self.qs_dict[str(q)] = {}
            dictionary = self.qs_dict[str(q)]
            dictionary['fit'] = self.Fit(q=q)
            for name in self.names:
                dictionary[name] = EOS(name=name, q=q)


    def plot_main(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        for q in self.qs:
            dictionary = self.qs_dict[str(q)]
            fit = dictionary['fit']
            lower_lims = []

            for name in self.names:
                eos = dictionary[name]
                eos.plot(ax=ax)

                lower_lims.append(eos.lower_lim)

            lower_lim = np.min(lower_lims)
            upper_lim = ax.get_xlim()[1]

            fit.plot(ax=ax, lims=(lower_lim, upper_lim))

        ax_min = 1
        ax_max = 1e4

        ax.set_ylim((ax_min, ax_max))
        ax.set_xlim((ax_min, ax_max))

        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlabel(r'\Lambda_s')
        ax.set_ylabel(r'\Lambda_a')

        # plt.legend()
        if save:
            plt.savefig('plots/plot.png')
        if show:
            plt.show()


    def plot_raw(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        for name in self.names:
            data = DataLoader('data/macro-' + name + '.csv')
            eos = EOS(name=name, q=1)
            eos.plot_raw(ax=ax)

        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlabel(r'm')
        ax.set_ylabel(r'\Lambda(m)')
        fig.suptitle('Raw plot for lambda(m) vs m for various EOS')
        plt.legend()
        if save:
            plt.savefig('plots/raw_plot.png')
        if show:
            plt.show()
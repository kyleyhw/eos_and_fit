import numpy as np
import matplotlib.pyplot as plt

from eos import EOS

class Plotter:
    def __init__(self, qs, names, Fit, ax_lims=(8, 1e4)):
        self.qs = qs
        self.names = names
        self.Fit = Fit
        self.ax_min = ax_lims[0]
        self.ax_max = ax_lims[1]

        self.qs_dict = {}

        for q in self.qs:
            self.qs_dict[str(q)] = {}
            dictionary = self.qs_dict[str(q)]
            fit = self.Fit(q=q)
            dictionary['fit'] = fit

            for name in self.names:
                eos = EOS(name=name, q=q)
                dictionary[name] = eos
                residual = np.abs(eos.lambda_a - fit.function(eos.lambda_s)) / fit.function(eos.lambda_s)
                dictionary[name + '_residual'] = residual

            self.linestyles = ['solid', 'dotted', 'dashed', 'dashdot']

    def plot_main_on_ax(self, ax):
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

        ax.set_ylim((self.ax_min, self.ax_max))
        ax.set_xlim((self.ax_min, self.ax_max))

        ax.set_xscale('log')
        ax.set_yscale('log')

    def plot_residual_on_ax(self, ax):
        for i, q in enumerate(self.qs):
            linestyle = self.linestyles[i % len(self.qs)]
            dictionary = self.qs_dict[str(q)]
            for name in self.names:
                x = dictionary[name].lambda_s
                y = dictionary[name + '_residual']
                ax.plot(x, y, label=name + ' q=' + str(q), linestyle=linestyle)

        ax.set_xlim((self.ax_min, self.ax_max))

        ax.set_xscale('log')
        ax.set_yscale('log')


    def plot_main(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        self.plot_main_on_ax(ax=ax)

        ax.set_xlabel(r'$\Lambda_s$')
        ax.set_ylabel(r'$\Lambda_a$')

        fig.suptitle('EOS and fit for q in ' + str(self.qs))

        # plt.legend()
        if save:
            plt.savefig('plots/plot.png')
        if show:
            plt.show()

    def plot_residual(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        self.plot_residual_on_ax(ax=ax)

        ax.set_xlabel(r'$\Lambda_s$')
        ax.set_ylabel('fractional difference')

        fig.suptitle('Residual plots for each EOS')

        if save:
            fig.savefig('plots/residual_plot.png')
        if show:
            fig.show()

    def plot_combined(self, save=False, show=False):
        fig, axs = plt.subplots(2, 1, sharex=True)
        (ax1, ax2) = axs

        fig.subplots_adjust(wspace=0, hspace=0)

        self.plot_main_on_ax(ax=ax1)
        self.plot_residual_on_ax(ax=ax2)

        if save:
            fig.savefig('plots/combined_plot.png')
        if show:
            fig.show()


    def plot_raw(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        for name in self.names:
            eos = EOS(name=name, q=1)
            eos.plot_raw(ax=ax)

        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlabel(r'm')
        ax.set_ylabel(r'$\Lambda$(m)')
        fig.suptitle('Raw plot for lambda(m) vs m for various EOS')
        plt.legend()
        if save:
            plt.savefig('plots/raw_plot.png')
        if show:
            plt.show()
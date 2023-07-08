import numpy as np
import matplotlib.pyplot as plt

from eos import EOS

class Plotter:
    def __init__(self, qs, names, truth, fits, ax_lims=(8, 1e4)):
        self.qs = qs
        self.names = names
        self.truth = truth
        self.fits = fits
        self.ax_min = ax_lims[0]
        self.ax_max = ax_lims[1]

        self.qs_dict = {}
        self.fit_names = []

        for q in self.qs:
            self.qs_dict[str(q)] = {}
            dictionary = self.qs_dict[str(q)]
            truth = self.truth(q=q)
            for Fit in self.fits:
                fit = Fit(q=q)
                dictionary[fit.name] = fit
                self.fit_names.append(fit.name)

            for name in self.names:
                eos = EOS(name=name, q=q)
                dictionary[name] = eos
                residual = np.abs(eos.lambda_a - truth.function(eos.lambda_s)) / truth.function(eos.lambda_s)
                dictionary[name + '_residual'] = residual

            self.linestyles = ['solid', 'dotted', 'dashed', 'dashdot']
            self.colors = ['red', 'blue', 'lime', 'violet', 'orange']

    def plot_main_on_ax(self, ax):
        for i, q in enumerate(self.qs):
            dictionary = self.qs_dict[str(q)]
            fit = dictionary['fit']
            lower_lims = []
            label = None

            for j, name in enumerate(self.names):
                eos = dictionary[name]
                color = self.colors[j % len(self.colors)]
                if i == 0:
                    label = name
                eos.plot(ax=ax, label=label, color=color)

                lower_lims.append(eos.lower_lim)

            lower_lim = np.min(lower_lims)
            upper_lim = ax.get_xlim()[1]

            if i == 0:
                label=self.truth.name

            fit.plot(ax=ax, lims=(lower_lim, upper_lim), label=label)

        ax.set_ylim((self.ax_min, self.ax_max))
        ax.set_xlim((self.ax_min, self.ax_max))

        ax.set_xscale('log')
        ax.set_yscale('log')

    def plot_residual_on_ax(self, ax):
        for i, q in enumerate(self.qs):
            dictionary = self.qs_dict[str(q)]

            linestyle = self.linestyles[i % len(self.linestyles)]

            for j, name in enumerate(self.names):
                color = self.colors[j % len(self.colors)]

                x = dictionary[name].lambda_s
                y = dictionary[name + '_residual']

                label = None

                if j == 0:
                    label = 'q=' + str(q)

                ax.plot(x, y, label=label, linestyle=linestyle, color=color)

        ax.set_xlim((self.ax_min, self.ax_max))

        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.legend()


    def plot_main(self, save=False, show=False):
        fig, ax = plt.subplots(1, 1)
        self.plot_main_on_ax(ax=ax)

        ax.set_xlabel(r'$\Lambda_s$')
        ax.set_ylabel(r'$\Lambda_a$')

        fig.suptitle('EOS and fit for q in ' + str(self.qs))

        plt.legend()

        if save:
            plt.savefig('plots/main_plot.png')
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

        ax1.set_ylabel(r'$\Lambda_a$')
        ax2.set_ylabel(r'fractional diff. from fit')
        ax2.set_xlabel(r'$\Lambda_s$')

        ax1.legend()

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

        # plt.legend()

        if save:
            plt.savefig('plots/raw_plot.png')
        if show:
            plt.show()
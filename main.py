from fits import YagiYunes
from plotter import Plotter

names = ['alf2cr', 'alf4cr', 'bsk20cr', 'bsk21cr', 'bsr2cr', 'dd2ycr', 'ddhdcr', 'ddq2acr', 'gm1bcr', 'h4cr',
         'hqc18cr', 'hqc19cr', 'mpa1cr', 'nl3cr', 'nl3ycr', 'rscr', 'sk255cr', 'ski2cr', 'skopcr', 'sly230acr',
         'slycr', 'tm1cr']
qs = [0.9]

ax_min = 8
ax_max = 1e4

plotter = Plotter(names=names, qs=qs, Fit=YagiYunes, ax_lims=(ax_min, ax_max))

plotter.plot_main(save=True)
plotter.plot_residual(save=True)
plotter.plot_raw(save=True)
plotter.plot_combined(save=True)
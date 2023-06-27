from fits import YagiYunes
from plotter import Plotter

names = ['alf2cr', 'alf4cr', 'bsk20cr']
qs = [0.9]

ax_min = 8
ax_max = 1e4

plotter = Plotter(names=names, qs=qs, Fit=YagiYunes, ax_lims=(ax_min, ax_max))

plotter.plot_main(save=True)
plotter.plot_residual(save=True)
plotter.plot_raw(save=True)
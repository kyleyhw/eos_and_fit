from fits import YagiYunes
from plotter import Plotter

names = ['alf2cr', 'alf4cr', 'bsk20cr']
qs = [0.5, 0.75, 0.9]

plotter = Plotter(names=names, qs=qs, Fit=YagiYunes)

plotter.plot_main(save=True)
plotter.plot_raw(save=True)
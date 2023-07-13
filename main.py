from fits import YagiYunes, CommonRadius
from plotter import Plotter

eos_names = ['alf2cr', 'alf4cr', 'bsk20cr', 'bsk21cr', 'bsr2cr', 'dd2ycr', 'ddhdcr', 'ddq2acr', 'gm1bcr', 'h4cr',
         'hqc18cr', 'hqc19cr', 'mpa1cr', 'nl3cr', 'nl3ycr', 'rscr', 'sk255cr', 'ski2cr', 'skopcr', 'sly230acr',
         'slycr', 'tm1cr'][:4]
qs = [0.5, 0.75, 0.9]

ax_min = 8
ax_max = 1e4

plotter = Plotter(qs=qs, eos_names=eos_names, Truth=YagiYunes, fits=[CommonRadius], ax_lims=(ax_min, ax_max))

plotter.plot_main(save=True)
plotter.plot_residual(save=True)
plotter.plot_raw(save=True)
plotter.plot_combined(save=True)
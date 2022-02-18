from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

vaspout = Vasprun("./vasprun.xml")
bandstr = vaspout.get_band_structure(line_mode=True)
plt = BSPlotter(bandstr).get_plot(ylim=[-25,20])
plt.savefig("bandstructure.pdf")


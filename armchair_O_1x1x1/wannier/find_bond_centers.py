
from pymatgen.core import Structure
from pymatgen.analysis.chemenv.coordination_environments.coordination_geometry_finder import LocalGeometryFinder
from sympy import true

from numpy.linalg import norm
from numpy import remainder

struct = Structure.from_file("POSCAR")

centers = []

for s in struct.sites:
    for n in struct.get_neighbors(s,1.5):
        c = (s.frac_coords + n.frac_coords)/2.0
        c = remainder(c,1)
        if s.specie != n.specie:
            add_center = True
            for c2 in centers:
                d = c-c2
                if norm(d) < 0.001:
                    add_center = False
                    break
            if add_center: 
                centers.append(c)

print('Found {:d} bonds'.format(len(centers)))
centers.sort(key=lambda c: c[1])
for c in centers:
    print('f={x:6.4f},{y:6.4f},{z:6.4f}:s'.format(x=c[0],y=c[1],z=c[2]))
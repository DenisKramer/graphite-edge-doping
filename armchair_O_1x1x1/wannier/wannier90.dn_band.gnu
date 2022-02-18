set style data dots
set nokey
set xrange [0: 2.42773]
set yrange [-21.52966 : 14.01133]
set arrow from  0.81055, -21.52966 to  0.81055,  14.01133 nohead
set arrow from  1.61718, -21.52966 to  1.61718,  14.01133 nohead
set xtics ("G"  0.00000,"A"  0.81055,"X"  1.61718,"Z"  2.42773)
 plot "wannier90.dn_band.dat"

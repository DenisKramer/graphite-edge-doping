#File to plot a colour-mapped Bandstructure
set palette defined ( 0 "blue", 3 "green", 6 "yellow", 10 "red" )
unset ztics
unset key
# can make pointsize smaller (~0.5). Too small and nothing is printed
set pointsize 0.8
set grid xtics
set view 0,0
set xrange [0:  2.42773]
set yrange [-21.52966: 14.01133]
set xtics ("G                   "  0.00000,"A                   "  0.81055,"X                   "  1.61718,"Z                   "  2.42773)
splot "wannier90.dn_band.dat" u 1:2:3 w p pt 13 palette
#use the next lines to make a nice figure for a paper
#set term postscript enhanced eps color lw 0.5 dl 0.5
#set pointsize 0.275

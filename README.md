# Investigation of doped graphite edges

This repository contains an investigation of the electronic structure of graphite edges via Wannier functions.

## Folders

| Name             | Description                                       |
| ---------------- | ------------------------------------------------- |
| armchair_O_1x1x1 | Calcualtion of O-terminated undoped armchair edge |

## Structure of calculations

| Subfolder | Description                                                   |
| --------- | ------------------------------------------------------------- |
| relax     | Initial relaxation run to relax structure                     |
| relax2    | Repeat of relaxation run                                      |
| static    | Static calculation of relaxed structure to get charge density |
| band      | Reference calculation of band structure in VASP               |
| wannier   | Calculation of Wannier functions and projected band structure |

## Protocol

- Calculate fully relaxed structure in VASP
- Generate charge density 
- Generate needed Wannier90 files running VASP in wannier folder
- Run Wannier90 in wannier folder to create Wannier functions and plots

## Notes on generating Wannier functions

- The interface between Wannier90 and VASP is a bit clunky
- Best to run VASP once to create a fresh 'wannier90.win' file
- Then edit the 'wannier90.win' by defining the wanted projections and number of bands and wannier functions
- Then run VASP again to create the needed matrix elements of the projections
- Then run Wannier90 to create Wannier functions and plots

For spin-polarised calculations, VASP creates two files 'wannier90.up.win' and wannier90.dn.win'. These can be treated as completely separate calculations. 

Wannier90 3.0 is needed for these calculations, because the number of bands and wannier functions is not equal. There is also no suitable isolated set of bands to operate on, making the disentanglement features of the newer Wannier90 versions a needed pre-requisit.

### Comments on initial projections

Using atom-centred projections led to really ugly Wannier functions, so I opted to place s functions in the bond centres for all C-C bonds and the C-O bonds. This is facilitated by the 'find_bond_centers.py' script, which simply calculates the centres between pairs of atoms and writes them in a Wannier90-friendly way into the terminal. This output needs to be copied into the 'wannier90.xx.win' files.

Nonetheless, the resulting individual Wannier functions are not particularly good. However, the sum of Wannier functions derived for the pz and sp2 manifolds seems to be ok. There are the 'sum_xfs_data.ipynb' and 'xsf2vtk.ipyn' Jupyter notebooks to create a visualisation of the summed Wannier functions.

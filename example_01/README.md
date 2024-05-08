# Example 01

## Description
This example is the least complex. The example pipeline does the following:
1. Read in a series of 2d diffraction patterns saved in .cbf format.
1. Azimuthally integrate each diffraction pattern.
1. Save the resulting Intensity vs. radial coordinate data in .npz format.

## Instructions

### Activate the conda environment
1. `source /nfs/chess/user/x-cite/miniconda3/bin/activate`
1. `conda activate CHAP_example_01`

### Create simulated diffraction data
1. `cd CHAP-Training-Examples-Materials/example_01/`
1. `mkdir input`
1. Run the simulation: `./generate_input_data.py`
1. Check results: `ls input` -- there should be 10 .cbf files and 1 .poni file

### Run the azimuthal integration (CHAP pipeline):
1. `CHAP pipeline.yaml`
1. `ls output`, check for a file named azimuthally_integrated.npz

### Visualize the output with `matplotlib` (via a Jupyter notebook)
1. Add the conda environment as a jupyter kernel:
   ```bash
   python -m ipykernel install --user --name=chap_example_01 --display-name "CHAP_example_01"
   ```
1. On JupyterHub, navigate to the directory with the jupyter notebook:
    1. Double-click on CLASSE_shortcuts folder
    1. Double-click on chess_[username] folder: This is a softlink to /nfs/chess/user/[username]
    1. Double-click on CHAP-Training-Examples-Materials -> example_01
1. Load the notebook: Double-click on visualize.ipynb
1. Select Kernel: choose CHAP_example_01
1. Run the cells, close tab when done
1. `conda deactivate`
1. `conda deactivate`
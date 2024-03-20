# Example 01
This example is the least complex. The example pipeline does the following:
1. Read in a series of 2d diffraction patterns saved in .cbf format.
1. Azimuthally integrate each diffraction pattern.
1. Save the resulting Intensity vs. radial coordinate data in .npz format.

## Instructions
1. Setup:
    1. `conda env create -f environment.yaml`
    1. `conda activate CHAP_example_01`
    1. `./generate_input_data.py`
1. Run the CHAP pipeline:
    1. `CHAP pipeline.yaml`
1. Examine the results:
    1. Open `visualize.ipynb` on jupyter01.classe.cornell.edu
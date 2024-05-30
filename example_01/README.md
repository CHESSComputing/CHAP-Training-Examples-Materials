# Example 01

## Description
This example is the least complex. The example pipelines do the following:
1. Read in a series of 2D diffraction patterns.
1. Azimuthally integrate each diffraction pattern.
1. Save the resulting Intensity vs. radial coordinate data in .npz format.

Note that there are two pipelines to choose from in this example: `pipeline_cbf.yaml` and `pipeline_h5.yaml`. They both do the same thing, but each one operates on a different set of input 2D diffraction data. `pipeline_cbf.yaml` will run slightly faster (~3 seconds as opposed to ~1 minute), but the data in this case are synthetic and not very interesting for visualization.

## Instructions

1. Activate the conda environment. Open a terminal and run:
    1. `source /nfs/chess/user/x-cite/miniconda3/bin/activate`
    1. `conda activate CHAP_example_01`

1. Process the input data using `CHAP`. In the same terminal used in step 1:
    1. Navigate to your `CHAP-Training-Examples-Materials/example_01` directory
    1. Run the process: `CHAP pipeline_cbf.yaml` (and/or `CHAP pipeline_h5.yaml`)
    1. Check the output: `ls output_cbf` (and/or `ls output_h5`)
        1.  Look for a file named `azimuthally_integrated.npz`

1. Visualize the input and output data used in this example with `matplotlib` (via a Jupyter notebook)
    1. Add the conda environment as a jupyter kernel. In the same terminal used in step 1 and 2, run:
        ```bash
        python -m ipykernel install --user --name=chap_example_01 --display-name "CHAP_example_01"
        ```
    1. (optional) We're now done using the terminal with this example, so deactivate the environment by running `conda deactivate; conda deactivate`. Close the terminal.
    1. In JupyterHub, navigate to the directory with the jupyter notebook:
        1. Double-click on CLASSE_shortcuts folder
        1. Double-click on chess_[username] folder: This is a softlink to `/nfs/chess/user/[username]`
        1. Double-click on CHAP-Training-Examples-Materials -> example_01
    1. Open the notebook by double-clicking on visualize.ipynb
    1. Select Kernel: choose CHAP_example_01
    1. Run the cells in order (click the right-triangle button or type Shift-Enter), complete the optional exercises, and the notebook close tab when done.

# Example 02

## Description
A standard tomographic reconstruction in CHAP consists of three steps:
1. Reducing the data, i.e., correcting the raw detector images for background
and non-uniformities in the beam intensity profile using dark and bright fields
collected separately from the tomography image series.
1. Finding the calibrated rotation axis. Accurate reconstruction relies on
accurately knowing the center of rotation at each data plane perpendicular to
the rotation axis (the sinogram). This rotation axis is calibrated by selecting
two data planes, one near the top and one near the bottom of the sample or
beam, and visually or automatically picking the optimal center location.
1. Reconstructing the reduced data for the calibrated rotation axis.
For samples taller than the height of the beam, this last step can consist of
two parts:
    - reconstruction of each individual stack of images, and
    - combining the individual stacks into one 3D reconstructed data set.

## Instructions

1. Activate the conda environment. Open a terminal and run:
    1. `source /nfs/chess/user/x-cite/miniconda3/bin/activate`
    1. `conda activate CHAP_example_02`

1. Create simulated tomography data
    1. Navigate to your `CHAP-Training-Examples-Materials/example_02` work directory.
    1. Run the simulation: `CHAP pipeline_create_simdata.yaml`
    1. After completion, you should have a data directory in your work directory
with the SPEC data for a sample named "hollow_pyramid" of a simulated
tomography experiment on a truncated hollow square pyramid on the CHESS id1a3
beamline.

1. Process the input data using `CHAP` (tomographic reconstruction). In the same terminal used in step 1, run: 
    1. `CHAP pipeline.yaml`
    1. Follow the interactive prompts OR replace `true` with `false` on line 4 in
`pipeline.yaml` (`interactive: false`) and run the workflow non-interactively. When running interactively, simply select or accept the offered defaults for this tutorial.
    1. The job output appears in a newly created `output` directory and consists of a
single NeXus file (`combined_hollow_pyramid.nxs`) containing the
reconstructed data set as well as all metadata pertaining to the
reconstruction. Additionally, optional output figures (`.png`) may be saved to
an output directory specified in the pipeline file and can be viewed directly by any PNG image viewer.

1. Use NoMachine to visualize the output data with [NeXpy](https://nexpy.github.io/nexpy/), a high-level python interface to HDF5
files, particularly those stored as [NeXus data](http://www.nexusformat.org):
    1. Browse to https://nomachine.classe.cornell.edu
    1. Log in with your CLASSE ID
    1. Connect to `lnx201` (general purpose Linux login node)
    1. Select "Create a new virtual desktop"
    1. You will be guided through a short tutorial. Click "OK" to advance to the next screen.
    1. Click on the Terminal icon to open a terminal window
    1. Activate conda environment (see above)
    1. Open the NeXpy GUI by entering in your terminal:
       ```bash
       nexpy &
       ```
    1. After the GUI pops up, click File-> Open and navigate to the folder where
your output `.nxs` file was saved:
        1. Double-click on CLASSE_shortcuts folder
        1. Double-click on chess_[username] folder: This is a softlink to /nfs/chess/user/[username]
        1. Double-click on CHAP-Training-Examples-Materials -> example_02 -> output
        1. Select combined_hollow_pyramid.nxs
    1. Double click on the base level `NXroot` field in the leftmost "NeXus Data"
panel to view the reconstruction. Note that the `NXroot` name is always the
basename of the output file.
    1. Or navigate the file tree in the "NeXus Data" panel to inspect any other
output or metadata field. Note that the latest data set in any tomography
reconstruction workflow is always available under the "data" `NXdata` field
among the default `NXentry`'s fields (it is this data set that is opened in the
viewer panel when double clicking the `NXroot` field). The default `NXentry`
name is always the "title" field in the workflow's map configuration, in this
case "hollow_pyramid".
    1. When finished, quit NeXpy
    1. Log out of lnx201 by clicking on your username in the upper right corner


## Real experiment examples

A full tomographic reconstruction from an actual CHESS experiment can easliy take half an hour or longer, requires a fair amount of computational resources and generates tens of GBs of data. It is therefore not suitable for the purpose of this tutorial. However, there are two fully reconstructed datasets available to view with NeXpy to illustate examples of actual reconstructed samples measured here at CHESS, one for a sample of a tube filled with tiny ruby balls and one for a tick in a tube:

1. Open a NoMachine session and start NeXpy following the first 8 steps under item 4 in the Instructions above.
1. After the GUI pops up, click File-> Open and enter the following path in the File name box at the bottom: `/nfs/chess/user/x-cite/data/example_02`
1. Hit enter
1. You will be presented with two folders to choose from: `ruby_test` and `tick_test`. First Double-click of the ruby_test folder and select reconstructed.nxs
1. Select the "z" tab underneath the figure in the display panel and enter 1.5 in the box under the tab. Note that interactions in the GUI and refreshing of the figure will be somewhat slow due to the size of the dataset.
1. Select the "signal" tab underneath the figure in the display area and enter a range from -0.01 to 0.01 in the available boxes under the tab.
1. Under the same panel change the color scheme from the default of "viridis" to "grey" using the pull down menu.
1. Change to a log schale for the color bar by selecting the "Log" box.
1. Change the slicing direction in the viewer by selecting the "y" tab and changing it from the default of "y" to "z" in the pull down menu.
1. These are just a few examples of how to view data within NeXpy, feel free to play around some more with other options and repeat the exercise with the `tick_test` sample.

As a demonstration of the reconstruction, there are also movies slicing through each sample in the z-direction. To view these:

1. Click on the "Home" file folder on the NoMachine desktop to open the File Manager.
1. Enter `/nfs/chess/user/x-cite/data/example_02` directly in the file browser bar on the top.
1. Double-click on either `ruby_test` or `tick_test`.
1. Double-click on `recon_z.git`.
1. Repeat for the other sample.

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

### Activating the tomography conda environment

### Create simulated tomography data

1. Navigate to your `CHAP-Training-Examples-Materials/example_02` work
directory.
1. Run the simulation:
    ```bash
    CHAP pipeline_create_simdata.yaml
    ```
1. After completion, you should have a data directory in your work directory
with the SPEC data for a sample named "hollow_pyramid" of a simulated
tomography experiment on a tructaed hollow square pyramid on the CHESS id1a3
beamline.

### Running a tomography reconstruction

1. Navigate to your `CHAP-Training-Examples-Materials/example_02` work
directory.
1. Run the reconstruction:
   ```bash
   CHAP pipeline.yaml
   ```
1. Follow the interactive prompts or replace `true` with `false` on line 4 in
`pipeline.yaml` (`interactive: false`) and run the workflow non-interactively.

### Inspecting output

The output consists of a single NeXus (`.nxs`) file containing the
reconstructed data set as well as all metadata pertaining to the
reconstruction. Additionally, optional output figures (`.png`) may be save to
an output directory specified in the pipeline file.

Any of the optional output figures can be viewed directly by any PNG image
viewer. The data in the NeXus output file can be viewed in
[NeXpy](https://nexpy.github.io/nexpy/), a high-level python interface to HDF5
files, particularly those stored as [NeXus data](http://www.nexusformat.org):

1. Open the NeXpy GUI by entering in your terminal:
   ```bash
   nexpy &
   ```
1. After the GUI pops up, click File-> Open to navigate to the folder where
your output `.nxs` file was saved (the `output` directory in your work
directory), and select it ("combined_hollow_pyramid.nxs").
1. Double click on the base level `NXroot` field in the leftmost "NeXus Data"
panel to view the reconstruction. Note that the `NXroot` name is always the
basename of the output file.
1. Or navigate the filetree in the "NeXus Data" panel to inspect any other
output or metadata field. Note that the latest data set in any tomography
reconstruction workflow is always available under the "data" `NXdata` field
among the default `NXentry`'s fields (it is this data set that is opened in the
viewer panel when double clicking the `NXroot` field). The default `NXentry`
name is always the "title" field in the workflow's map configuration, in this
case "hollow_pyramid".


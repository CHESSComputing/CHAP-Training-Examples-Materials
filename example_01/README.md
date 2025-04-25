# Example 01

## Description
This example is the least complex. The example pipelines do the following:
1. Read in a series of 2D diffraction patterns.
1. Azimuthally integrate each diffraction pattern.
1. Save the resulting Intensity vs. radial coordinate data in .npz format.

### Physics Motivation
#### The input data
The 2D diffraction patterns used as input data for this pipeline represent fairly typical raw data collected during a powder diffraction experiment. In a powder diffraction experiment, the incident X-ray beam is scattered by the sample and the spatial pattern of scattered beam is captured on a 2D area detector. When the incident beam hits the sample at certain angles, the scattered X-rays between different crystal planes are in phase with each other and therefore constructively interfere to produce a signal on the detector. The angle at which this constructive interference can occur is determined by [Bragg's law](https://en.wikipedia.org/wiki/Bragg%27s_law): 

$$n\lambda = 2d\sin{\theta}$$

Where $n \in \mathbb{N}$, $\lambda$ is the wavelength of the incident beam, $d$ is the distance between crystal planes, and $\theta$ is the glancing angle of the incident beam relative to the sample's crystal planes.
| ![](https://github.com/keara-soloway/diagrams/blob/main/bragg_diffraction_screenshot_version.png) |
|:--:| 
| Illustration of Bragg diffraction. The lower ray has a path length which is $2dsin{\theta}$ longer than the upper ray. If the wavelength of the incident X-rays is equal to this value (or is a natural number multiple of it), then both rays leaving the sample have the same phase and will therefore constructively interfere with each other to produce a signal on the detector. Otherwise, the light rays will destructively interfere with each other and no signal will be produced on the detector. |

Because the sample is a powder, the diffraction pattern captured by the detector shows _rings_ of diffracted X-rays because the sample contains grains whose crystal planes are oriented at all directions relative to the incident beam.
| ![](http://pd.chem.ucl.ac.uk/pdnn/diff2/cone.gif) | 
|:--:| 
| How a powder diffraction experiment produces ring-like patterns. http://pd.chem.ucl.ac.uk/pdnn/diff2/kinemat2.htm|
#### Processing the data
In this particular experiment, we are interested in finding out the intensity of the diffracted X-rays as a function of the radial coordinate going out from the center of the beam -- this can be used to find out things like the distance between the sample's crystal planes. We are _not_ interested in the intensity of diffracted X-rays as a function of the angular coodinate going around each ring -- this would tell us the relative amount of the sample's crystal planes which are oriented in a certain direction (but beacuse our sample is a powder composed of many grains each oriented in an arbitrary direction, there should be no systematic relationship between the angular coordinate around the beam and the intensity of a ring at that angle). So, we reduce each 2D diffraction pattern into a 1D signal by integrating over the angular coordinate in each image, leaving us with intensity as a function of the radial coordinate.

## Instructions

1. Activate the conda environment. This ensures you will run the correct version of `python`, `CHAP`, and have all the extra third-party python modules available that are necessary for later steps in this example. Open a terminal and run:
    1. `source /nfs/chess/user/x-cite/miniconda3/bin/activate`
    1. `conda activate CHAP_example_01`

1. Process the input data using `CHAP`. In the same terminal used in step 1:
    1. Navigate to your `CHAP-Training-Examples-Materials/example_01` directory
    1. Inspect the contents of `pipline.yaml` by running `cat pipeline.yaml` -- this will print the contents of the file to your terminal. This file configures the CHAP pipeline you will run, so read the output. The file is meant to be human-readable, but don't expect to understand every detail. For now, just try to understand what the different pieces of the `pipeline` section are doing, how they fit together, and how the variables in the `config` section can be used to set the absolute locations of in/output files for the pipeline.
    1. Run the process: `CHAP pipeline.yaml` (this should take ~1min to complete)
    1. Check the output: `ls output`
        1.  Look for a file named `azimuthally_integrated.npz`

1. Visualize the input and output data used in this example with `matplotlib` (via a Jupyter notebook)
    1. Add the conda environment as a jupyter kernel. In the same terminal used in step 1 and 2, run:
        ```bash
        python -m ipykernel install --user --name=chap_example_01 --display-name "CHAP_example_01"
        ```
        This makes your active python environment avilable for _your_ use in the CLASSE JupyterHub. You will now be able to select this environment when running any notebook, meaning you will have access to the correct version of python and all the third-party modules you'll need for the notebook in this example. 
    1. (optional) We're now done using the terminal with this example, so deactivate the environment by running `conda deactivate; conda deactivate`. Close the terminal.
    1. In JupyterHub, navigate to the directory with the jupyter notebook:
        1. Double-click on CLASSE_shortcuts folder
        1. Double-click on chess_[username] folder: This is a softlink to `/nfs/chess/user/[username]`
        1. Double-click on CHAP-Training-Examples-Materials -> example_01
    1. Open the notebook by double-clicking on visualize.ipynb
    1. Select Kernel: choose CHAP_example_01
    1. Run the cells in order (click the right-triangle button or type Shift-Enter), complete the optional exercises, and the notebook close tab when done.

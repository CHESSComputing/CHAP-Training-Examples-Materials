# Example 01

## Description
This example is the least complex. The example pipelines do the following:
1. Read in a series of 2D diffraction patterns.
1. Azimuthally integrate each diffraction pattern.
1. Save the resulting Intensity vs. radial coordinate data in .npz format.

Note that there are two pipelines to choose from in this example: `pipeline_cbf.yaml` and `pipeline_h5.yaml`. They both do the same thing, but each one operates on a different set of input 2D diffraction data. `pipeline_cbf.yaml` will run slightly faster (~3 seconds as opposed to ~1 minute), but the data in this case are synthetic and not very interesting for visualization.

### Physics Motivation
#### The input data
The 2D diffraction patterns used as input data for this pipeline represent fairly typical raw data collected during a powder diffraction experiment. In a powder diffraction experiment, the incident X-ray beam is scattered by the sample and the spatial pattern of scattered beam is captured on a 2D area detector. When the incident beam hits the sample at certain angles, the scattered X-rays between different crystal planes are in phase with each other and therefore constructively interfere to produce a signal on the detector. The angle at which this constructive interference can occur is determined by [Bragg's law](https://en.wikipedia.org/wiki/Bragg%27s_law): 

$$n\lambda = 2d\sin{\theta}$$

Where $n \in \mathbb{N}$, $\lambda$ is the wavelength of the incident beam, $d$ is the distance between crystal planes, and $\theta$ is the glancing angle of the incident beam relative to the sample's crystal planes.
| ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Bragg_diffraction_2.svg/2560px-Bragg_diffraction_2.svg.png) | 
|:--:| 
| *By Hydrargyrum - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=17543875* |
| Illustration of Bragg diffraction. The lower ray has a path length which is $2dsin{\theta}$ longer than the upper ray. If the wavelength of the incident X-rays is equal to this value (or is a natural number multiple of it), then both rays leaving the sample have the same phase and will therefore constructively interfere with each other to produce a signal on the detector. Otherwise, the light rays will destructively interfere with each other and no signal will be produced on the detector. |

Because the sample is a powder, the diffraction pattern captured by the detector shows _rings_ of diffracted X-rays because the sample contains grains whose crystal planes are oriented at all directions relative to the incident beam.
| ![](http://pd.chem.ucl.ac.uk/pdnn/diff2/cone.gif) | 
|:--:| 
| How a powder diffraction experiment produces ring-like patterns. http://pd.chem.ucl.ac.uk/pdnn/diff2/kinemat2.htm|
#### Processing the data
In this particular experiment, we are interested in finding out the intensity of the diffracted X-rays as a function of the radial coordinate going out from the center of the beam -- this can be used to find out things like the distance between the sample's crystal planes. We are _not_ interested in the intensity of diffracted X-rays as a function of the angular coodinate going around each ring -- this would tell us the relative amount of the sample's crystal planes which are oriented in a certain direction (but beacuse our sample is a powder composed of many grains each oriented in an arbitrary direction, there should be no systematic relationship between the angular coordinate around the beam and the intensity of a ring at that angle). So, we reduce each 2D diffraction pattern into a 1D signal by integrating over the angular coordinate in each image, leaving us with intensity as a function of the radial coordinate.

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

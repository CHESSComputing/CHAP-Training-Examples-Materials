#!/usr/bin/env python
"""Script to generate input data for X-CITE / CHAP example no. 1.
To run:
```
./generate_input_data.py
```
"""

from pyFAI.test.utilstest import create_fake_data, test_options
from fabio.cbfimage import CbfImage as Image
test_options.TEST_RANDOM = True

# Number of detector data frames to generate. Recommended: keep
# n_frames <= 10 in the interest of conserving space, computing
# resources, and speed.
n_frames = 10

print(f'Saving {n_frames} frames of fake diffraction data.')

for i in range(n_frames):
    # Get a fake 2d diffraction pattern and corresponding azimuthal
    # integrator for the simulated detector / beam setup.
    data, ai = create_fake_data()

    if i == 0:
        # Save the .poni file only once.
        ai.save('input/detector.poni')
        print('Saved input/detector.poni.')

    # Save the diffraction pattern to an indexed .cbf file.
    img = Image(data=data)
    img.save(f'input/detector_data_{i:02d}.cbf')
    print(f'Saved input/detector_data_{i:02d}.cbf.')

print('Done.')

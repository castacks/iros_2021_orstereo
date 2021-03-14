
# Utilities for accessing the 4K stereo data used for evaluating ORStereo #

File access utilities for the data published with the IROS 2021 submission __ORStereo: Occlusion-Aware Recurrent Stereo Matching for 4K-Resolution Images__.

We collect 100 4K-resolution stereo images with true disparities and occlusion masks. This dastaset is used for evaluating our model's performance on 4K-resolution images. It is collected by AirSim in the Unreal engine. Get the dataset [here](https://cmu.box.com/s/28v8bxx9g9fu8odsqenefmjvexjsr2p7).

All utility functions are in __file_access_utils.py__. The utility depends on OpenCV. Use `pip install opencv-python` to install OpenCV. The utility has been tested with Python3.

The disparities are saved as 4-channel PNG files. We provide utility functions to read a single disparity file and convert the data into single-precision floating-point values (numpy.float32).

The occlusions are saved as single-channel PNG files. There is a function for reading an occlusion file as a boolean image.

For more details about the paper, please refer to the [project webpage](https://theairlab.org/orstereo).

Created by Yaoyu Hu \<yaoyuh@andrew.cmu.edu\>

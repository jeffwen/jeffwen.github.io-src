Title: Kalman Filters for Object Tracking
Date: 2017-11-15 03:21
Author: Jeff Wen
Category: Python
Slug: kalman_filter
Summary: Using C++ to implement an extended and unscented kalman filter for object tracking
Index_image_url: /images/sdcnd/extended_kalman_filter_index.png

_November 15, 2017_

[//]: # (Image References)

[dataset1]: /images/sdcnd/dataset1.png "Original dataset"
[dataset2]: /images/sdcnd/dataset2.png "Reversed dataset"
[lidar_only]: /images/sdcnd/lidar_only.png "Lidar only"
[radar_only]: /images/sdcnd/radar_only.png "Radar only"
[dataset1_unscented]: /images/sdcnd/dataset1_unscented.png "Original dataset"
[lidar_only_unscented]: /images/sdcnd/lidar_only_unscented.png "Lidar only"
[radar_only_unscented]: /images/sdcnd/radar_only_unscented.png "Radar only"
[lidar_nis]: /images/sdcnd/lidar_nis.png "Lidar NIS"
[radar_nis]: /images/sdcnd/radar_nis.png "Radar NIS"

This post will be less invovled than some of the other projects but you can look at the code for the [extended kalman filter](https://github.com/jeffwen/sdcnd_extended_kalman_filter) and [unscented kalman filter](https://github.com/jeffwen/sdcnd_unscented_kalman_filter) if you want more details! Also, if you want to read more about kalman filters and understand how these types of models work feel free to read this intuitive and well written [blog](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/).

In this project, we use an extended kalman filter and later an unscented kalman filter to predict the location and velocity of a simulated bicycle that is traveling around the vehicle. The measurement data comes from lidar and radar sensors with the main algorithm implemented in C++.

### Extended Kalman Filter
In the screenshots below, the green triangles represent the predicted location, the red circles are from the laser sensor, and the blue markers are from the radar sensor. We measure the accuracy of the algorithm by calculating the RMSE of the `x, y` positions and the velocity along the `x, y` axis. 

![alt text][dataset1]

* The original dataset starting with lidar measurement 

![alt text][dataset2]

* Reverse of the original dataset starting with radar measurement

If we just use one or the other of the sensor measurements to update the algorithm we can start to see what each sensor is better.

![alt text][lidar_only]

* The original dataset starting with lidar measurement and only using the lidar measurements to update to algorithm. We can see that compared to using both sources of sensor data the overall algorithm performs worse. 

![alt text][radar_only]

* The original dataset starting with lidar measurement and only using the radar measurements to update to algorithm. Compared to using only the lidar data, the radar only updated algorithm is worse at localizing the positon (higher RMSE for `x` and `y`).

### Unscented Kalman Filter 

![alt text][dataset1_unscented]

* The original dataset starting with lidar measurement 

Overall, the unscented kalman filter performs better than the extended kalman filter. The RMSE values are lower in general, but especially the velocity predictions are much better for the unscented kalman filter. One reason for this might be that mechanically, the unscented kalman filter doesn't employ a linear process model nor does it linearize the non-linear measurement model. Rather, it uses an [unscented transform](https://en.wikipedia.org/wiki/Unscented_transform) to approximate the non-linear transformation. With regards to the process model (or motion model), instead of a constant velocity model we switched to using a constant turn rate and velocity magnitude model, which is better able to model how objects behave in turns.

![alt text][lidar_only_unscented]

* Using only the lidar measurements, the overall algorithm performs worse especially with regard to the velocity predictions. 

![alt text][radar_only_unscented]

* Similar to the extended kalman filter case, using just the radar measurements, the algorithm performs worse then with just the lidar or both sensors. 

One difference in terms of the two filters is the use of the normalized innovation squared (NIS) metric to finetune the noise parameters that are used in the unscented kalman filter. The NIS metric gives an approximate idea of whether or not the parameters were initialized in the correct range. Specifically, the NIS follows a Chi-squared distribution and given the number of dimensions we can figure out what the value should be if we expect that only in 5% of the cases the NIS will exceed the value. In our case, for the radar measurement example we have 3 dimensions and the value that we expect to exceed 5% of the time is `7.815`. For the lidar, since there are 2 dimensions (the `x` and `y` position) the value we expect to exceed ~5% of the time is `5.991`.

![alt text][lidar_nis]

* For the lidar NIS, we see that only in about ~5% of the cases does the value of the NIS exceed the `5.991` value.

![alt text][radar_nis]

* Similarly, for the radar NIS, about ~5% of the time the NIS exceeds `7.815`

### Compile and Build
In order to compile and build this project, make sure that the following dependencies are met.

* `cmake`:
  * For Mac make sure that `cmake` is at least version 3.5
* `make`:
  * For Mac make sure that `make` is at least version 4.1
* `gcc/g++`:
  * For Mac make sure that `gcc/g++` is at least version 5.4
* `uWebSocketIO`
  * From the project directory run `install-mac.sh`, which should be linked to the necessary `cmakepatch.txt` file
  * In order to run the above shell script, `homebrew` should also be installed

Once the above dependencies are installed:

1. Clone this repository
2. Create a build directory and navigate into it
  * `mkdir build && cd build`
3. Compile 
  * `cmake .. && make`
4. Run the program
  * Make sure that the [Udacity simulator](https://github.com/udacity/self-driving-car-sim/releases) is installed
  * `./ExtendedKF` or
  * `./UnscentedKF`

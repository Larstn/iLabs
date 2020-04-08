# Recording an experiment for vLabs
## Step by Step Guide 

_Thank you for considering turning one of your laboratory experiments into an online 
Here, we explain how to turn your experiment into a data set. Turning your experiment into a data set can be some work, but once the process has been done once, the experiment can be displayed to as many people as you like on the internet._

_The amount of effort it requires to record an experiment depends on how much of your experiment is already computer controlled. If your experiment is already computer controlled, it is relatively easy and quick. If your experiment is not already computer controlled, this would be the first step to take._

## Controlling your Experiment with a computer
If your experiment is already computer controlled, you can skip this step. Your experiment is ready to be recorded! 

If your experiment is not computer controlled, we recommend using a RasberryPi (https://www.raspberrypi.org). You need to buy one RasberryPi and the HATs (Hardware on Top) that allow you to control the hardware of your experiment. All pieces of equipment that you want to be able to adjust or read out during a recording need to be computer controlled. You will also need one (or more) camera(s) to record images or videos of your experiment. We recommend using a PiCamera (https://projects.raspberrypi.org/en/projects/getting-started-with-picamera, https://picamera.readthedocs.io/en/release-1.13/ , https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS). You will need to write a set of simple functions to run on your Rasberry Pi to control all the equipment that you are using. Since RasberryPi has a big developer community, you can find a lot of help online!

Once your experiment is computer controlled - either with a RasberryPi or with a different solution, we can start to record it! 
Your Experiment as a Set of States
Recording your experiment requires you to think about your experiment as a set of finite states. To figure out what states your experiment can be in, you have to think about what the control variables of your experiment are. A control variable is anything that you can vary in your experiment. These can be the position of motion stages or a button that you can turn on or off. If your experiment changes over time, the amount of time passed is another control for your experiment. Think about controls in a broad sense: Anything that influences the experiment is an experimental control variable. 

For our purposes, we have two types of control variables: Buttons (A control that can only take two values, often On/Off) and Slides (A control that can have a high number of values). Each individual combination of values that control variables can take is a state of your experiment. 

To turn your experiment into an online experiment, please think about the states of your experiment. It is easier to digitize an experiment with fewer control variables. Try to think about the least number of control variables you would need, so that you can convey the point of the experiment and make the best use of the interactive features of the vLabs platform. Sometimes, you could break up an experiment into multiple experiments to reduce the complexity. If you have figured out the control variables for your experiment, you have already done a big part of the required work. 

#### Example: Diffraction Experiment 
_Throughout this guide, we will use the Diffraction Experiment as an example. The recording of the Diffraction experiment can be found online:  http://ilabs.education/showExperiment?exp_id=5187247892594688_

_The diffraction experiment has the following controls:_

- _Light (On/Off)_
- _Red Laser (On/Off)_
- _Green Laser (On/Off)_
- _Grating (5 different gratings are available)_
- _Position of the photodetector (about 283 positions)_

_Each unique combination of possible control values is a state of the diffraction experiment. Thus, the experiment has: 2 [Light] * 2 [Red Laser] * 2 [Green Laser] * 5 [Grating] * 283 [Photodetector] = 11,320 states. Even though this might sound like a lot of states, the recording of the diffraction experiment takes less than 2 hours and it can easily be uploaded to the vLabs platform._


## Digitalizing your experiment
To turn your experiment into a dataset that can be uploaded to the vLabs platform, you need to record it in all possible states. For this, you need to walk through all the possible combinations of the control variables and, once your experiment reached the state, record all data points (here called indicator data) associated with this state and take pictures with your camera. If your experiment is already computer controlled and you have an idea about how to vary your control, this is relatively straight forward. 
Recording the states
To record your experiment, you need code that runs through all states. For that, you need to either make adjustments to the code that currently runs your experiment or write a short new code piece importing the existing code that runs the experiment. Then, you need to write nested for-loops to run through all the states. You should use one for loop for each control. In each for loop, change the control value. In the innermost for-loop you also need to gather the indicator data, take pictures and then write the meta-data of this state into a file. For setting the control values, use the functions to control your hardware, e.g. over your RasberryPi. To gather your indicator data, use your function that controls the hardware that collects the data, e.g. a sensor. To take a picture, you need to run code that controls your camera. On our github, we provide you with a python function that allows you to write your state file. You can also write your own function - it is important that you store the data in the format that is described below. After your code run through all the states, you are done recording. 

#### Example
We are providing a short full example on how a code that can record an experiment can look like for the Diffraction experiment we described earlier. It can be found on this github repository, as [FullExample.py](FullExample.py). 
The example uses [CreateStateFile.py](CreateStateFile.py) and [writeStateFile.py](writeStateFile.py) functions that are also provided on this github. Before running the experiment, you need to run the CreateStateFile function once. The inputs are the number of numerical controls, boolean controls, indicators and, if any, noise types of the experiment. For the latter, you can indicate either “g” or “p” for Gaussian or Poisson Noise or “n” for any other kind of noise. If you want to record a noise type that is not Gaussian and Poisson, you need to include several sensor readings for each state. To do so, you need to include the same state multiple times into your data file, each of them with a different sensor reading. If you want to record Gaussian noise, you need to include the standard division of your noise into each of the states. The writeStateFile.py function has the optional inputs “noise” and “NoiseType” that you need to provide in this case. Both of them are lists, each element representing one indicator. If you want to record Poisson noise, you only need to include the list of noise types. Please see the python file for more detail. 

### Taking pictures with computer-controlled cameras
For an automated recording, you also need to control a camera with your computer. If you use a PiCamera, you can use the code we are providing on this github in python (see: [TakePicturePICam.py](TakePicturePICam.py)). You can see that the code to control the camera is relatively short. Controlling cameras with your computer is generally easy and there are many pre-build libraries that can help you with this. Please find some of them below: 

- https://picamera.readthedocs.io/en/release-1.13/
- http://simplecv.org
- https://opencv.org

### The data format 
If you need or want to write your own function to record the meta data of your experiment, you need to follow the correct data format. The format is as follows: 

[Header]:

number of controls:N_c,number of booleans:N_b,number of indicators:N_i, noise: gpn

[One Line per state, showing:]

Control Variable 1, Control Variable 2, .. Control Variable N, Boolean Control String(1,..N), Indicator Value 1(:Std {if Gaussian}), Indicator Value 2, … Indicator Value N, ImageName 1, Image Name 2, ... , Image Name N

You can find some example data files for the diffraction experiment on this repository (see: Diffraction Recording.txt and Diffraction Recording with Noise.txt) 

### Manual Recordings
Under some limited circumstances, it might be helpful to manually record your experiment. This will only be feasible, if your experiment has a very limited number of states. Yet, in this case, you do not need to make your experiment computer-controlled. If you want to do a manual recording, please use the data format provided above, take and associate pictures with your states and ensure, that you provide data for all possible states. 

## Uploading the experiment to the vLabs Platform
Once you recorded your experiment and your pictures and data file is ready, the upload is very straightforward. You only need to go on www.ilabs.education and log in using either your email address or any other service like Google. Please contact us at larstn@stanford.edu and tell us the email address that you are using, so we can add you to the list of people that is allowed to upload experiments (we are currently restricting access to the upload feature). Once we added you, you can click on “Create” and then follow some easy steps to upload your experiment. The menu is straight forward. There are two different instances that you can create: a laboratory and an experiment. An experiment is a sub-class of a laboratory. Think about the laboratory as some general container for a number of experiments, e.g. different diffraction experiments. They help you better sort your work. If you have any questions about the upload process, please feel free to reach out. 

## Participating in the vLabs development

We would like to make the vLabs project as openly available as possible. There are two ways for anyone to contribute. You can help by uploading functions that you used to record your experiments onto this repository, so other people can use them as inspiration. Another way to contribute is to help with the development of the platform. The repository for the platform is currently not public, since it includes several authentication keys that we are using to run it. However, we are always happy if anyone wants to join our team and bring some of their ideas for the platform to life. Contact us at larstn@stanford.edu, if you are interested! 

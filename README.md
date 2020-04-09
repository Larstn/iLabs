# Recording an experiment for iLabs
## Step by Step Guide 

_Thank you for considering turning one of your laboratory experiments into an online experiment._

_Here, we you can read about how to turn your experiment into a data set. This can require some effort, but once the process has been established, the experiment can be easily re-recorded and displayed to as many people as you like on the internet._

_The amount of effort it requires to record an experiment depends on what degree of your experiment is already computer controlled. If your experiment is already computer controlled, recording it is relatively easy and quick. If your experiment is not already computer controlled, this needs to be the first step to take._

## Controlling your Experiment with a computer
If your experiment is already computer controlled, you can skip this step. Your experiment is ready to be recorded! 

If your experiment is not computer controlled, we recommend using a [RasberryPi](https://www.raspberrypi.org). You need to buy one RasberryPi and the HATs (Hardware on Top) that allow you to control the hardware of your experiment. All pieces of equipment that you want to be able to adjust or read out during a recording need to be computer controlled. You will also need one (or more) camera(s) to record images or videos of your experiment. We recommend using a [PiCamera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera), see also [here](https://picamera.readthedocs.io/en/release-1.13/) or [here](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS). You will need to write a set of simple functions to control all your equipment. Since RasberryPi has a big developer community, you can find a lot of help online.

Once your experiment is computer controlled - either with a RasberryPi or with a different solution, we can start to record it! 

## Your Experiment as a Set of States
Recording your experiment requires you to think about your experiment as a set of finite states. To figure out what states your experiment can be in, think about what the control variables of your experiment are. A control variable is anything that you can vary in your experiment. These can be the position of motion stages or a button that you can turn on or off. If your experiment changes over time, the amount of time passed is another control variable for your experiment. Think about controls in a broad sense!

For our purposes, we defined two distinct types of control variables: Buttons (A control that can only take two values, often On/Off) and Slides or numerical controls (a control that can have a high number of values, anything more than 2). Each individual combination of values that control variables can take is a state of your experiment. 

To turn your experiment into an online experiment, please think about the states of your experiment. It is easier to digitize an experiment with fewer control variables and fewer states. Try to think about the lowest number of control variables that is required to convey the point of the experiment. Sometimes, you can break up an experiment into multiple experiments to reduce the complexity. If you have figured out the control variables for your experiment, you have already done a significant part of the required work. 

#### Example: Diffraction Experiment 
_Throughout this guide, we will use the Diffraction Experiment as an example. The recording of the Diffraction experiment can be found [online](http://ilabs.education/showExperiment?exp_id=5187247892594688)_

_The diffraction experiment has the following controls:_

- _Light (On/Off)_
- _Red Laser (On/Off)_
- _Green Laser (On/Off)_
- _Grating (5 different gratings are available)_
- _Position of the photodetector (about 283 positions)_

_Each unique combination of possible control values is a state of the diffraction experiment. Thus, the experiment has: 2 [Light] * 2 [Red Laser] * 2 [Green Laser] * 5 [Grating] * 283 [Photodetector] = 11,320 states. Even though this might sound like a lot of states, the recording of the diffraction experiment takes less than 2 hours and it can easily be uploaded to the iLabs platform._


## Digitalizing your experiment
To turn your experiment into a dataset that can be uploaded to the iLabs platform, you need to record it in all possible states. For this, you need software to walk through all the possible combinations of the control variables and, once your experiment reached the state, record all data points (here called indicator data) associated with this state. You also need to take pictures with your camera once you reached each state. If your experiment is already computer controlled and you thought about the possible values for each control, this is straight forward. 

### Recording the states
The code that allows your experiment to reach all possible states can be relatively simple. You can to either make adjustments to the code that currently runs your experiment or write a short new code piece importing the existing functions to control your hardware. You then need to write nested for-loops to run through the possible values of each control. You should use one for-loop for each control. In each for-loop, change the control value of one piece of equipment. For setting the control values, use the functions to control your hardware, e.g. over your RasberryPi.

In the innermost for-loop, you reach a new state. Here, you also gather the indicator data, take pictures and then write the meta-data of this state into a state file. The state file collects all data for the experiment. To gather your indicator data, use a function that controls the indicator, e.g. a sensor, and returns a value. To take a picture, you need to run code that controls your camera. On our github, we provide you with a python function that allows you to write the information of this state into the state file. For this, you can also write your own function - it is important that you store the data in the format that is described below. After your code run through all the states, you are done recording.

#### Example
We are providing a full example of code for the recording of the Diffraction experiment. It can be found on this github repository, as [FullExample.py](FullExample.py). 

The example uses [CreateStateFile.py](CreateStateFile.py) and [writeStateFile.py](writeStateFile.py) functions that are also provided on this github. Before running the experiment, you need to run the CreateStateFile function once. The inputs to this function are the number of numerical controls, boolean controls, indicators and, if any, noise types of the experiment. The writeStateFile function takes the current setting of the controls as well as the indicator data and picture names as input and then adds a data entry to the state file. 

### Including Noise 
You can include noise to your data recording, this is an optional feature. The addition of noise is straight forward. If your indicator data is noisy, it will vary over time. Thus, you can include the same state multiple times in your state file, each time with a different sensor reading. The iLabs platform will then display the different values for the state as noisy indicator data. 

### Taking pictures with computer-controlled cameras
For an automated recording, you also need to control a camera with your computer. If you use a PiCamera, you can use the code we are providing on this github in python (see: [TakePicturePICam.py](TakePicturePICam.py)). Code to control the camera can be relatively short. Controlling cameras with your computer is generally straight forward and there are many pre-build libraries that can help you with this. Please find some of them below: 

- https://picamera.readthedocs.io/en/release-1.13/
- http://simplecv.org
- https://opencv.org

### The data format 
If you need or want to write your own function to record the meta data of your experiment into a state file, you need to follow the correct data format. The format is as follows: 

[Header]:

number of controls:{N_controls for your experiment},number of booleans:{N_boolenas for your experiment},number of indicators:{N_indicators for your experiment}

[One Line per state, showing:]

{Value of Control 1}, {Value of Control 2}, .. {Value of Control N}, {String to describe value of boolean controls, e.g. 00010}, {Value of Indicator 1}, {Value of Indicator 2}, .. {Value of Indicator N}, {ImageName 1}, {Image Name 2}, ... , {Image Name N}

In this notation, please replace the parts in {} with the values in your experiment. You can find some example data files for the diffraction experiment on this repository (see: [Diffraction Recording.txt](Diffraction%20Recording.txt) and [Diffraction Recording with Noise.txt](Diffraction%20Recording%20with%20Noise.txt)) (The latter shows a way to include Gaussian Noise to your experiment, which differs from repeating the same state. For Gaussian noise, you can also indicate the standard deviation of each indicator data point as shown in the example.)

### Manual Recordings
Under some limited circumstances, it might be helpful to manually record your experiment. This will only be feasible, if your experiment has a very limited number of states. Yet, in this case, you do not need to make your experiment computer-controlled. If you want to do a manual recording, please use the data format provided above, take and associate pictures with your states and ensure that you provide data for all possible states. 

## Uploading the experiment to the iLabs Platform
Once you recorded your experiment and the pictures and state file is ready, the upload process is straightforward. You only need to go on www.ilabs.education and log in using either your email address or any other service like Google. Prior to your upload, please contact us at larstn@stanford.edu and tell us the email address that you are using, so we can add you to the list of people that are allowed to upload experiments (we are currently restricting access to the upload feature). 

On the platform, you can click on “Create” and then follow easy steps to upload your experiment. You will be walked through a step-by-step menu. There are two different instances that you can create: a laboratory and an experiment. An experiment is a sub-class of a laboratory. Think about the laboratory as some general container for a number of experiments, e.g. different diffraction experiments. They help you better sort your work. You first create a laboratory and then, you can add your experiments to this laboratory. If you have any questions about the upload process, please feel free to reach out. 

## Participating in the iLabs development
We would like to make the iLabs project as openly available as possible. There are two ways for anyone to contribute. You can help by uploading the functions that you used to record your experiments onto this repository. Then, other people can use them as inspiration. Another way to contribute is to help with the development of the platform. The repository for the platform is currently not public, since it includes several authentication keys for our different APIs. However, we are always happy if anyone wants to join our team and bring some of their ideas for the platform to life. Contact us at larstn@stanford.edu, if you are interested and we share the repository with you! 

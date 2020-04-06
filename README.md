Readme File vLabs

This repository is a collection of code snippets that help record an experiment so that it can be uploaded to the vLabs platform (www.ilabs.education)!

Right now, there are two files in this repository: 

WriteStateFile.py
createStateFile.py

These two simple python files are an initial starter to record the states of any experiment in the right format. You can use them as follows: 

createStateFile.py is used to create a text file that will record all states. You need to run it once in the beginning of your data collection. The inputs are the name, the number of numerical controls, the number of boolean controls, the number of data indicators and, if existing, their noise profiles of your experiment. 

The WriteStateFile.py file can be used to record an single state. This function should be called within the innermost for-loop of your experimental recording. The inputs are the name of your experiment and the current setting of your numerical controls, boolean controls, the data of your indicators, the name of the associated images and (optimal) the noise and noise profiles. 

Please see the file documentations for more detail. 
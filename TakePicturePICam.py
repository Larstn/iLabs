from picamera import PiCamera
from time import sleep

camera = PiCamera()

 def takePicture(ExperimentName, camera, N):
 	"""Takes Picture, input arguments:
 	ExperimentName: Name of your experiment, camera: camera object, N: individual identifier number for the image"""
 	ImageFilename = ExperimentName + 'Image{}.jpg'.format(N)
    camera.capture(ImageFilename)
    sleep(1)
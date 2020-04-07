from picamera import PiCamera
from time import sleep


 def takePicture(ExperimentName, camera, N):
 	ImageFilename = ExperimentName + 'Image{}.jpg'.format(N)
    camera.capture(ImageFilename)
    sleep(1)
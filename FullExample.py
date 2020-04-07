import numpy as np 

# Copy or import the StateFile Functions

def createStateFile(ExperimentName, Ncontrols, Nbooleans, Nindicators, NoiseProfiles = []):
  """creates the file to store the state data, Input: ExperimentName, NControls, NBooleans, Nindicators, [NoiseProfiles]"
  Experiment Name: Name of your experiment
  NControls: Number of numeric controls in the experiment
  NBooleans: Number of boolean controls in the experiment 
  Nindicators: Number of Indicators (data displays) in the experiment
  NoiseProfile [optional]: Noise Profile of the Indicators. String Type. If gaussian, use "g", if Poisson use "p", if no noise use "n"
"""
  FileName = "{}.txt".format(ExperimentName)
  iLabsFile = open(FileName, "w")

  if NoiseProfiles != []:
    Noise = ''.join([str(noise) for noise in NoiseProfiles])
    header = "number of controls:{},number of booleans:{},number of indicators:{},noise:{} \n \n".format(Ncontrols, Nbooleans, Nindicators, Noise)
  else: 
    header = "number of controls:{},number of booleans:{},number of indicators:{} \n \n".format(Ncontrols, Nbooleans, Nindicators)
  
  iLabsFile.write(header)
  iLabsFile.close()

def writeStateFile(ExperimentName, controls, booleans, indicators, imagenames, noise = [], NoiseProfiles = []):
  """Input: ExperimentName, controls, booleans, indicators, imagenames, [noise, NoiseProfiles]
    ExperimentName: String, Name of the Experiment
    controls: ListType, List of how the controls are set in this state 
    boolenas: ListType, List of how the booleans are set in this state
    indicators: ListType, List of indicator values at this state
    imagenames: ListType, List of all images associated with this state
    noise: ListType, if you provide noise type, provide one value for each indicator. Empty element, if poission or no noise, std if gaussian noise
    NoiseProfiles = ListType, provide noise with the profiles, List of strings, use "g" for Gaussian, "p" for Poission and "n" for no noise type or other noise
  """
  FileName = "{}.txt".format(ExperimentName)
  iLabsFile = open(FileName, "a")

  controlString = ','.join([str(control) for control in controls])
  booleanString = ''.join([str(boolean) for boolean in booleans])
  ImageString = ','.join([str(imagename) for imagename in imagenames])

  if noise != []: 
    indicatorList = []
    for n, NoiseProfile in enumerate(NoiseProfiles): 
      if NoiseProfile == 'g':
        indicatorList.append(str(indicators[n])+":"+str(noise[n]))
      else: 
        indicatorList.append(str(indicators[n]))
    indicatorString = ','.join(indicatorList)
  else: 
    indicatorString = ','.join([str(indicator) for indicator in indicators])
  
  state = "{},{},{},{} \n".format(controlString, booleanString, indicatorString, ImageString)
  iLabsFile.write(state)
  iLabsFile.close()

# Import or set the functions that control your equipment 
def SetPhotodetector(value):
  """Dummy Function to simulate the Photodetector"""
  return True

def SetGrating(value):
  """Dummy Function to simulate the Grating"""
  return True

def SetLight(value):
  """Dummy Function to simulate the Light"""
  return True

def SetRedLaser(value):
  """Dummy Function to simulate the Red Laser"""
  return True

def SetGreenLaser(value):
  """Dummy Function to simulate the Red Laser"""
  return True

def ReturnPhotodetector():
  """Dummy function to simulate the Photodetector"""
  return np.random.rand(1)[0]

def TakeImage(cnt):
  """Dummy function to simulate the camera"""
  return "Image"+str(cnt) + ".jpg"

#Set variables that describe your expiriment
ExperimentName = "Diffraction Experiment"
Ncontrols = 2
Nbooleans = 2
Nindicators = 1

#Set values that the equipment pieces are supposed to take 
PhotodetectorValues = np.linspace(0.1, 28.3, 283)
GratingValues = np.linspace(1, 5, 5)

#call createStateFile Function 
createStateFile(ExperimentName, Ncontrols, Nbooleans, Nindicators)
cnt = 0 

#create nested for loops for all controls 
for g in np.nditer(GratingValues):
  for p in np.nditer(PhotodetectorValues):
    for l in (0,1):
      for r in (0,1):
        for gr in (0,1):
          #in the innermost for loop, set the equipment into the state 
          cnt = cnt + 1
          SetGrating(g)
          SetPhotodetector(p)
          SetLight(l)
          SetRedLaser(r)
          SetGreenLaser(g)

          # Collect Data and Image
          Detector = ReturnPhotodetector()
          ImageName = TakeImage(cnt)
          #Call writeStateFile function 
          writeStateFile(ExperimentName, [g, np.round(p,1)], [l, r, gr], [Detector], [ImageName])


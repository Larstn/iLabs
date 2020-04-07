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
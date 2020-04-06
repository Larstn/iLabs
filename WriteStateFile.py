def writeStateFile(ExperimentName, controls, booleans, indicators, imagenames, noise = [], NoiseProfiles = []):
  FileName = "{}.txt".format(ExperimentName)
  iLabsFile = open(FileName, "a")

  controlString = ','.join([str(control) for control in controls])
  booleanString = ''.join([str(boolean) for boolean in booleans])
  ImageString = ','.join([str(imagename) for imagename in imagenames])

  if noise != []: 
    indicatorList = []
    for n, NoiseProfile in enumerate(NoiseProfiles): 
      print("n: {}, NoiseProfile: {}".format(n, NoiseProfile))
      if NoiseProfile == 'g':
        indicatorList.append(str(indicators[n])+":"+str(noise[n]))
      else: 
        indicatorList.append(str(indicators[n]))
    print("Indicator List: {}".format(indicatorList))
    indicatorString = ','.join(indicatorList)
  else: 
    indicatorString = ','.join([str(indicator) for indicator in indicators])
  
  state = "{},{},{},{} \n".format(controlString, booleanString, indicatorString, ImageString)
  iLabsFile.write(state)
  iLabsFile.close()
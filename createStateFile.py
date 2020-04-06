def createStateFile(ExperimentName, Ncontrols, Nbooleans, Nindicators, NoiseProfiles = []):
  FileName = "{}.txt".format(ExperimentName)
  iLabsFile = open(FileName, "w")

  if NoiseProfiles != []:
    Noise = ''.join([str(noise) for noise in NoiseProfiles])
    header = "number of controls:{},number of booleans:{},number of indicators:{},noise:{} \n \n".format(Ncontrols, Nbooleans, Nindicators, Noise)
  else: 
    header = "number of controls:{},number of booleans:{},number of indicators:{} \n \n".format(Ncontrols, Nbooleans, Nindicators)
  
  iLabsFile.write(header)
  iLabsFile.close()

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

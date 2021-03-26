from pxz import *
from PiXYZ_Studio_Scripts.demo import process
from PiXYZ_Studio_Scripts.FileUtils import *
from os.path import join

def processDirectory(inputDirectory, inputExtensions, outputDirectory, outputExtensions):
	# get recursively all files of the given extensions in the input directory
	inputFiles = getFilesInDirectory(inputDirectory, inputExtensions, True, False)
	
	# process each file
	for inputFile in inputFiles:
		# import the file
		io.importScene(join(inputDirectory,inputFile))
		
		# process the model
		process()
		
		# export to all wanted output extensions
		for extension in outputExtensions:
			io.exportScene(join(outputDirectory, replaceFileExtension(inputFile, extension)))
			
		# clear the scene
		scene.clear()

#processDirectory("U:/dloveridge/_User_Examples/bmerva/Whirlpool/QRefresh_Stl", ["stl"], "U:/dloveridge/_User_Examples/bmerva/Whirlpool/QRefresh_Fbx", ["fbx"])

from pxz import *

def process():
	allScene = [[scene.getRoot()]]

	# tessellate with maxSag=0.2mm and maxAngle=10deg
	algo.tessellate(allScene, 0.2, -1, 10)

	# repair with a tolerance of 0.1mm
	algo.repairMesh(allScene, 0.1)

	# remove through holes with diameter less than 10mm
	algo.defeature(allScene, True, False, False, 10)

	# remove hidden patches
	algo.hiddenRemoval(algo.SelectionLevel.Patches, 1024, 16)

	# delete patches to allow the decimation to remesh over the base CAD patches
	algo.deletePatches(allScene)

	# decimate with surfacic tolerance to 1mm, lineic tolerance to 0.1mm and normal distorsion tolerance to 5mm
	algo.decimate(allScene, 1, 0.1, 5)

#process()

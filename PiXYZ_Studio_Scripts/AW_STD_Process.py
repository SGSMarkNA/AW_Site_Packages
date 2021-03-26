def runit():
	all = [[scene.getRoot()]]
	algo.tessellate(all, 0.050000, -1.000000, -10.000000, -1.000000, True, algo.UVGenerationMode.NoUV, False, False, False)
	scene.deleteEmptyParts()
runit()
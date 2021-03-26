from pxz import *

# Returns the component instanciated by the occurrence
def getOccurrenceComponent(occurrence):
	return occurrence[-1] # Component is the last element of the occurrence array

# Remove all occurrence contained in occurrenceToRemove from allOccurrences
# and returns the resulting list
def substractOccurrences(allOccurrences, occurrenceToRemove):
	finalOccurrences = []
	for occ in allOccurrences:
		if occ not in occurrenceToRemove:
			finalOccurrences.append(occ)
	return finalOccurrences

# convert an occurrence list (which can contains assemblies and parts occurrence)
# to an occurrence list which contains only parts occurrences
def getPartOccurrencesFromOccurrences(occurrences):
	partOccurrences = []
	for occ in occurrences:
		partOccs = scene.getPartPaths(occ)
		partOccurrences.extend(partOccs)
	return partOccurrences

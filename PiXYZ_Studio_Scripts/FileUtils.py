from os import listdir
from os.path import isfile, isdir, join, normpath, splitext
import fnmatch

def getFilesInDirectory(directory, extensions, recursive, joinPath):
	files = []
	for f in listdir(directory):
		fullPath = join(directory, f)
		if isfile(fullPath):
			if extensions:
				# check extensions
				extOk = False
				for ext in extensions:
					if fnmatch.fnmatch(f.upper(), "*." + ext.upper()):
						extOk = True
						break
				if not extOk:
					continue
			if joinPath:
				files.append(normpath(fullPath))
			else:
				files.append(f)
		elif recursive and isdir(fullPath):
			dirFiles = getFilesInDirectory(fullPath, extensions, recursive, joinPath)
			if not joinPath:
				tmp = dirFiles
				dirFiles = []
				for file in tmp:
					dirFiles.append(normpath(join(f, file)))
			files.extend(dirFiles)
	return files

def replaceFileExtension(file, newExt):
	(root,ext) = splitext(file)
	return root + "." + newExt

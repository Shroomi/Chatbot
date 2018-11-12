import bz2

compressFilename = r'./output 5.bz2'
f = bz2.BZ2File(compressFilename, 'r')

for line in f:
	print(line)

f.close()
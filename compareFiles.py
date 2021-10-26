import os


pathComputer = os.getcwd() + "\Computer"
pathMobile = os.getcwd() + "\Mobile"
filesComputer = os.listdir(pathComputer)
filesMobile = os.listdir(pathMobile)
fileCompare = open(os.getcwd() + "\compare.txt", "w")
countComputer = 1
countMobile = 1
countFilesComputer = 0
countFilesMobile = 0
countDuplicateComputer = 0
countDuplicateMobile = 0

for x in filesComputer:
	countFilesComputer += 1
for x in filesMobile:
	countFilesMobile += 1

fileCompare.write("There are " + str(countFilesComputer) + " Musik files on the Computer \nThere are " + str(countFilesMobile) + " Musik files on your Mobile \n")
dif = countFilesComputer - countFilesMobile
if dif < 0:
	fileCompare.write("There are " + str(abs(dif)) + " Musik files less on your Computer \n\n")
elif dif > 0:
	fileCompare.write("There are " + str(abs(dif)) + " Musik files less on your Mobile \n\n")
elif dif == 0:
	fileCompare.write("There is a equal amount of Mobile files on your Computer and Mobile \n\n")

#write missing Files on Computer
fileCompare.write("Files Missing on Computer:\n")
for x in filesMobile:
	if x not in filesComputer:
		fileCompare.write(format(str(countComputer), "3") + " " + str(x) + "\n")
		countComputer += 1

#write missing Files on Mobile
fileCompare.write("Files Missing on Mobile:\n")
for x in filesComputer:
	if x not in filesMobile:
		fileCompare.write(format(str(countMobile), "3") + " " + str(x) + "\n")
		countMobile += 1
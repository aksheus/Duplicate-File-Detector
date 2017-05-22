from Detector import Detector
import os 
if __name__=='__main__':
	print("enter the path for the starting node in the directory tree: ")
	start=input() 
	assert isinstance(start,str)
	if not os.path.exists(start):
		print('path does not exist')
		exit(1)
	if not os.path.isdir(start):
		print('enter path not file')
		exit(2)
	detector= Detector(start)
	detector.FindAllDuplicates()
	duplicates=detector.SortedOutput()
	with open('duplicate_files.txt','w') as outfile:
		print('Duplicate files sorted by file size in bytes (rightmost number)',file=outfile)
		print(file=outfile)
		if duplicates!=[]:
			for d in duplicates:
				outstring=' '.join(str(x) for x in d)
				print(outstring,file=outfile)
		else:
			print('no duplicates here')

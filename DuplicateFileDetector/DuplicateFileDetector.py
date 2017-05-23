from Detector import Detector
import os 
if __name__=='__main__':
	print("enter the path for the starting node in the directory tree: ")
	start=input() 
	assert isinstance(start,str)
	print('enter the file that may be duplicated')
	search_file=input()
	assert isinstance(search_file,str)
	if not os.path.exists(start):
		print('path does not exist')
		exit(1)
	if not os.path.isdir(start):
		print('enter path not file')
		exit(2)
	detector= Detector(start)
	duplicates=detector.FindDuplicate(search_file)
	with open('duplicate_files.txt','w') as outfile:
		print('Duplicate files sorted by file size in bytes (rightmost number)',file=outfile)
		if duplicates!=[]:
			outstring=' '.join(str(x) for x in duplicates)
			print(outstring,file=outfile)
		else:
			print('no duplicate found',file=outfile)

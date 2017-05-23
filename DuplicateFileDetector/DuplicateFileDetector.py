from Detector import Detector
from Menu import Menu
import os 
if __name__=='__main__':
	menu=Menu(Title="File Duplicate Detector",Resolution='600x600')
	if menu.IsSingle:
		detector= Detector(menu.ChosenPath)
		duplicates=detector.FindDuplicate(menu.ChosenFile)
		with open('duplicate_files.txt','w') as outfile:
			print('Duplicate files sorted by file size in bytes (rightmost number)',file=outfile)
			if duplicates!=[]:
				outstring=' '.join(str(x) for x in duplicates)
				print(outstring,file=outfile)
			else:
				print('no duplicate file found',file=outfile)
	else:
		detector= Detector(menu.ChosenPath)
		detector.FindAllDuplicates()
		duplicates=detector.SortedOutput()
		with open('duplicate_files.txt','w') as outfile:
			print('Duplicate files sorted by file size in bytes (rightmost number)',file=outfile)
			if duplicates!=[]:
				for d in duplicates:
					outstring=' '.join(str(x) for x in d)
					print(outstring,file=outfile)
			else:
				print('no duplicate files found',file=outfile)


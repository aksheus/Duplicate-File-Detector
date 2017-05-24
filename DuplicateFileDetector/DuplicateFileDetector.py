from Detector import Detector
from Menu import Menu
import os 
import csv 
if __name__=='__main__':
	menu=Menu(Title="File Duplicate Detector",Resolution='600x600')
	if menu.IsSingle:
		detector= Detector(menu.ChosenPath)
		duplicates=detector.FindDuplicate(menu.ChosenFile)
		with open('duplicate_files.csv','w',newline='') as csvfile:
			writer=csv.writer(csvfile, delimiter=',')
			if duplicates!=[]:
				writer.writerow(['FileName','File Size'])
				writer.writerow([duplicates[0][duplicates[0].rfind('\\')+1:],str(duplicates[-1])])
				writer.writerow(['Locations'])
				for loc in duplicates[:-1]:
					writer.writerow([loc[:loc.rfind('\\')]])
			else:
				writer.writerow(['No Duplicates Found'])
	else:
		detector= Detector(menu.ChosenPath)
		detector.FindAllDuplicates()
		duplicates=detector.SortedOutput()
		with open('duplicate_files.csv','w',newline='') as csvfile:
			writer=csv.writer(csvfile, delimiter=',')
			if duplicates!=[]:
				for d in duplicates:
					writer.writerow(['FileName','File Size'])
					writer.writerow([d[0][d[0].rfind('\\')+1:],str(d[-1])])
					writer.writerow(['Locations'])
					for loc in d[:-1]:
						writer.writerow([loc[:loc.rfind('\\')]])
			else:
				writer.writerow(['No Duplicates Found'])


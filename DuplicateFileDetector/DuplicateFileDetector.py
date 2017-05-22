"""
traverse directory tree from given node and find all duplicate files and sort the output by the file sizes"""
import os
import hashlib
from collections import defaultdict
from operator import itemgetter
from multiprocessing import Pool
from Detector import Detector

def ComputeFileHashes(f,buffer_size=65536):
	try:
		with open(f,'rb') as hash_this:
			md5_hasher=hashlib.md5()
			while True:
				data=hash_this.read(buffer_size)
				if not data:
					break
				md5_hasher.update(data)
			return (f,md5_hasher.digest())
	except FileNotFoundError:
		pass 

def GetDuplicates(dup_dict):
	for key in dup_dict.keys():
		if len(dup_dict[key])>2:
			yield tuple(dup_dict[key])

def GenerateFiles(start):
	for base,dirs,files in os.walk(start):
		files_arg=(os.path.join(base,x) for x in files)
		for fi in files_arg:
			yield fi 


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

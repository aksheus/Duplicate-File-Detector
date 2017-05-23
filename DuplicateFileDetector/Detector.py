from collections import defaultdict
from multiprocessing import Pool
from operator import itemgetter
import os 
import hashlib

class Detector:
    """computes the duplicate files list accordingly
      all duplicates recusrsively or particular file duplicate if one exists """

    def __init__(self,SearchPath,PoolSize=None,BufferSize=65536,Threshold=2):
        self.SearchPath=SearchPath
        self.DuplicatesDict=defaultdict(list)
        self.PoolSize=PoolSize # need to is none check later on
        self.BufferSize=BufferSize
        self.Threshold=Threshold

    def GenerateFilesLocal(self):
        for base,dirs,files in os.walk(self.SearchPath):
            files_arg=(os.path.join(base,x) for x in files)
            for fi in files_arg:
                yield fi

    def ComputeFileHashes(self,f):
        try:
            with open(f,'rb') as hash_this:
                md5_hasher=hashlib.md5()
                while True:
                    data=hash_this.read(self.BufferSize)
                    if not data:
                        break
                    md5_hasher.update(data)
                return (f,md5_hasher.digest())
        except FileNotFoundError:
            pass # need to pass message that some files were missing !? 

    def FindAllDuplicates(self):
       pool=None
       if self.PoolSize is None:
            pool=Pool()
       else:
            pool=Pool(self.PoolSize)
       filenames=(x for x in self.GenerateFilesLocal()) # later will have check for remote not sure how that works yet so 
       file_and_hash=pool.imap(self.ComputeFileHashes,filenames)
       for f,h in file_and_hash:
           self.DuplicatesDict[h].append(f)
       # may add arguments to sort not based not on file size but other property ?? 
       for k in self.DuplicatesDict.keys():
           self.DuplicatesDict[k].append(os.path.getsize(self.DuplicatesDict[k][0])) # append size of duplicate files

    def GetDuplicates(self):
        for key in self.DuplicatesDict.keys():
            if len(self.DuplicatesDict[key])>self.Threshold:
                yield tuple(self.DuplicatesDict[key])

    def SortedOutput(self):
        duplicates=[ d for d in self.GetDuplicates()]
        duplicates.sort(key=itemgetter(-1),reverse=True) # largest duplicate files first 
        return duplicates

    def FindDuplicate(self,SearchFile):
        self.FindAllDuplicates() # need to do this anyway as more than one duplicate may exist
        target=self.ComputeFileHashes(SearchFile)[-1]
        return self.DuplicatesDict[target] # warning : returns []




     







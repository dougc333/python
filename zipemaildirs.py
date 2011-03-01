#!/usr/bin/python
import os
import sys
import zipfile
import time

# given directory, should return a zipfile with directory contents in it zipped up
def listFiles(dir,z,size):
	subdirlist = []
	for item in os.listdir(dir):
	  if os.path.isfile(os.path.join(dir,item)):
	    print "file", os.path.join(dir,item), "size:", os.path.getsize(os.path.join(dir,item))
            size = size + os.path.getsize(os.path.join(dir,item))
            z.write(os.path.join(dir,item),os.path.join(dir,item),zipfile.ZIP_DEFLATED)
	  else:
	    print "this is a subdir", os.path.join(dir,item)
	    subdirlist.append(os.path.join(dir,item))
	for subdir in subdirlist:
	  listFiles(subdir,z,size);



def testListFiles():
  t = os.path.abspath("/ebsvolume/data(emailsjobs)/DVD009_1")
  zf = zipfile.ZipFile("test.zip","w")
  start = time.time()
  size = 0
  listFiles(t,zf,size)
  end = time.time()
  zf.close()
  print 'elapsed time in mimutes:', (end-start)/60
  print 'size:',size


def newCode():
  p = os.path.abspath("/ebsvolume/data(emailsjobs)")
  listDirs = os.listdir(p)
  print "num dirs to zip", len(listDirs)
  for zipDir in listDirs:  
    print "we are going to zip:", zipDir, "to:", zipDir+".zip", "in path:", os.path.join(p,zipDir)
    zfileOfDir = zipfile.ZipFile(zipDir+".zip","w");
    size = 0
    listFiles(os.path.join(p,zipDir),zfileOfDir,size)
    zfileOfDir.close()
newCode()

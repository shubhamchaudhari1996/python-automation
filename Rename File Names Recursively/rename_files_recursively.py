import os
import sys

directory = os.path.dirname(os.path.realpath(sys.argv[0]))
for subdir, dirs, files in os.walk(directory):
 for filename in files:
  if filename.find('.jpg') > 0:
   subdirectorypath = os.path.relpath(subdir, directory)
   filepath = os.path.join(subdirectorypath, filename)
   newfilename = filepath.replace(".mp4","_mp4")
   print(newfilename)
   os.rename(filePath, newfilename)
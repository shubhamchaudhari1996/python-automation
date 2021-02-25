import os
import shutil

for dirpath, dirnames, filenames in os.walk ("FOLDER PATH"):
   for dirname in dirnames:
     if "2019" in dirname.lower ():
       path = os.path.join (dirpath, dirname)
       print ("Removing"), path
       shutil.rmtree (path)
       dirnames.remove (dirname)
	   
	   

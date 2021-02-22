import os,sys
folder = 'FOLDER PATH'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.jpeg', '.jpg')
       output = os.rename(infilename, newname)
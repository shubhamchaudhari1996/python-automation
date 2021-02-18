import os
from shutil import copyfile
folder_path = 'Folder Path'
os.chdir(folder_path)
for file in os.listdir(folder_path)
    ch = file[0:4]
    year = file[6:9]
    final_path = folder_path + '/' + ch + '>' + year + '/' + file + .mp4'
    copyfile(file, final_path)
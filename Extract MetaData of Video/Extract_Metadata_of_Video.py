import os

os.chdir(os.environ["PROGRAMFILES"] + "\\mediainfo")  # The folder where you installed MediaInfo
from MediaInfoDLL3 import MediaInfo, Stream

MI = MediaInfo()

def get_mediainfo_from(directory):
  for file in os.listdir(directory):
    MI.Open(directory + file)
    file_extension = MI.Get(Stream.General, 0, "FileExtension")
    duration_string = MI.Get(Stream.Video, 0, "Duration/String3")  # Length. "Duration" for ms
    fps_string = MI.Get(Stream.Video, 0, "FrameRate")
    width_string = MI.Get(Stream.Video, 0, "Width")
    height_string = MI.Get(Stream.Video, 0, "Height")
    aspect_ratio_string = MI.Get(Stream.Video, 0, "DisplayAspectRatio")
    frames_string = MI.Get(Stream.Video, 0, "FrameCount")
    local_created_date_string = MI.Get(Stream.General, 0, "File_Created_Date_Local")  # Date of copying
    local_modified_date_string = MI.Get(Stream.General, 0, "File_Modified_Date_Local")  # Date of filming

    if file_extension == "MP4":
      print("Extension: "+file_extension)
      print("Length: "+duration_string)
      print("FPS: "+fps_string)
      print("Width: "+width_string)
      print("Height: "+height_string)
      print("Ratio: "+aspect_ratio_string)
      print("Frames: "+frames_string)
      print("Created Date: "+local_created_date_string)
      print("Modified Date: "+local_modified_date_string)

    else:
      print("{} ain't no MP4 file!".format(file))

    MI.Close()

get_mediainfo_from('FOLDER PATH')  # The folder with video files

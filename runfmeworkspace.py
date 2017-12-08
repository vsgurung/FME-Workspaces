import subprocess
try:
  subprocess.call([r"D:\Program Files\FME\fme.exe",r"E:\My Learning Folder\FME\Workspace\SpatialIndexCreator.fmw"])
except Exception as e:
  print(e)

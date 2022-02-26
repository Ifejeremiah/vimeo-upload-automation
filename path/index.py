import os

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def process_path(path):
  absol = os.path.isabs(path)
  exists = os.path.exists(path)
  isFile = os.path.isfile(path)
  isDir = os.path.isdir(path)

  if absol and exists:
    if isFile:
      return path
    elif isDir:
       return newest(path)

  else:
    return 'Path to file does not exist'

import os

def is_empty(s):
    if not s or len(s) == 0:
        return True
    return False

def is_same_file_in_path(file, path):
    _, fileName = os.path.split(file)
    if fileName in os.listdir(path):
        if os.path.getsize(file) == os.path.getsize(os.path.join(path, fileName)):
            return True
        return False
    return False
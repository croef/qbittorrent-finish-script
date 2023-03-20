import sys
import shutil
import os
import re
import tool


DES_PATH = '/nas/video/'
DOWNLOAD_PATH = '/downloads'
SKIP_PATHS = ['a', 'personal']

CONTENT_ENUM_OTHER = "Other"
CONTENT_ENUM_MOVIE = "MOVIE"
CONTENT_ENUM_TV = "TV"
DEBUG=False

def mkdir(path):
    print('mkdir "{}"'.format(path))
    if not DEBUG:
        os.mkdir(path)

def move_file(ori, des):
    print('move file: "{ori}" to "{des}"'.format(ori=ori, des=des))
    if not DEBUG:
        shutil.copy(ori, des)

def move_path(ori, des):
    desPath = os.path.join(des, os.path.basename(ori))
    if os.path.exists(desPath):
        mkdir(desPath)
    for x in os.listdir(ori):
        oriPath = os.path.join(ori, x)
        if os.path.isdir(oriPath):
            move_path(oriPath, os.path.join(desPath, x))
            continue
        if tool.is_same_file_in_path(oriPath, desPath):
            continue
        move_file(oriPath, desPath)
             

def is_skip_path(path):
    for p in SKIP_PATHS:
        if os.path.join(DOWNLOAD_PATH, p) in path:
            return True
    return False

def is_tv(path):
    regex = r"\.[Ss]\d+\.|\.[Ss]\d+-[Ss]?\d+\.|\.[Ss]\d+$"
    if re.search(regex, path):
        return True
    return False


def identify_type(contentPath, rootPath):
    identifyPath = [contentPath]
    if not tool.is_empty(rootPath):
        identifyPath = [rootPath] + [os.path.join(rootPath, x) for x in os.listdir(rootPath)]
    for x in identifyPath:
        if is_tv(x):
            return CONTENT_ENUM_TV
    return CONTENT_ENUM_MOVIE

def main(contentPath, rootPath):
    if is_skip_path(contentPath) or is_skip_path(rootPath):
        return
    desPath = os.path.join(DES_PATH, identify_type(contentPath, rootPath))
    if tool.is_empty(rootPath):
        move_file(contentPath, desPath)
        return
    move_path(rootPath, desPath)
    


if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit(400)
    contentPath = sys.argv[1]
    rootPath = sys.argv[2]
    if len(sys.argv) > 3:
        DEBUG=sys.argv[3]
    main(contentPath=contentPath, rootPath=rootPath)

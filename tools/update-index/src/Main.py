#!/usr/bin/env python

import os
import sys
import json
import glob


NAME_DIR_SPAMS  = 'spams'
NAME_FILE_INDEX = 'index.json'
PATH_DIR_SCRIPT = os.path.abspath(__file__)
PATH_DIR_ROOT   = os.path.abspath(PATH_DIR_SCRIPT + '/../../../../')
PATH_DIR_SPAMS  = PATH_DIR_ROOT + '/' + NAME_DIR_SPAMS
PATH_FILE_INDEX = PATH_DIR_ROOT + '/' + NAME_FILE_INDEX


def append_dict_to_file_obj(DictItemInfo, ObjFile):
    ObjFile.seek(0, 2)
    if ObjFile.tell() == 0:
        ObjFile.write(json.dumps([DictItemInfo]).encode())
    else:
        ObjFile.seek(-1, 2)
        ObjFile.truncate()
        ObjFile.write(",\n".encode())
        ObjFile.write(json.dumps(DictItemInfo).encode())
        ObjFile.write(']'.encode())


def get_path_as_relative(PathFileFull):
    return PathFileFull.replace(PATH_DIR_ROOT + '/', '')


def get_list_files(PathDir):
    return glob.glob(PathDir + '/*/*.json', recursive=True)


def get_dict_iteminfo(PathFileFull):
    if os.path.isdir(PathFileFull):
        return {}
    if os.path.isfile(PathFileFull):
        NameFileJSON     = os.path.basename(PathFileFull)
        PathFileRelative = get_path_as_relative(PathFileFull)
        DictFileInfo     = {
            'name': NameFileJSON,
            'path': PathFileRelative
        }
        return DictFileInfo


def save_dirlist_as_json(PathDirTarget, PathFileToSave):
    ObjFile   = open(PathFileToSave, 'ab+')
    ListPaths = get_list_files(PathDirTarget)
    CountFile = 0

    for PathFileFull in ListPaths:
        DictItemInfo = get_dict_iteminfo(PathFileFull)

        if DictItemInfo != {}:
            append_dict_to_file_obj(DictItemInfo, ObjFile)
            CountFile += 1

    ObjFile.close()
    return CountFile


if __name__ == '__main__':
    Result = save_dirlist_as_json(PATH_DIR_SPAMS, PATH_FILE_INDEX)
    print(str(Result) + ' indexes written in "/index.json".')

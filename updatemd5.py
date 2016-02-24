#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
import hashlib
import os

def md5sum(fname):
    """计算文件的MD5值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(fname, basestring) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()

def DeepDir(fname):
    """
    递归检查目录
    """
    listdir = os.listdir(fname)
    for name in listdir:
        if name[0] == '.':
            continue
        print "name", name
        if os.path.isfile(name):
            print name,"\t", md5sum(name)
        elif os.path.isdir(name):
            DeepDir(name)
        #else:
        #    print "it's not a file"

def main():
    """ 检查路径
        如果未给入参，则检查当前目录
        如果给定参数，则检查是否为目录，如果是则检验给定目录的md5，否则退出
    """
    argvlen = len(sys.argv)
    path = ""
    if argvlen == 1:
        path = os.getcwd()
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            path = os.path.abspath(path)
        else:
            print "it's not a path"
            return
    DeepDir(path)

if __name__ == '__main__':
    main()

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
    try:
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
    except:
        pass

def DeepDir(fname):
    """
    递归检查目录
    """
    if not os.path.isdir(fname):
        print "it's not a path"
        return
    fname = os.path.abspath(fname)
    listdir = os.listdir(fname)
    for name in listdir:
        if name[0] == '.':
            continue
        path = os.path.join(fname, name)
        if os.path.isfile(path):
            print path,"\t", md5sum(path)
        elif os.path.isdir(path):
            DeepDir(path)
        else:
            print "it's not a file or a dir"

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
    DeepDir(path)

if __name__ == '__main__':
    main()

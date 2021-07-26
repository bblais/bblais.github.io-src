#!/usr/bin/env python

import os,sys
from dateutil.parser import parse
from datetime import datetime

def status_date(fname):
    with open(fname) as fid:
        lines=fid.readlines()

    found=False
    for line in lines:
        if line.startswith('status:'):
            found=True
            break
    
    if not found:
        s=None
    else:
        s=line.split(':')[1].lower().strip()

    found=False
    for line in lines:
        if line.startswith('date:'):
            found=True
            break
    
    if not found:
        d=None
    else:
        d=line.split(':')[1].lower().strip()
        dt=parse(d)

    return s,dt


base='content/publish'
for (path, dirs, files) in os.walk(base):
    for f in files:
        fname,ext=os.path.splitext(f)
        if not ext=='.md':
            continue

        print("[%s]" % f)
        s,dt=status_date(path+"/"+f)
        print(s,dt)
        if s=='published':
            print (path+"/"+f,dt.strftime("%A, %d %b %Y"),end="")
            if not dt:
                print(" no date given")
                continue

            if dt<=datetime.today():
                print(" to be published now.")

                start=path+"/"+f
                subpath=path.replace(base,"")
                if subpath.startswith('/'):
                    subpath=subpath[1:]

                print("path",path)
                print("subpath",subpath)
                end='content/articles/%s' % (subpath+"/"+f)
                cmd='mv "%s" "%s"' % (start,end)
                print("\t",cmd)
                os.system(cmd)

            else:
                print(" to be published later.")
                

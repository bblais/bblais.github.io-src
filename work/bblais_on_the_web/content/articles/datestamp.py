#!/usr/bin/env python
import os,sys,shutil
import datetime
import time


for fname in sys.argv[1:]:
    base,ext=os.path.splitext(fname)
    if ext!='.md':
        print("Skipping ",fname)
        continue
        
    newfname=base+"_.md"

    with open(fname) as fid:
        lines=fid.readlines()
        
    found=False
    for line in lines:
        if line.lower().startswith('date:'):
            found=True
            break
            
    if found:
        print("%s date found: %s" % (fname,line.strip()))
    else:
        newlines=[]
        dt=time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(fname)))
        
        for line in lines:
            newlines.append(line)
            if line.lower().startswith('title:'):
                newlines.append('Date: %s\n' % (dt)) 
        print(fname,"with date ",dt)
        
        with open(newfname,'w') as fid:
            fid.write(''.join(newlines))
            
        shutil.copystat(fname,newfname)
        os.remove(fname)
        os.rename(newfname,fname)
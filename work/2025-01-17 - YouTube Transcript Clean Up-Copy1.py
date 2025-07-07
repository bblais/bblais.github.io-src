#!/usr/bin/env python
# coding: utf-8

# In[6]:


with open("transcript.txt") as fid:
    lines=fid.readlines()
lines[:10]


# In[12]:


url="https://youtu.be/VrIvwPConv0?si=5nveCWNxdxPjsFcq&t=60"
url="https://youtu.be/VrIvwPConv0?si=5nveCWNxdxPjsFcq"
lines=[_.strip() for _ in lines[2:]]


# In[13]:


NS=""
last_time=0
duration_minutes=0.5
block=[]
for line in lines:
    if not line:
        continue
    if line[0] in '0123456789' and ':' in line:
        parts=line.split(":")
        if len(parts)==2:
            h=0
            m=int(parts[0])
            s=int(parts[1])
        else:
            h=int(parts[0])
            m=int(parts[1])
            s=int(parts[2])
            
        current_time=h*60+m+s/60
        seconds=int(current_time*60)
        if not block:
            block.append(f"{url}&t={seconds}: ")
            block.append(line)

        continue
            
    block.append(line)
    
    if current_time-last_time>duration_minutes:
        last_time=current_time
        NS+=' '.join(block)
        NS+="\n\n"
        block=[]
        
if block:
    NS+=' '.join(block)
    


# In[14]:


print(NS)


# In[ ]:





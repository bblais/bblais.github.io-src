#!/usr/bin/env python
# coding: utf-8

# In[2]:


transcripts=[
    ('transcript2.txt','https://youtu.be/OMBQwGzn_TE?si=-4uOYpjwp0_Pqdwt'),
    ('transcript3.txt','https://youtu.be/cXBIhtFyH9g?si=QmghzvOHtH7Cb23t'),
]


# In[9]:


fname,url=transcripts[1]


# In[10]:


with open(fname) as fid:
    lines=fid.readlines()
lines[:10]


# In[ ]:





# In[11]:


lines=[_.strip() for _ in lines]


# In[12]:


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
    


# In[13]:


print(NS)


# In[ ]:





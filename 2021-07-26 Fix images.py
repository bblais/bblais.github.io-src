#!/usr/bin/env python
# coding: utf-8

# In[10]:


fname='content/articles/art_math.md'


# In[11]:


with open(fname) as fid:
    lines=fid.readlines()


# In[12]:


stop=False
image_fname=None
for line in lines:
    if ':' in line:
        continue
    if not line.strip():
        continue
    if line.startswith("!["):
        image_fname=line.split("(")[1].split(")")[0]
        break
        
    break
    
if image_fname:
    print(image_fname)
    new_lines=[]
    flag=False
    for line in lines:
        if ':' in line:
            new_lines.append(line)
            continue
            
        if not line.strip() and not flag:  # only do first
            flag=True
            continue
            
        if line.startswith("!["):
            new_lines.append("image: %s\n" % image_fname)
            new_lines.append("\n")
            continue

        new_lines.append(line)
        
    print(fname)
    with open(fname,'w') as fid:
        fid.write(''.join(new_lines))


# In[ ]:





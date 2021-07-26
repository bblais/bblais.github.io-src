
# coding: utf-8

# In[10]:


with open('bblaisontheweb-2019-01-24T14_54_12.007312-links.csv') as fid:
    all_lines=fid.readlines()
    
print(len(all_lines))


# In[28]:


lines=[line for line in all_lines if 
       line.startswith('https://bblais.github.io') or 
       line.startswith('http://bblais.github.io')]

lines=[line for line in lines if not 'nikola' in line]

print(len(lines))


# In[29]:


lines=[line.strip().split('?')[0] for line in lines]


# In[30]:


lines[0]


# In[31]:


ls ../output/


# In[43]:


import fnmatch
import os

with open('migration.csv','w') as fid:


    for line in lines:
        if line.endswith('/'):
            slug=line.split('/')[-2]
        else:
            slug=line.split('/')[-1]

        slug=slug.split('.html')[0]


        matches = []

        if '/pages/' in line:
            walk='../output/pages/'
        else:
            walk='../output/posts/'

        for root, dirnames, filenames in os.walk(walk):
            for filename in fnmatch.filter(filenames, slug):
                matches.append(os.path.join(root, filename))
            for dirname in fnmatch.filter(dirnames, slug):
                matches.append(os.path.join(root, dirname))

        if len(matches)==1:
            match=matches[0].replace('../output/','https://bblais.github.io/')
            fid.write('%s,%s\n' % (line,match))
            #print(line,'==>',match)
        elif len(matches)==0:
            print(line,'==>',None)
            fid.write('%s,%s\n' % (line,' '))
        else:
            raise ValueError("More than one match for ",line)


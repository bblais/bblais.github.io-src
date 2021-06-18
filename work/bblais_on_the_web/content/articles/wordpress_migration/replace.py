import fileinput
for line in fileinput.input(inplace=True,backup='.bak'):
    if line.strip('\n')=="Category: Uncategorized":
        continue
        
    line=line.replace("Category: ","Tags: ")
    line=line.replace("![]","!")
    
    line=line.replace("http://brianblais.wordpress.com/2013/02/27/unbelievable-project-a-non-believers-armchair-perspective-on-six-years-of-christian-debates/","http://web.bryant.edu/~bblais/unbelievable-project-a-non-believers-armchair-perspective-on-six-years-of-christian-debates.html")
    
    print line.strip('\n')
    

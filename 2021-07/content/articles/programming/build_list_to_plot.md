title: Common Python Pattern - Building Up Lists To Plot
date: 2/24/2020
image: artmath.jpg

I find that a common pattern I implement again and again in Python is to build up a list (or multiple lists) in a loop and turn them into arrays at the end for plotting or further calculating.  An example that stores 4 lists of a [SIR compartmental model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model) would look like,

```python
t=0
S=100
I=1
R=0

β=0.1
γ=0.1

dt=0.01

t_arr=[t]
S_arr=[S]
I_arr=[I]
R_arr=[R]

for t in arange(0,10,dt):
    
    dS=(-β*S*I)*dt
    dI=(+β*S*I - γ*I)*dt
    dR=(+γ*I)*dt
    
    S+=dS
    I+=dI
    R+=dR

    t_arr.append(t)
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)
    
t,S,I,R=array(t_arr),array(S_arr),array(I_arr),array(R_arr)
    
plot(t,S)
plot(t,I)
```

Notice the repetition.  I get the same pattern running through the values of a parameter, calculating a result, but then wanting to make a plot of the result vs the parameter.   For the loop I have to seemingly choose between,

```python
param_arr=linspace(0,3,100)

result_arr=[]
for param in param_arr:
    result=some_calculation(param)
    
    result_arr.append(result)
    
result_arr=array(result_arr)

plot(param_arr,result_arr)
```

Or

```python
param_arr=[]
result_arr=[]
for param in linspace(0,3,100):
    result=some_calculation(param)
    
    result_arr.append(result)
    param_arr.append(param)
    
result_arr=array(result_arr)
param_arr=array(param_arr)

plot(param_arr,result_arr)
```

Or

```python
param_arr=linspace(0,3,100)
result_arr=zeros(len(param_arr))

for i,param in enumerate(param_arr):
    result=some_calculation(param)    
    result_arr[i]=result
    
plot(param_arr,result_arr)
```

The first two solutions seem to have a lot of repetition, and two variables for every one I want to save. The last one seems a bit ugly, and forces me to remember to have an index variable (enumerate or counter), and won't work if I don't know the sizes ahead of time.  I’d love to know if there is a standard solution to this common pattern.   Here’s one that I came up with, which I don’t think it optimum but at least solves the immediate problem.  Defining a Storage class,

```python
class Storage(object):
    def __init__(self):
        self.data=[]
    
    def __add__(self,other):
        s=Storage()
        s+=other
        return s
        
    def __iadd__(self,other):
        self.append(*other)
        return self
        
    def append(self,*args):
        if not self.data:
            for arg in args:
                self.data.append([arg])

        else:
            for d,a in zip(self.data,args):
                d.append(a)
       
    def arrays(self):
        for i in range(len(self.data)):
            self.data[i]=array(self.data[i])

        ret=tuple(self.data)
        if len(ret)==1:
            return ret[0]
        else:
            return ret

    def __array__(self):
        from numpy import vstack
        return vstack(self.arrays())
```

I can rewrite the above SIR model with 

```python
t=0
S=100
I=1
R=0

β=0.1
γ=0.1

dt=0.01
data=Storage()
data+=(t,S,I,R)

for t in arange(0,10,dt):
    
    dS=(-β*S*I)*dt
    dI=(+β*S*I - γ*I)*dt
    dR=(+γ*I)*dt
    
    S+=dS
    I+=dI
    R+=dR

    data+=(t,S,I,R)
    
t,S,I,R=array(data)
    
plot(t,S)
plot(t,I)
```

And the parameter exploration example with,

```python
data=Storage()
for param in linspace(0,3,100):
    result=some_calculation(param)
    
    data+=(param,result)

param,result=array(data)

plot(param,result)
```

What do you think?


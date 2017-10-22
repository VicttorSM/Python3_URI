a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if(a<b):
  if(a<c):
    print(a)
if(b<c):
  if(b<a):
    print(b)
if(c<a):
  if(c<b):
    print(c)
    
if(b>a>c):
  print(a)
if(a>b>c):
  print(b)
if(a>c>b):
  print(c)
  
if(c>a>b):
  print(a)
if(c>b>a):
  print(b)
if(b>c>a):
  print(c)

if(a>b):
  if(a>c):
    print(a)
if(b>c):
  if(b>a):
    print(b)
if(c>a):
  if(c>b):
    print(c)

print("")
print(a)
print(b)
print(c)

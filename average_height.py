import random
heights=input("plz Enter student heights?").split()
stu=list(map(int,heights))
height=0
for n in stu:
   height=height+n
print(height)  

# for iteration
b=0
for a in stu:
   b=b+1
print(b)

#
avg=round(height/b)
print(f"now average height::{avg} ")
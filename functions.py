def myfun(name):
    print(f"hello name is {name}")
    
myfun("aqib")

# 
# 
height=int(input('Enter height of wall:'))
width=int(input('Enter height of wall:'))
coverage=5
def painarea(height,width,coverage):
    result=round((height*width)/coverage)
    
    print(f"The cans used of paint:{result}")
    
painarea(height,width,coverage)
import random
row1=["🫨","🫨","🫨"]
row2=["🫨","🫨","🫨"]
row3=["🫨","🫨","🫨"]
Map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Please Enter where u want to hide treasure?")
vertical=int(position[0])
horizaontal=int(position[1])
Map[vertical-1][horizaontal-1]="xx"
print(f"{row1}\n{row2}\n{row3}")
 
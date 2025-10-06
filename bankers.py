import random

names=input("plz Enter name of persons:")
names=names.split()
len_names=len(names)
ran_len=random.randint(0,len_names-1)
person_who_pay=names[ran_len]
print(f"the person who is going to pay the bill {person_who_pay}")
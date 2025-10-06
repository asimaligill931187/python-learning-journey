name1=input(print("Enter your name:"))
name2=input(print("Enter your crush name"))
combined_name=name1+name2

# now count love
combined_name_lower=combined_name.lower()
l=combined_name_lower.count('l')
o=combined_name_lower.count('o')
v=combined_name_lower.count('v')
e=combined_name_lower.count('e')
love=l+o+v+e
# count for true
t=combined_name_lower.count('t')
r=combined_name_lower.count('r')
u=combined_name_lower.count('u')
e=combined_name_lower.count('e')
true=t+r+u+e
# final score
final_score=int(str(love)+str(true))
if final_score>10 or final_score<90:
    print(f"your love score is {final_score} ur good")
elif final_score>=40 or final_score<=50:
    print(f"your are alright ur score is {final_score}")
else:
    print("your not good")

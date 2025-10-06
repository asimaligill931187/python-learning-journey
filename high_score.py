student_scores= input("input a list of scores:").split()
for n in range(0,len(student_scores)):
    student_scores[n]= int(student_scores[n])
    
max_number=student_scores[0]

for number in student_scores:
    if number>max_number:
        max_number=number
        
print(f"max number is:{max_number}")  
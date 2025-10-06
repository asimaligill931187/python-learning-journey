student_score={"harry": 81,
               "ron":78,
               "AJ":99,
               "Ali":62,
               "zain":73,             
}

student_grades={
    
    
}


for score_key in student_score:
    if student_score[score_key]>=91 and student_score[score_key]<=100:
        student_grades[score_key]="Outstanding"
    elif student_score[score_key]>=81 and student_score[score_key]<=90:
        student_grades[score_key]="Exceeds"
    elif student_score[score_key]>=71 and student_score[score_key]<=80:
        student_grades[score_key]="Acceptable"
    elif  student_score[score_key]<=70:
        student_grades[score_key]="Fail"
print(student_grades)
    
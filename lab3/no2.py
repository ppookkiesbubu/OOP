def add_score(subject_score,student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject:score})
    else:
        subject_score.update({student:{subject:score}})
    return subject_score

def calc_average_score(subject_score):
    total = 0
    count = 0
    finish = {}
    for name in subject_score.keys():
        score_dict = subject_score[name]
        for j in score_dict.values():
            total += j
            count +=1
    total = total/count
    finish.update({name:'%0.2f'%total})
    return finish

subject_score = { '65010001' : { 'python' : 50 } }
student = '65010001'
subject = 'calculus'
score = 60
add_score(subject_score,student, subject, score)
print(calc_average_score(subject_score))

    
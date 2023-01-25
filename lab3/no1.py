def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    total = 0
    score_dict = {}
    score_dict.update(subject_score)
    for i in score_dict:
        total += score_dict[i]
    total = total/len(score_dict)
    return '%.2f'%total


    
print(calc_average_score())
    
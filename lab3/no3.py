def is_plusone_dictionary(d):
    total = 0
    before = 0
    for i in d.keys():
            if d[i]-i == 1 and i - before ==1:
                total += 1
                before = d[i]
    print(total)           
    if total == len(d):
        return True
    else:
        return False
d = {1:2, 3:4, 5:6, 7:8}
print(is_plusone_dictionary(d))






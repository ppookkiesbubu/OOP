def char_count(str):
    char_dict = {}
    total = 1
    for i in str:
        if char_dict.get(i):
            char_dict.update({i:char_dict[i]+1})
        else:
            char_dict.update({i:total})
    return char_dict
print(char_count('pooky'))
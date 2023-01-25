num_str = input()
num_split = num_str.split()
num_num = list(map(int,num_split))
num_num.sort()
a = num_num.count(0)
num_num[0],num_num[a] = num_num[a],num_num[0]
for i in range(len(num_num)):
    print(num_num[i],end='')
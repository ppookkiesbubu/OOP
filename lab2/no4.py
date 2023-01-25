def count_minus(str = input().split()):
    total = [i for i in str if int(i)<0]
    return len(total)
print(count_minus(

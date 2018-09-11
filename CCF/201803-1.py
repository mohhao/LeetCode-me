l = input().split()
scores = 0
flag = 0
ruler = 2
for index, value in enumerate(l):
    if value == '0':
        break
    else:
        if value == '2':
            if flag == 0:
                scores += ruler
                flag = 1
            else:
                ruler += 2
                scores += ruler
        else:
            scores += 1
            ruler = 2
            flag = 0
print(scores)
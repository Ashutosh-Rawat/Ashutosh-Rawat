arr = [1, 2, 3, 4, 5, 7, 8, 10, 12]
count = 1
flag = False
for i in arr:
    if count == i:
        count += 1
        continue
    else:
        print("missing number:", count)
        count += 2
        flag = True

if not flag:
    print("no number missing")

case = int(input())
for i in range(case):
    start,end= input().split(" ")
    for j in range(int(start), int(end)+1):
        counter = 0
        for k in range(2, j):
            if j % k == 0:
                counter += 1
                break
        if counter == 0 and j != 1:
            print(j)
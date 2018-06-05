point = [90, 25, 67, 45, 80]
number = 0
for result in point:
    number = number + 1
    if result < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

point = [1, 2, 3, 4, 5, 6, 66, 90, 100]
for result in point:
    if result % 3 == 0:
        print(result)
        break

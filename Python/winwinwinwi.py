def getDayName(a,b):
    answer = ""
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [0,31,59,90,120,151,181,212,243,273,304,334]
    sum = month[a-1] + b
    answer = day[sum%7]
    return answer

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
korean = {
    '오상원': 90,
    '박찬우': 91,
    '김문수': 92
}
english = {
    '오상원': 92,
    '박찬우': 91,
    '김문수': 90
}
math = {
    '오상원': 91,
    '박찬우': 90,
    '김문수': 92
}
science = {
    '오상원': 90,
    '박찬우': 91,
    '김문수': 92
}


def score(a):
    if a in korean.keys():
        print("{}님의 국어 점수는 {}점 입니다.".format(a, korean[a]))
    else:
        print("{}님의 국어 점수는 존재하지 않습니다.".format(a))
    if a in math.keys():
        print("{}님의 수학 점수는 {}점 입니다.".format(a, math[a]))
    else:
        print("{}님의 수학 점수는 존재하지 않습니다.".format(a))
    if a in english.keys():
        print("{}님의 영어 점수는 {}점 입니다.".format(a, english[a]))
    else:
        print("{}님의 영어 점수는 존재하지 않습니다.".format(a))
    if a in science.keys():
        print("{}님의 과학 점수는 {}점 입니다.".format(a, science[a]))
    else:
        print("{}님의 과학 점수는 존재하지 않습니다.".format(a))


def add(d):
    if d == '1':
        c = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if c != korean.keys():
            e = int(input("점수를 입력해 주세요: "))
            korean[c] = e
        else:
            print("다시 입력하세요!!")
    elif d == '2':
        c = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if c != math.keys():
            e = int(input("점수를 입력해 주세요: "))
            math[c] = e
        else:
            print("다시 입력하세요!!")
    elif d == '3':
        c = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if c != english.keys():
            e = int(input("점수를 입력해 주세요: "))
            english[c] = e
        else:
            print("다시 입력하세요!!")
    elif d == '4':
        c = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if c != science.keys():
            e = int(input("점수를 입력해 주세요: "))
            science[c] = e
        else:
            print("다시 입력하세요!!")
    else:
        print("다시 입력하세요!!")


def delete(f):
    if f == '1':
        g = str(input("삭제하실 분의 성함을 입력해 주세요: "))
        if g == korean.keys():
            del korean[g]
            print("삭제되었습니다.")
        else:
            print("다시 입력하세요!!")
    elif f == '2':
        g = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if g == math.keys():
            del math[g]
            print("삭제되었습니다.")
        else:
            print("다시 입력하세요!!")
    elif f == '3':
        g = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if g == english.keys():
            del english[g]
            print("삭제되었습니다.")
        else:
            print("다시 입력하세요!!")
    elif f == '4':
        g = str(input("추가하실 분의 성함을 입력해 주세요: "))
        if g == science.keys():
            del science[g]
            print("삭제되었습니다.")
        else:
            print("다시 입력하세요!!")
    else:
        print("다시 입력하세요!!")


while True:
    b = int(input("1.조회 2.추가 3.삭제 4.종료: "))
    if b == 1:
        a = str(input("성함을 입력하세요: "))
        score(a)
    elif b == 2:
        d = str(input("추가하실 성적의 과목 선택: 1.국어 2.수학 3.영어 4.과학: "))
        add(d)
    elif b == 3:
        f = str(input("삭제하실 성적의 과목 선택: 1.국어 2.수학 3.영어 4.과학: "))
        delete(f)
    elif b == 4:
        break
    else:
        print("다시 입력해주세요!!")

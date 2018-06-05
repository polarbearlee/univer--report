import dic
user = input("1.더하기  2.빼기  3.곱하기  4.나누기:")
a = int(input("첫번째 정수 입력"))
b = int(input("첫번째 정수 입력"))

if user == '1':
    print("{}더하기 {}은(는) {} 입니다.".format(a, b, dic.sum(a, b)))
elif user == '2':
    print("{}빼기 {}은(는) {} 입니다.".format(a, b, dic.diff(a, b)))
elif user == '3':
    print("{}곱하기 {}은(는) {} 입니다.".format(a, b, dic.multi(a, b)))
elif user == '4':
    print("{}나누기 {}은(는) {} 입니다.".format(a, b, dic.div(a, b)))
else:
    print("재대로 입력하세욤")


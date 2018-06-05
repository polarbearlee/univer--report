def fibonacci1(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return (a)
x = int(input("n값 입력: "))
print(fibonacci1(x))
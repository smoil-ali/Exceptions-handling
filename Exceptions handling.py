T = int(input())
for x in range(T):
    val = input().split()
    a = val[0]
    b = val[1]
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)



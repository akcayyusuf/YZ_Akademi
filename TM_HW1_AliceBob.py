def compareTriplets(a,b):
    points=[0,0]
    for i in range(3):
        if a[i]>b[i]:
            points[0]+=1
        elif a[i]<b[i]:
            points[1]+=1
    print(points[0],points[1])

alice=list(map(int,input().split()))
bob=list(map(int,input().split()))

compareTriplets(alice,bob)
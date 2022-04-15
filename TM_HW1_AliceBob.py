def compareTriplets(a,b):
    points=[0,0] #initialize scores

    #check for all inputs
    for i in range(3):
        if a[i]>b[i]:
            points[0]+=1
        elif a[i]<b[i]:
            points[1]+=1
    print(points[0],points[1])

alice=list(map(int,input().split())) #Get alice inputs
bob=list(map(int,input().split())) #Get bob inputs

compareTriplets(alice,bob)
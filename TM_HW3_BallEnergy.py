def sigma(n,h):

    if n < 1 or n > 10**5:
        return "Pleae insert valid array size!\n"

    for k in h:
        if k<1 or k>10**5:
            return "Please insert valid height for lego!\n"
    if len(h)!=n:
        return "Input dimensions not correct ! \n"

    tot=0
    for i in range(n):
        tot+=(2**n)*(h[i]/2**(i+1))

    Eo = int(tot//(2**n)+ (tot % 2**n > 0))
    return Eo

size=int(input("Please insert number of legos [1-10^5]: "))
heightArr=list(map(int,input("Please insert height of legos for every height[1-10^5]: ").split()))

print(sigma(size,heightArr))

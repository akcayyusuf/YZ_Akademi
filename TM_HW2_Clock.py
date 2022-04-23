def timeInWords(h,m):

    if h < 1 or h > 23 or m < 0 or m > 59:
        return "Pleae insert valid expression!\n"

    if h>12:
        h=h-12  ##Convert to 12 Hour Format

    nums=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen"
           ,"quarter","sixteen","seventeen","eighteen","nineteen"]
    decs=["","","twenty ","thirty ","fourty ","sixty "]

    if m==0:
        return nums[h]+" o' clock"

    if m==15:
        return nums[m]+" past "+nums[h]

    if m==30:
        return "half past "+nums[h]

    if m==15:
        return nums[m]+" to "+nums[h+1]


    if m>=1 and m<30:
        return decs[m//10]+nums[m%20]+" minutes past "+nums[h]
    else:
        m=60-m
        return decs[m//10]+nums[m%20]+" minutes to "+nums[h+1]


hour =int(input("Please insert Hour [1-23]: "))
minute =int(input("Please insert Minute [0-59]: "))
print(timeInWords(hour,minute).replace("  "," "))
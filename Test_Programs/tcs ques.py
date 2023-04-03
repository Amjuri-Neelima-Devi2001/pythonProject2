def tcs(l,found):
    count=0
    for i in range(len(l)):
        if l[i]==found:
            count+=1
        if count==2:
            return i
    return 0
print(tcs([1,2,1,3,4,4],1))

l = input('enter the list elements :').split()
print(l)


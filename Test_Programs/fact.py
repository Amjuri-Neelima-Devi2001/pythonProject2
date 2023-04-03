class Find_fact():
    def __init__(self,n):
        self.n=n
    def findfact(n):
        fact=1
        n=int(input("enter the number:"))
        if n==0:
            return "number must be greater than zero"
        elif n<0:
            return "only positive numbers should enter"
        elif n>0:
            for i in range(n+1):
                fact=fact*i
        return fact

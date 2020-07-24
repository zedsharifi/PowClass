class ToPow:
    def pow(self, x, n):
        temp=1
        if x==0 or x==1 or n==1:
            return x
        elif x==-1:
            if n%2 == 0:
                return 1
            else:
                return -1
        elif n==0:
            return 1
        elif n>0:
            for i in range(n):
                temp*=x
            return temp
        elif n<0:
            return 1/self.pow(x,-n)
def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            return sum==n
        #Test the function
        print(is_perfect(6))
        #True
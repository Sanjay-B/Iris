class Math:

    def sqrt(n):
        start = 0
        end = n
        m = 0
        min_range = 0;
     
        while end - start > min_range:
            m = (start + end) / 2.0;
            pow2 = m * m
            if abs(pow2 - n) <= min_range:
                return m
            elif pow2 < n:
                start = m
            else:
                end = m
             
        return m

 

    def power(x, y):
        return 1 if y == 0 else x * pow(x, y - 1)

    def gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        lcm = (x*y)//gcd(x,y)
        return lcm
    
    

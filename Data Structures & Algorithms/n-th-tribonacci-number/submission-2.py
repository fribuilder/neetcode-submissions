class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return math.ceil(n/2)
        Tri = [0] * (n+1) #The last element is Tn
        Tri[0] = 0
        Tri[1] = 1
        Tri[2] = 1

        for i in range(3,n+1):
            Tri[i] = Tri[i-1]+Tri[i-2]+Tri[i-3]
        
        return Tri[n]
        
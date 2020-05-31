class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        gs = [0,1]
        for i in range(2,n+1,1):
        	n_2 = (2**i)//2
            for j in range(0,n_2,1):
                gs[j] = [0] + gs[i]
        for j in range(0,n_2,1):
                k = (2**i)/2
                gs[j+k] = [1] + gs[k-j-1][1:]
        return gs
            
        
        
            


s = Solution()
p = s.grayCode(3)
print(p)
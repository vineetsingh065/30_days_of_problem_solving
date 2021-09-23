"""
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

Example 1:

Input: N = 4
Output: 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bits
For 2: 0 1 0 = 1 set bits
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bits
Therefore, the total set bits is 5.
"""

def countSetBits(n):
    
    count=0
    i=1
    
    while(i<=n):
       i=i*2
       q=(n+1)//i
       r=(n+1)%i
       t=q*(i//2)
       
       if r>(i//2):
           t+=r-i//2
       count+=t
    return count    

 
if __name__=='__main__':
    n = 17
    print(countSetBits(n))

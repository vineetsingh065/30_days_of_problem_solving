"""
gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.

Given two integers n and p denoting the number of houses and the number of pipes. The connections of pipe among the houses contain three input values: ai, bi, di denoting the pipe of diameter di from house ai to house bi. Find the efficient way for the construction of the network of pipes.

The output will contain the number of pairs of tanks and taps t installed in first line and the next t lines contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.

Example 1:

Input:
n = 9, p = 6
a[] = {7,5,4,2,9,3}
b[] = {4,9,6,8,7,1}
d[] = {98,72,10,22,17,66} 
Output: 
3
2 8 22
3 1 66
5 6 10
Explanation:
Connected components are 
3->1, 5->9->7->4->6 and 2->8.
Therefore, our answer is 3 
followed by 2 8 22, 3 1 66, 5 6 10.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function solve() which takes an integer n(the number of houses), p(the number of pipes),the array a[] , b[] and d[] (where d[i] denoting the diameter of the ith pipe from the house a[i] to house b[i]) as input parameter and returns the array of pairs of tanks and taps installed i.e ith element of the array contains three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.  

Expected Time Complexity: O(n+p)
Expected Auxiliary Space: O(n+p)

Constraints:
1<=n<=20
1<=p<=50
1<=a[i],b[i]<=20
1<=d[i]<=100
"""

class Solution:
    def __init__(self):
        self.ans0 = 0
        self.ans1 = []
        self.ans2 = []
        self.ans3 = []
        self.rd1 = [0]*1100
        self.wt2 = [0]*1100
        self.cd3 = [0]*1100
        self.f_ans = []
        
    def dfs(self, w):
        if (self.cd3[w] == 0):
            return w
        if (self.wt2[w] < self.ans0):
            self.ans0 = self.wt2[w]
        return self.dfs(self.cd3[w])
        
    def solve(self, n, p ,a, b, d):
            
        i = 0
        
        while i < p:
            x = a[i]
            y = b[i]
            z = d[i]
            
            self.cd3[x] = y
            self.wt2[x] = z
            self.rd1[y] = x
            i += 1
            
        for j in range(1, n + 1):
            if self.rd1[j] == 0 and self.cd3[j]:
                 
                self.ans0 = 1000000000
                w = self.dfs(j)
                
                self.ans1.append(j)
                self.ans2.append(w)
                self.ans3.append(self.ans0)
                
        for i in range(len(self.ans1)):
            self.f_ans.append([self.ans1[i], self.ans2[i], self.ans3[i]])
            
        return self.f_ans


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))

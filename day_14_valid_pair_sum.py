"""
Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.

Example 1:

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two 
possible pairs.
Example 2:

Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.
Your Task:  
You don't need to read input or print anything. Complete the function ValidPair() which takes the array a[ ] and size of array N as input parameters and returns the count of such pairs.

Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105 
-104  ≤ a[i] ≤ 104
"""

class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
    	a.sort()
    	point_a , point_b = 0, n-1
    	count = 0
    	while point_a!=point_b:
    	    if a[point_a] + a[point_b] > 0:
    	        count +=point_b - point_a
    	        point_b -= 1
    	    elif a[point_a] + a[point_b] <= 0:
    	        point_a += 1
    	return count


if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		n = int(input())
		array = list(map(int, input().strip().split()))
		obj = Solution()
		ans = obj.ValidPair(array, n)
		print(ans) 
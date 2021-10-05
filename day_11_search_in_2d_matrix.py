"""
You are given a 2-D matrix with 'N' rows and 'M' columns, each row of the matrix is sorted in non-decreasing order and the first element of each row is greater than or equal to the last element of the previous row. You are also given an integer ‘X’, you are supposed to find whether 'X' is present in the given matrix or not.
Input Format :
The first line contains a single integer ‘T’ denoting the number of test cases. The test cases are as follows.

The first line of each test case contains three integers ‘X’, ‘N’ and ‘M’ separated by a single space denoting the element to be searched, the number of rows in the matrix, and the number of columns in the matrix respectively.

The next ‘N’ lines contain ‘M’ integers each denoting the elements of the matrix.
Output Format :
For each test case, print “Yes”(without quotes) if ‘X’ is present in the matrix otherwise print “No”.

Print the output of each test case on a new line. 
Note :
You don’t need to print anything; It has already been taken care of.
Constraints :
1 <= T <= 50
1 <= X <= 10 ^ 6
1 <= N, M <= 100
-10 ^ 6 <= ARR[i][j] <= 10 ^ 6

Where ‘T’ denotes the number of test cases, ‘N’ denotes the number of rows in a matrix, ‘M’ denotes the number of columns in the matrix and ARR[i][j] denotes the j-th element of the i’th row of the given matrix.

Time Limit: 1 sec
Sample Input 1 :
2
4 2 2
2 4
8 12
7 3 4
1 2 4 5
8 12 14 16
23 25 26 29
Sample Output 1 :
Yes
No
"""

def findInMatrix(x, arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):

        #    Do a binary search
        low = 0
        high = m - 1
        while (low <= high):

            mid = (low + high) //2
            if (arr[i][mid] == x):
                return True

            elif (arr[i][mid] > x):
                high = mid - 1

            else:
                low = mid + 1

    return False
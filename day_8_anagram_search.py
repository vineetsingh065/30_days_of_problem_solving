class Solution:

	
	def search(self, pat, txt):
		n, m, ans = len(txt), len(pat), 0
		ar, br = [0]*26, [0]*26

		for i in range(m):
			ar[ord(pat[i]) - 97] += 1
			print(ar)
			br[ord(txt[i]) - 97] += 1
			print(br)

		for i in range(m, n):
			if ar == br: ans += 1
			br[ord(txt[i]) - 97] += 1
			br[ord(txt[i-m]) - 97] -= 1

		return ans+1 if ar == br else ans


if __name__ == "__main__": 		
    ob = Solution()
    ans = ob.search("for", "forxxorfxdofr")
    print(ans)
    
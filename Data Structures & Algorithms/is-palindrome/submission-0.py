class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointer
        s_arr = [] 
        for c in s:
            if not c.isalnum():
                continue
            s_arr.append(c.lower())
        
        l, r = 0, len(s_arr) - 1
        while l < r:
            if s_arr[l] != s_arr[r]:
                return False
            l += 1
            r -= 1
        
        return True
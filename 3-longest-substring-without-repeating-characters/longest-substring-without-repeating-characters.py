class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        maxlen = 0
        left = 0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            maxlen = max(maxlen, right-left+1)
        return maxlen
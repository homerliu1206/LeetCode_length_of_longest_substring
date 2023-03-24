class Solution:
    def lengthOfLongestSubstring(self, s):
        list_s = list(s)
        length = len(list_s)
        result = []
        seek_max = []

        for alph in list_s:
            if alph not in result:
                result.append(alph)
            else:
                seek_max.append(len(result))
                result = []
                result.append(alph)
        print(max(seek_max))
        
solution = Solution()
solution.lengthOfLongestSubstring("pwwkew")

#Testcase:

# "abcabcbb"
# "bbbbb"
# "pwwkew"
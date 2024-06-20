# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1: Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2: Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        print(len(prefix))
        for st in strs[1:]:
            #print(type(st))
            while st.find(prefix)!=0:
                print(prefix)
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return(prefix)

ob  = Solution()
ls = ob.longestCommonPrefix(["flower","flow","flight"])
print(ls)
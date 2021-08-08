class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def convert_to_hash(s):
            str_hash = {}
            for i in s:
                if i not in str_hash:
                    str_hash[i] = 1
                else:
                    str_hash[i] += 1
            return str_hash
        return convert_to_hash(s) == convert_to_hash(t)

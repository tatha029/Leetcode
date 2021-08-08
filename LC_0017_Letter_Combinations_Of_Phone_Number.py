class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mnemonics = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        all_codes = []
        def mnemonicsCreator(alreadyChecked, remaining):
            if remaining == "":
                return all_codes.append(alreadyChecked)
            for x in mnemonics[remaining[0]]:
                mnemonicsCreator(alreadyChecked + x, remaining[1:])
        if len(digits) == 0:
            return []
        mnemonicsCreator('', digits)
        return all_codes

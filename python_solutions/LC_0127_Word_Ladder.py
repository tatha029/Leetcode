from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        alpha = "abcdefghijklmnopqrstuvwxyz"

        def permuteWord(word):
            simWords = []
            for i in range(len(word)):
                for j in alpha:
                    if j == word[i]:
                        continue
                    genWord = word[:i] + j + (word[i+1:] if i < len(word) else '')
                    if genWord in wordSet:
                        simWords.append(genWord)
                        wordSet.remove(genWord)
            return simWords

        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, depth = queue.popleft()
            simWords = permuteWord(word)
            for s in simWords:
                if s == endWord:
                    return depth+1
                queue.append((s, depth+1))
        return 0

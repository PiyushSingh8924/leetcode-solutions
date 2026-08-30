class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while queue:
            curr_word , level = queue.popleft()
            if curr_word == endWord:
                return level
            for i in range(0,len(curr_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == curr_word[i]:
                        continue
                    new_word = curr_word[:i] + c + curr_word[i+1:]
                    if new_word in wordset:
                        queue.append((new_word,level+1))
                        wordset.remove(new_word)
        return 0

            
        
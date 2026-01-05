from itertools import permutations

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:    
        res = []
        # Sorting ensures the result is in lexicographical order
        words.sort()
        # permutations(words, 4) handles distinct words automatically
        for top, left, right, bottom in permutations(words, 4):
            # Check matching characters at the 4 corners:
            # top[0] - left[0] (TL), top[3] - right[0] (TR)
            # bottom[0] - left[3] (BL), bottom[3] - right[3] (BR)
            if (top[0] == left[0] and 
                top[3] == right[0] and 
                bottom[0] == left[3] and 
                bottom[3] == right[3]):
                res.append([top, left, right, bottom])

        return res
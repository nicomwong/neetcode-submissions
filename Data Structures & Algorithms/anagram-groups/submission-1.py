class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # s1 + s2      s2 + s3

        # N-1 anagram comparisons + N-2 + N-3 + ... + 1 
        # -> O(N^2)

        # O(N) per anagram comparison

        # O(N^3)

        # map from string -> list of strings that are anagrams (i.e. anagram group)
        # "act" -> "act", "cat"

        # "cat" -> "act" 

        # O(slogs * N) where s is the max size of any given string
        # space: O(N)

        # nlogn amortized
        # nlogn

        # O(S* N) where S is the max size of any given string
        # space: O(N)

        # act -> a:1, c:1, t:1
        # cat -> a:1, c:1, t:1
        
        # a:1, c:1, t:1 -> "act", "cat"

        # [.., 1 (97th index), 0, 1 ('c'), .., 1, ..]

        from collections import Counter

        anagramGroups = dict()

        for word in strs:
            # get character frequencies of the word
            counts = [0] * 128
            for ch in word:
                counts[ord(ch)] += 1

            # counts = [.., 0, 0, 0, 1 (97th index), 0, 1 ('c'), .., 1 ('t'), 0, 0, 0, ..]
            counts = tuple(counts)
            # counts = (.., 0, 0, 0, 1 (97th index), 0, 1 ('c'), .., 1 ('t'), 0, 0, 0, ..)

            if counts in anagramGroups:
                # an anagram (with this string) has been seen -> existing group
                anagramGroups[counts].append(word)
            else:
                # no existing anagram group
                anagramGroups[counts] = [word]

        return [val for val in anagramGroups.values()]

        # create own example

        # ["pay", "", "lamppost"]
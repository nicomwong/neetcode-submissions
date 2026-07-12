#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        } 
        
        std::unordered_map<char, int> charactersCounts; // stores char -> count of s
        for (char c : s)
        {
            if (charactersCounts.count(c))
            {
                charactersCounts.at(c)++;
            }
            
            else
            {
                charactersCounts.insert({c, 1});
            }
        }

        // charactersCounts: {r: 2, a: 2, c: 2, e: 1}

        // "carrace"
        // c:1
        // a:1
        // r:1
        // del r
        // del a
        // del c
        // del e

        // treating charactersCounts as the remaining chars to find in t
        for (char c : t)
        {
            if (!charactersCounts.count(c))
            {
                // found char in t that is not in s (note: can be that the same alphanumeric char occurs more times in t than s)
                return false;
            }

            else
            {
                // valid, so far
                if (charactersCounts.at(c) == 1)
                {
                    charactersCounts.erase(c);
                }

                else // charactersCounts.count(c) > 1
                {
                    charactersCounts.at(c)--;
                }
            }
        }

        return charactersCounts.size() == 0;
    }
};

def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if not s:
        return 0
        
    if len(s) <= k:
        return len(s)
    
    window = {}
    left = 0
    curlen, maxlen = 0, 0
    for i in xrange(len(s)):
        #print window
        curlen += 1
        if s[i] not in window:
            window[s[i]] = 1
        else:
            window[s[i]] += 1
            
        if len(window) > k:
            while len(window) > k:
                window[s[left]] -= 1
                curlen -= 1
                if window[s[left]] == 0: 
                    del window[s[left]]
                left += 1
        maxlen = max(maxlen, curlen)
                
    return maxlen

print(lengthOfLongestSubstringKDistinct("abcgccgdkiyhdfgaefakfn",4))

#linear solution
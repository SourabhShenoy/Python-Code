class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]
        
#Ask for O/P for 0, 01, 10, 100, 110 etc
#
#
#
def numDecodings(self, s):
        '''
        Here we try to compute dp[i] for each i. dp[i] is the number of ways in which the string
s[i:len(s)] can be decoded.
        
        '''
        if not s:   return 0
        i, n = len(s)-1, len(s)
        prev, prevPrev = 1, 1
        while i>=0:
            char = s[i]
            # If current character is 3-9, then dp[i]=dp[i+1] since there is no additional ways that can
            # be induced by these digits
            if char in '3456789':
                curr = prev
            # If current char is 0, then there can be ZERO ways of decoding a string that starts with a 0
            elif char == '0':
                curr = 0
            elif char in '12':
                # If current char is 1 or 2 and next character is 0, then we have no additional ways of
                # decoding. 
                # Hence dp[i] = dp[i+2] (Note: dp[i+1] would be 0, since s[i+1] is '0'
                if i<n-1 and s[i+1]=='0':
                    curr = prevPrev
                # If the next char is 1-6 (or 7-9 with curr char as '1'), then dp[i] = dp[i+1] + dp[i+2] 
                # dp[i] = dp[i+1] (represents the numWays when we regard 1/2 as A/B) + dp[i+2]
                # (represents the numWays when we regard 1/2 along with next digit
                elif i<n-1 and ((s[i+1] in '123456') or (s[i+1] in '789' and char=='1')):
                    curr = prev + prevPrev
                # If we have 1/2 as the rightmost digit of the string, then we don't have any additional
                # ways to produce
                else:
                    curr = prev
            prev, prevPrev = curr, prev
            i-=1
        return prev
#balenced parenthesis
#
#Destroys the original string. O(1) Space. O(n^2). Slow
#
def isValid(s):
	n = len(s)
	if n == 0:
		return True
	
	if n % 2 != 0:
		return False
		
	while '()' in s or '{}' in s or '[]' in s:
		s = s.replace('{}','').replace('()','').replace('[]','')
	
	return len(s) == 0

#Stack solution	
#
def isValid(s):
	stack = []
	dict = {"]":"[", "}":"{", ")":"("}
	for char in s:
		if char in dict.values():
			stack.append(char)
		elif char in dict:#.keys():
			if stack == [] or dict[char] != stack.pop():
				return False
		else:
			return False
	return stack == []
	
############################################################################
############################################################################
#Generate valid parenthesis
'''
n = 3
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
]
'''

'''
p is the parenthesis-string built so far, left and right tell the number of left and right parentheses
still to add, and parens collects the parentheses.
'''
#Backtracking
def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
    
############################################################################
############################################################################
#Remove invalid parenthesis
'''
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

'''

def removeInvalidParentheses(self, s):
    def isvalid(s):
        s = filter('()'.count, s)
        while '()' in s:
            s = s.replace('()', '')
        return not s
    level = {s}
    while True:
        valid = filter(isvalid, level)
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
        


############################################################################
############################################################################
#Longest valid parenthesis.... DP
#For "(()", the longest valid parentheses substring is "()", which has length = 2.

class Solution(object):
    def longestValidParentheses(self, s):
        result=0
        stk=[]
        lst=-1
        for i in xrange(len(s)):
            if s[i]=='(':
                if lst!=-1:
                    stk.append(lst)
                    lst=-1
                else:
                    stk.append(i)
            else:
                if stk:
                    stt=stk.pop()
                    if i-stt+1>result:
                        result=i-stt+1
                    lst=stt
                else:
                    lst=-1
        return result
'''
stk store the index of '('. 

we intereate through the string. 

result is the length of the longest unbroken bracket chain at that position, we update it when we iterate through the string. We initiate it to 0.

lst is -1 or the starting index of the unbroken bracket chain we just extended with a matching ')', its initial value is -1, if we iterate to a '(' or a umatchable ')', we set lst to -1. So we are using lst for two purposes.

Every time we see a '(', we push a index to the stack. if the lst is not -1 (means last time we just got a matching ')' and extended the current unbroken bracket chain and we set lst to the starting index of that chain), we push lst into the stack. If lst is -1, it means we are on index 0 or last character is not a match ')'. We push the index i into the stack. We set lst to -1 in either case.

Every time we see a ')' and the stack is not empty ( means it's a matching ')' ),we pop the stack. we calculate the length of the chain and update the result and set the lst to the popped index. If the stack is empty, it means that's a unmatchable ')', and we set lst to -1.

A lot of times, we pop a index and push it right back like when we iterate to index 2 of string "()()"
In the end of the interation we will have the length of the longest chain in the result variable
'''

############################################################################
############################################################################
#Ways to add parenthesis

Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

def diffWaysToCompute(self, input):
   tokens = re.split('(\D)', input)
   nums = map(int, tokens[::2])
   ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
   def build(lo, hi):
       if lo == hi:
           return [nums[lo]]
       return [ops[i](a, b)
               for i in xrange(lo, hi)
               for a in build(lo, i)
               for b in build(i + 1, hi)]
   return build(0, len(nums) - 1)
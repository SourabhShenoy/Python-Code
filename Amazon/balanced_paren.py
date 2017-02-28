def balanced_parenthesis(input_string):

#Stack which stores the matching end brace for an opening brace
	stack = []

#Parenthesis pairs
	dict = {	"[":"]",
				"{":"}",
				"(":")"
			}

	for char in input_string:
#If opening brace is present, append closing brace to the stack
		if char in dict:
			stack.append(dict[char])
#If we encounter a closing brace, then check if the last element added to stack is the corresponding opening brace
		elif char in dict.values():
			if stack==[] or char != stack.pop():
				return False 
#For other string characters such as numbers, digits: ignore them
		else:
			continue
#Final condition to check if all braces were matched
	return stack == []

print(balanced_parenthesis("(sd(sdg[sd]sdsdf)fgff)sfg"))

#Time Complexity: O(n) (Iterates through the string once)
#Space Complexity: O(n) (For stack)
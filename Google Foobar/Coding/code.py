def solution(S, K):
#return string in all caps without hyphens if k is greater than the length
	if K > len(S):
		return S.replace("-","").upper()
#Remove incorrect hyphens	
	plain_S = S.replace("-","")
#Convert to upper case	
	upper_S = plain_S.upper()
#Reverse string, since First grouping should be small if len(S)%K != 0
	rev_S = upper_S[::-1]
#Will store strings in groups of K	
	K_words = []
#Split into groups of K
	for i in range(0, len(rev_S), K):
		K_words.append(rev_S[i:i+K])
#Join the words with a hyphen			
	final_str = "-".join(K_words)
#Reverse to get the original string
	return final_str[::-1]
    
print solution("2-4A0r7-4k",20)
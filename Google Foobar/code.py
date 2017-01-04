def delete(list, first, second):
    if first in list:
        list.pop(list.index(first))
    if second in list:
        list.pop(list.index(second))
    return list
    
def loop(a, b):
    sum = a + b
    if sum % 2:
        return True
    sum /= 2
    if a < b:
    	min = a
    else:
    	min = b
    if not sum % min:
        sum /= min
        count = 1
        while count < sum:
            count *= 2
        if count == sum:
            return False
    return True

def answer(banana_list):
	if not len(banana_list):
		return 0
	sorted_list = sorted(banana_list)
	pairs = []
	for first in sorted_list:
		temp = []
		for second in sorted_list:
			if loop(first,second):
				temp.append(second)
		pairs.append(temp)
	
	smallest_list = min(pairs, key=lambda x: len(x) or 999)
	count = 0
	while len(filter(lambda x: len(x), pairs)) >= 2:
		if not len(smallest_list):
			break
		second = smallest_list[0]
		match_list = []
		for a, b in enumerate(sorted_list):
			if second == b:
				match_list.append(a)	
		for i in match_list:
			if len(pairs[i]):
				del pairs[i][:]
				break
		del smallest_list[:]
		pairs = map(lambda x: delete(x, sorted_list[pairs.index(smallest_list)], second), pairs)
		smallest_list = min(pairs, key=lambda x: len(x) or 999)
		count += 2
	
	return len(sorted_list) - count

input1 = [1, 1]
input3 = [1, 7, 3, 21, 13, 19]
input2 = [1, 2, 1, 7, 3, 21, 13, 19]
input = []
print(answer(input1))
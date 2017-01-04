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
	banana_list = sorted(banana_list)
	pairs = []
	for first in sorted_list:
		temp = []
		for second in sorted_list:
			if loop(first,second):
				temp.append(second)
		pairs.append(temp)

	smallest_list = min(pairs, key=lambda x: len(x) or 999)
	while len(filter(lambda x: len(x), pairs)) >= 2:
		if not len(smallest_list):
			break
        current_item = banana_list[match_list.index(current_min_list)]
        matched_item = current_min_list[0]
        for matched_item_index in item_matched_lists(banana_list, matched_item):
            if len(match_list[matched_item_index]):
                del match_list[matched_item_index][:]
                break
        del current_min_list[:]
        match_list = map(lambda x: extract_values(x, current_item, matched_item), match_list)
        count += 2
	smallest_list = min(pairs, key=lambda x: len(x) or 999)
    return len(banana_list) - count


input1 = [1, 1]
input3 = [1, 7, 3, 21, 13, 19]
input2 = [1, 2, 1, 7, 3, 21, 13, 19]
input = []
print(answer(input2))
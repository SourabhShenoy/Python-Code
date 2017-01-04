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
    count = 0

    banana_list = sorted(banana_list)

    match_list = [[second_item for second_item in banana_list if loop(item, second_item)] for item in
                  banana_list]

    current_min_list = min(match_list, key=lambda x: len(x) or 999)

    while len(current_min_list) and len(filter(lambda x: len(x), match_list)) > 1:
        current_item = banana_list[match_list.index(current_min_list)]
        matched_item = current_min_list[0]
        match_list = []
        for a, b in enumerate(sorted_list):
            if second == b:
                match_list.append(a)
        for matched_item_index in match_list:
            if len(match_list[matched_item_index]):
                del match_list[matched_item_index][:]
                break
        del current_min_list[:]
        match_list = map(lambda x: delete(x, current_item, matched_item), match_list)
        count += 2
        current_min_list = get_shortest_list(match_list)

    return len(banana_list) - count
    
input1 = [1, 1]
input3 = [1, 7, 3, 21, 13, 19]
input2 = [1, 2, 1, 7, 3, 21, 13, 19]
input = []
print(answer(input))
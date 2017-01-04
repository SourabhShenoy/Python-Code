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

def get_shortest_list(l):
    return min(l, key=lambda list_item: len(list_item) or 101)

def item_matched_lists(l, searched_value):
    return [i for i, x in enumerate(l) if x == searched_value]

def non_empty_list_count(l):
    return len(filter(lambda x: len(x), l))


def answer(banana_list):
    count = 0

    banana_list = sorted(banana_list)

    match_list = [[second_item for second_item in banana_list if loop(item, second_item)] for item in
                  banana_list]

    current_min_list = get_shortest_list(match_list)

    while len(current_min_list) and non_empty_list_count(match_list) > 1:
        current_item = banana_list[match_list.index(current_min_list)]
        matched_item = current_min_list[0]
        for matched_item_index in item_matched_lists(banana_list, matched_item):
            if len(match_list[matched_item_index]):
                del match_list[matched_item_index][:]
                break
        del current_min_list[:]
        match_list = map(lambda x: delete(x, current_item, matched_item), match_list)
        count += 2
        current_min_list = get_shortest_list(match_list)

    return len(banana_list) - count
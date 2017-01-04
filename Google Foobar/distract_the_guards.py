"""

Distract the Guards
===================

The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out!
Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the
space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that
time you spent working as first a minion and then a henchman means that you know the guards are fond of bananas.
And gambling. And thumb wrestling.

The guards, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. The
guard with fewer bananas will bet all their bananas, and the other guard will match the bet. The winner will receive
all of the bet bananas. You don't pair off guards with the same number of bananas (you will see why, shortly). You know
enough guard psychology to know that the one who has more bananas always gets over-confident and loses. Once a match
begins, the pair of guards will continue to thumb wrestle and exchange bananas, until both of them have the same number
of bananas. Once that happens, both of them will lose interest and go back to guarding the prisoners, and you don't want
THAT to happen!

For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling
they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they
will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to guarding.

How is all this useful to distract the guards? Notice that if the guards had started with 1 and 4 bananas, then they
keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into an infinite
thumb wrestling loop!

Write a function answer(banana_list) which, given a list of positive integers depicting the amount of bananas the each
guard starts with, returns the fewest possible number of guards that will be left to watch the prisoners. Element i of
the list will be the number of bananas that guard i (counting from 0) starts with.

The number of guards will be at least 1 and not more than 100, and the number of bananas each guard starts with will be
a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) banana_list = [1, 1]
Output:
    (int) 2

Inputs:
    (int list) banana_list = [1, 7, 3, 21, 13, 19]
Output:
    (int) 0

"""
import unittest


def detect_inf_loop(a, b):
    number_sum = a + b
    if number_sum % 2:
        return True
    number_sum /= 2
    lower_number = a if a < b else b

    if not number_sum % lower_number:
        number_sum /= lower_number
        count = 1
        while count < number_sum:
            count <<= 1
        if count == number_sum:
            return False
    return True


def get_shortest_list(l):
    return min(l, key=lambda list_item: len(list_item) or 101)


def extract_values(l, first_value, second_value):
    if first_value in l:
        l.pop(l.index(first_value))

    if second_value in l:
        l.pop(l.index(second_value))

    return l


def item_matched_lists(l, searched_value):
    return [i for i, x in enumerate(l) if x == searched_value]


def non_empty_list_count(l):
    return len(filter(lambda x: len(x), l))


def answer(banana_list):
    count = 0

    banana_list = sorted(banana_list)

    match_list = [[second_item for second_item in banana_list if detect_inf_loop(item, second_item)] for item in
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
        match_list = map(lambda x: extract_values(x, current_item, matched_item), match_list)
        count += 2
        current_min_list = get_shortest_list(match_list)

    return len(banana_list) - count


class TestDistractTheGuards(unittest.TestCase):
    def test1(self):
        test_input = [1, 1]
        self.assertEqual(answer(test_input), 2)

    def test2(self):
        test_input = [1, 7, 3, 21, 13, 19]
        self.assertEqual(answer(test_input), 0)

    def test3(self):
        test_input = [1, 2, 1, 7, 3, 21, 13, 19]
        self.assertEqual(answer(test_input), 0)

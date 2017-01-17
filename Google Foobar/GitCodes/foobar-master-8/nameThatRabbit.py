

"""
Professor Boolean has always had a thing for names with lots of letters near the "tail end"
of the alphabet.

Assign the values 1 through 26 to the letters of the alphabet, for each word,find the sum
of the values for all of the letters, the names with the highest total values will be sorted 
first. If two names have the same value, Professor Boolean prefers the lexicographically larger
name. For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and returns the list sorted
in descending order of how much the professor likes them. 

There will be at least 1 and no more than 1000 names. Each name will consist of only lower
case letters. The length of each name will be at least 1 and no more than 8.

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dict = {}
for i in range(len(alphabet)):
    # assign each letter of alphabet its value from 1 to 26
    alphabet_dict[alphabet[i]] = i+1

# get sum of the letters in each word, based on values for each letter
# in alphabet_dict
def str_sort(str_list):
    str_sum = 0
    for s in str_list:
        str_sum += alphabet_dict[s]
    return str_sum

def word_sort(word_list):
    # get the sum of the letters in each word in the list of words
    values = [str_sort(word) for word in word_list]
    # combine each word in the word list with its respective value
    word_values = list(zip(word_list, values))
    # sort words lexicogaphically first to ensure that the result is sorted lexicographically
    lexo_sorted_words = reversed(sorted(word_values, key=lambda x: x[0]))
    # sort words based on the sum of its letter values
    sorted_word_values = sorted(lexo_sorted_words, key=lambda x: -x[1])
    # filter tuple list to get just the value+lexo sorted words
    sorted_words = [word[0] for word in sorted_word_values]
    return sorted_words


test = """
The inverse can be understood this way Take the final table in the BWT algorithm and erase all but the last column Given only this information you can easily reconstruct the first column The last column tells you all the characters in the text so just sort these characters alphabetically to get the first column Then the first and last columns of each row together give you all pairs of successive characters in the document where pairs are taken cyclically so that the last and first character form a pair Sorting the list of pairs gives the first and second columns Continuing in this manner you can reconstruct the entire list Then the row with the end of file character at the end is the original text Reversing the example above is done like this
"""
test = test.lower()
test = test.strip('\n').split(' ')
print(word_sort(test))







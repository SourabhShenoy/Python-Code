

"""
Write a function called answer(document, searchTerms) which returns the shortest snippet of the
document that contains all of the given search terms. The search terms can appear in any order.

The length of the snippet is the number of words in the snippet. The document will be a string
consisting only of lower-case letters and spaces. Words in the string will be separated by a single space.
A word could appear multiple times in the document.

searchTerms will be a list of words, each word comprised only of lower-case letters [a-z]. All the search
terms will be distinct. Search terms must match words exactly, i.e. "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. The document will be guaranteed to
contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, and each word will be
1 to 10 letters long. Repeat words in the document are considered distince for counting purposes. The
number of words in searchTerms will be at least one, will not exceed 100, and each word will not be
more than 10 letters long.

Test cases:

Inputs:
document = "many google employees can program"
searchTerms = ["google", "program"]

Outputs:
"google employees can program"

Inputs:
document = 'a b c d a'
searchTerms = ["a", "c", "d"]

Outputs:
"c d a"

"""

# Little optimization function to trim the given on each side to just the possible
# stretch of text that contains the search terms. Starting from each end, remove
# words until an item from search terms appears. 
def trimDoc(document,searchTerms):
    document = document.split(' ')
    for i in range(len(document)):
        if document[i] in searchTerms:
            first = i 
            break 
    for i in range(len(document)-1,0,-1):
        if document[i] in searchTerms:
            last = i
            break
    return document[first:last+1]

def answer(document, searchTerms):
    all_snips = []
    document = trimDoc(document, searchTerms)
    minimum = (len(document)+len(searchTerms))
    count = 0
    while minimum >= len(searchTerms):
        cache = []
        for i in range(len(document)-minimum+1):
            snippet = document[i:i+minimum]
            for i in searchTerms:
                # if search term not in snippet, break to continue with next loop
                if snippet.count(i) < 1:
                    break
            else:
                cache.append(snippet)
                if all_snips:
                    # if snippet is shorter than all_snips, make all_snips = snippet
                    if len(snippet) < len(all_snips):
                        all_snips = snippet
                        break
                # if there are no snippets yet, make all_snips = snippet
                else:
                    all_snips = snippet
                    break
            count += 1
        minimum -= 1
        # if the loop has cycled through entirely and there are no snippets, but there
        # is all_snips, there are no other possibilities and the loop should break
        if not cache and all_snips:
            break
    return ' '.join(all_snips)


print(answer('a b c d a', ["a","c","d"]))
print(answer("many google employees can program",["google", "program"]))






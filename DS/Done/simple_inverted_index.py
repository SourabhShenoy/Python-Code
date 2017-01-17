#pretty print
from pprint import pprint as pp
#filename pattern matching
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
 
 
def parsetexts(fileglob='inverted_index/a*.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob): #matches all patterns
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words
 
def termsearch(terms): # Searches simple inverted index
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))
 
texts, words = parsetexts()
print('\nTexts')
pp(texts)
print('\nWords')
pp(sorted(words))
 
invindex = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
print('\nInverted Index')
pp({k:sorted(v) for k,v in invindex.items()})
 
terms = ["what", "is", "it"]
print('\nTerm Search for: ' + repr(terms))
pp(sorted(termsearch(terms)))
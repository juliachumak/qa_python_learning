s = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)
"""

words_number = len(s.split())
print(words_number)

words_list = s.split()

def remove_punctuation(list):
    print(list)
    punc_list = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
    result = []
    for s in words_list:
        for punc in punc_list:
            s = s.strip(punc)
            print(s)
        result.append(s)

    return (result)

words_list = remove_punctuation(words_list)
print(words_list)


sorted_list = sorted(words_list, key=lambda s: s.lower())
print(sorted_list)


def count_list_elements(list):
    counted_elements = {}
    for e in list:
        counted_elements[e] = 1
    return (counted_elements)

print(count_list_elements(words_list))
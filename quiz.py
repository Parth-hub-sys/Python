# a = input("\n enter your string : ")

# print(a)
# # rev = "".join(reversed(a))
# # print(rev)

# fc = a[0]
# rs = a[1:]
# print(rs)
# result = rs + fc
# print(result)
# import random
# import string

# def rs(length):
#     return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# ms = "hello are you brother"
# fc= ms[0]
# rx = ms[1:]
# g = rx + fc
# print(g)

# random_prefix = rs(3)
# random_suffix = rs(3)

# result = random_prefix + g + random_suffix
# print(result)


# def solution(result):
#     print(result)
#     c = result[3:-3]
#     print(c)
#     lc = c[-1]
#     M = lc + c
#     print(M)
#     print(M[:-1])
    
# solution(result)

import random
import string

def rs(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

ms = "hello are you brother"
words = ms.split()  # split the sentence into individual words

processed_words = []
for word in words:
    fc = word[0]
    rx = word[1:]
    g = rx + fc
    random_prefix = rs(3)
    random_suffix = rs(3)
    result = random_prefix + g + random_suffix
    print(result)
    
    def solution(result):
        c = result[3:-3]
        lc = c[-1]
        M = lc + c
        return M[:-1]
    
    processed_word = solution(result)
    processed_words.append(processed_word)

final_result = ' '.join(processed_words)
print(final_result)
    


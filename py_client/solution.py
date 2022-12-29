## write a function solution that, given a string s consisting of n letters 'a' and /or 'b'
#return True when all the occurences of letter 'a' are before all the occurences of letter 'b' and return false otherwise

# examples
# Given s = "aabbbb" = True
# Given s = "aabbbbbb" = True
# Given s = "bba" = False
# Given s = "abbaaa" = False
# Given s = "aaaa" = True
# Given s = "bbbb" = True
# Given s = "ba" = False
# Given s = "aabbb" = True

# write an efficient algorithm for the following assumptions:
# n is an integer within the range [1..200,000]


# def solution(s):
#     seen_a = False
#     for c in s:
#         if c == 'a':
#             seen_a = True
#         elif c == 'b' and seen_a:
#             return False
#     return True



# print(solution('aabbbb'))
# print(solution('aabbbbbb'))
# print(solution('bba'))
# print(solution('abbaaa'))
# print(solution('aaaa'))
# print(solution('bbbb'))
# print(solution('ba'))
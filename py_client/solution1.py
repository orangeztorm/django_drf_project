# you are givena string s of length N which encodes anon negative number v in a binary  form 
# the two types of encodings are:
# if v is odd subtract 1 from it;
# if v is even divide it by 2;
# These operations are repeated until v becomes 0.
# 

# examples:
# Given s = "011100" it value is initially 28 . The value of v should change as follows
# v = 28, v = 14, v = 7, v = 6, v = 3, v = 2, v = 1, v = 0
# solution('011100') = 7
# solution('111') = 5
# solution('1111010101111') = 22
# write an efficient aglorithm for the following assumptions:
# N is an integer within the range [1..100,000,000]
# the string s consists only of the characters '0' and/or '1'
# the string s represents a non negative integer in the range [0..1,000,000,000]

# def Solution(S):




# def solution(s):
#     last_a = -1
#     first_b = len(s) + 1
#     for i, c in enumerate(s):
#         if c == 'a':
#             last_a = i
#         elif c == 'b':
#             first_b = i
#             if first_b <= last_a:
#                 return False
#     return True



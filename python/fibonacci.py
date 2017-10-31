# def fibonacci():
#     a, b = 0, 1
#     for i in xrange(0, 10):
#         print(a)
#         a, b = b, a + b
#
#
# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)
#
#
# import collections
# import heapq
# import pprint
#
# class Spam(object):
#     def __init__(self, value):
#         self.value = value
#
#     def __repr__(self):
#         return '<%s: %s>' % (self.__class__.__name__, self.value)
#
#
# spams = [Spam(5), Spam(2), Spam(4), Spam(1)]
# sorted_spams = sorted(spams, key=lambda spam: spam.value)
# print(spams)
# print(sorted_spams)
#
#
# import functools
#
#
# def eggs(function):
#     @functools.wraps(function)
#     def _eggs(*args, **kwargs):
#         print('%r got args: %r and kwargs: %r' % (
#             function.__name__, args, kwargs))
#         return function(*args, **kwargs)
#     return _eggs
#
#
# @eggs
# def spam(a, b, c):
#     return a * b + c
#
#
# print(spam(1, 2, 3))

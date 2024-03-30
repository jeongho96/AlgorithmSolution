from collections import Counter
from sys import stdin

input = stdin.readline


def palindrome(name):
    word_counter = Counter(sorted(list(name)))

    center = ''
    half_sentence = ''
    odd_count = 0

    for char, count in word_counter.items():
        if count % 2 != 0:
            center = char
            odd_count += 1
            if odd_count > 1:
                return "I'm Sorry Hansoo"
        half_sentence += char * (count // 2)

    return half_sentence + center + half_sentence[::-1]


name = input().rstrip()

print(palindrome(name))

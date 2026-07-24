"""
LeetCode 692 Top K Frequet Words

MEDIUM

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same
frequency by their lexicographical order.



"""


words = ["love","i","leetcode","i","love","coding"]
k = 2
def topKFrequent(words: list[str], k:int) -> list[str]:

    freq_dict = dict()
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1


    result_list = []

    i = 0
    while i < k:

        max = 0
        max_word = ""
        for word, freq in freq_dict.items():
            if freq > max or (freq == max and word < max_word):
                max = freq
                max_word = word

        result_list.append(max_word)
        freq_dict.pop(max_word)
        i += 1

    return result_list



"""
Approach:
    Count frequencies in a dict, then select the max k times.
    Tiebreak: on equal frequency, pick the alphabetically smaller word.

Time:  O(k * n) — k passes, each scanning all n unique words.
Space: O(n) — the frequency dict.

Assumes k <= number of unique words (LeetCode-guaranteed).
"""


print(topKFrequent(words, k))
def max_cyclic_sum(s):
    n = len(s)
    s = s + s

    char_set = set()
    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(len(s)):
        val = ord(s[right]) - ord('a') + 1

        while s[right] in char_set:
            remove_val = ord(s[left]) - ord('a') + 1
            char_set.remove(s[left])
            curr_sum -= remove_val
            left += 1

        char_set.add(s[right])
        curr_sum += val

        while right - left + 1 > n:
            remove_val = ord(s[left]) - ord('a') + 1
            char_set.remove(s[left])
            curr_sum -= remove_val
            left += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum

s = "abca"
print(max_cyclic_sum(s))
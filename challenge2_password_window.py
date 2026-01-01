from collections import Counter

def min_window(log, pattern):
    # If pattern is longer than log, impossible
    if len(pattern) > len(log):
        return ""

    # Count required characters from pattern
    need = Counter(pattern)
    
    # How many unique chars we still need fully matched
    required = len(need)

    left = 0
    formed = 0  # how many characters currently satisfy required count
    window = {}
    
    min_len = float("inf")
    min_window = ""

    # Expand window using right pointer
    for right in range(len(log)):
        char = log[right]
        window[char] = window.get(char, 0) + 1

        # If this char count now matches what we need → one requirement satisfied
        if char in need and window[char] == need[char]:
            formed += 1

        # When all characters are satisfied → try shrinking from left
        while formed == required:
            # Update minimum window answer
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = log[left:right+1]

            # Remove left char & shrink window
            left_char = log[left]
            window[left_char] -= 1

            # If removing breaks requirement, reduce formed count
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1  # move window forward

    return min_window

print(min_window("ADOBECODEBANC", "ABC"))   # BANC
print(min_window("a", "a"))                 # a
print(min_window("a", "aa"))                # ""

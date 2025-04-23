

# '211213'
def count_me(s):
    if not s or not s.isdigit():
        return ""

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return ''.join(result)

# Example usage
# print(count_me("1123"))  # Output: "211213"
# print(count_me("211213"))  # Output: "1221121113"
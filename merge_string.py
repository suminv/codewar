
def merge_strings(s1, s2):
    max_overlap = 0
    
    # Найти максимальное перекрытие
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            max_overlap = i
    
    # Объединить строки с учетом найденного перекрытия
    merged_string = s1 + s2[max_overlap:]
    
    return merged_string
    

assert merge_strings("abcde", "cdefgh") == "abcdefgh" 
assert merge_strings("abc", "abc") == 'abc'
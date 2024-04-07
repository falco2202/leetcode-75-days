def merge_alternately(word1: str, word2: str) -> str:
    merged = ""
    i = 0
    while i < len(word1) and i < len(word2):
        merged += word1[i] + word2[i]
        i += 1
    merged += word1[i:] + word2[i:]
    return merged

merged = merge_alternately("abc", "def32132131333321")
print(merged)

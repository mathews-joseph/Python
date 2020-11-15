
def wordBreak(s, wordDict):
    n = len(s)
    res = []
    dp = [False] * n
    for i in range(n):
        for word in wordDict:
            word_len = len(word)
            sub_str = s[i-word_len+1:i+1]
            if word == sub_str and (dp[i-word_len] or i - word_len == -1):
                dp[i] = True
                res.append(sub_str)
                break
    return res

print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("aaple", ["aapl", "aapple", "e"]))

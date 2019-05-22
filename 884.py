# 884.
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

def uncommonFromSentences(A: str, B: str):
    results = {}
    for word in A.split(' ') + B.split(' '):
        results[word] = results.get(word, 0) + 1
    return( list(key for key in results if results[key] == 1) )

def main():
    A = "this apple is sweet"
    B = "this apple is sour"
    print(uncommonFromSentences(A, B))

main()

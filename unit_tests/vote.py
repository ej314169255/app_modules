from collections import Counter

def vote(votes):
    # your code
    res = Counter(votes).most_common(1)[0][0]
    return res

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
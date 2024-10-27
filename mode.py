L = [4, 6, 2, 4, 7, 8, 3, 5, 6, 4, 5, 0]
freq = [0] * 10
for i in L:
    freq[i] = freq[i] + 1
for i in range(0, 10):
    if freq[i]==max(freq):
        print(i)
def pairs_from(num):
    if num == 2:
        return 1
    if num >= 3:
        return 2
    return 0 

n = int(input())
digit = input().split()
s = []
odd = [0] * 10
even = [0] * 10
pairs = [0] * 10

for i in digit:
    #print(sorted(i))
    b = sorted(i)
    c = int(b[-1]) * 11 + int(b[0]) * 7
    if len(str(c)) > 2:
        c = int(c) % 100
    s.append(c)
s_string = list(map(str,s))

for i in range (len(s_string)):
    index = int(s_string[i][0])

    if (i+1)%2 == 0:
        even[index] += 1
    else:
        odd[index] += 1

for i in range(10):
    if even[i] <= 1 and odd[i] <= 1:
        continue
    pairs[i] += pairs_from(even[i]) + pairs_from(odd[i])
    pairs[i] = min(2,pairs[i])

print(sum(pairs))

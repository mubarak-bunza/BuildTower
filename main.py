odd = []
n = 6
i = 0
while len(odd) < n:
  if i%2 != 0:
    odd.append(i)
  i += 1
for i in range(len(odd)):
  space = odd[-1] - odd[i]
  print(' '*i)
print(odd)
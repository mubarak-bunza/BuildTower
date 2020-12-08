def tower_builder(n_floors):
    odd = []
    tower = []
    i = 0
    while len(odd) < n_floors:
        if i%2 != 0:
            odd.append(i)
        i += 1
    for i in range(len(odd)):
        space = ' '*((odd[-1] - odd[i])//2)
        star = '*'*odd[i]
        tower.append((f'{space}{star}{space}'))
    
    return tower

print(tower_builder(2))
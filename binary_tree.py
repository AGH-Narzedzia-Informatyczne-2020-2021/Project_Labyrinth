import random


grid = []
choice = ('N','W')


size = int(input("Rozmiar: "))
last = size*2 -2


# Creating a modified grid below
for i in range(1, size*2):
    grid.append([])

for x in range(1, size*2):
    for y in range(1, size*2):
        if x % 2 == 1:
            if y % 2 == 1:
                grid[x-1].append(1)
            elif y % 2 == 0:
                grid[x-1].append(0)
        elif x % 2 == 0:
            grid[x-1].append(0)

#End of grid creation

#Path carving
def Connect(a, b):
    where = choice[random.randint(0, 1)]
    if a == 0 and b == 0:
        grid[0][b + 1] = 1
        grid[a + 1][0] = 1

    elif a == 0 and b != last:
        grid[0][b+1]=1

    elif b == 0 and a != last:
        grid[a+1][0]=1

    else:
        if where == 'N':
            grid[a-1][b]=1
        else:
            grid[a][b-1]=1
#End of path carving

for i in range(0,last+1,2):
    for j in range(0,last+1,2):
        Connect(i,j)

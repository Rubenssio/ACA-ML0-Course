py = int(input('Enter y coordinate: '))
px = int(input('Enter x coordinate: '))

# # easiest solution
# print(py - 1, px - 2)
# print(py + 1, px - 2)
# print(py - 2, px - 1)
# print(py - 2, px + 1)
# print(py - 1, px + 2)
# print(py + 1, px + 2)
# print(py + 2, px - 1)
# print(py + 2, px + 1)

move1 = 1
move2 = 2

i = 0
while i < 4:
    print(py + move1, px + move2)
    print(py + move1, px - move2)
    move1, move2 = move2, - move1
    i += 1

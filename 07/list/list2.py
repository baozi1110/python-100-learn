from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())

"""列表推导式"""
vec = [2,4,6]
newvec = [3*x for x in vec]
print(newvec)
newvec = [[x, x*2] for x in vec]
print(newvec)
print([3 * x for x in vec if x > 3])
print([3 * x for x in vec if x < 2])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
newFruit = [weapon.strip() for weapon in freshfruit]
print(newFruit)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])  # [8, 6, -18, 16, 12, -36, 24, 18, -54]
print([x+y for x in vec1 for y in vec2])  # [6, 5, -7, 8, 7, -5, 10, 9, -3]
print([vec1[i]*vec2[i] for i in range(len(vec1))])  # [8, 12, -54]

# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
print([str(round(355 / 113, i)) for i in range(1, 6)])

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
newMatrix = [[row[i] for row in matrix] for i in range(4)]
print(newMatrix)
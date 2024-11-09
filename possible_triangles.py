triangles = set()

for first in range(1,178):
    for second in range(1,180-first):
        third = 180- (first + second)
        tri = tuple(sorted((first, second , third)))
        triangles.add(tri)

print(len(triangles))

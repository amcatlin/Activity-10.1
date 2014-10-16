__author__ = 'Alicia'

m = [2, 4, 6, 8]

print(m[1])

fivem = []
for i in range(len(m)):
    fivem.append(5 * m[i])
print(fivem)

m.append(10)
print(m)

m.append(6)  #You get two sixes
print(m)

print(m.index(8))

m.remove(8)
print(m)
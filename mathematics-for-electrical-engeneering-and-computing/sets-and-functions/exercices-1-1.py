# Given
E = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
A = {'a', 'b', 'e'}
B = {'b', 'c', 'd', 'f'}
C = {'c', 'd', 'e'}

# I write down the following sets:

# (a) A & B

a = A & B
print(f"(a) A & B = {a}")

# (b) A | B

b = A | B
print(f"(b) A | B = {b}")

# (c) A & C'

c = A & (E - C)
print(f"(c) A & C' = {c}")

# (d) (A | B) & C

d = b & C
print(f"(d) (A | B) & C = {d}")

# (e) (A & C) | (B & C)

e = (A & C) | (B & C)
print(f"(e) (A & C) | (B & C) = {e}")

# (f) (A & B) | C
f = (A & B) | C
print(f"(f) (A & B) | C = {f}")

# (g) (A | C) & (B | C)

g = (A | C) & (B | C)
print(f"(g) (A | C) & (B | C) = {g}")

# (h) (A & C)'

h = E - (A & C)
print(f"(h) (A & C)' = {h}")

# (i) A' | C'

i = (E - A) | (E - C)
print(f"(i) A' | C' = {i}")

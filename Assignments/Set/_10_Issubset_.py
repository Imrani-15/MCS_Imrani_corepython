# Issubset and issuperset.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
print("Issuperset:",A.issuperset(B))
print("Issuperset",B.issuperset(A))
print("Issuperset",C.issuperset(B))
print()
print("Issuperset:",A.issubset(B))
print("Issuperset",B.issubset(A))
print("Issuperset",C.issubset(B))

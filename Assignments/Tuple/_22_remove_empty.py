#  to remove an empty tuple(s) from a list of tuples

def Remove(tup):
    tup = [t for t in tup if t]
    return tup


# Driver Code
tup = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tup))
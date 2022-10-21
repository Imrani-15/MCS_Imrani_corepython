# sort a tuple by its float element.
def sot_tuple(tup):
    tup.sort(key = lambda x: float(x[1]),reverse = True)
    print(tup)
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
    ('anand', '4.256'), ('gaurav', '10.365')]
sot_tuple(tup)
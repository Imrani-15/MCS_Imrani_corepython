# Sort a dictionary by key
import _10_map_two_list
mydict = _10_map_two_list.result
for i in sorted(mydict):
    print((i,mydict[i]),end=" ")
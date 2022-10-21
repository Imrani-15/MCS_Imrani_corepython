# Sort Counter by value.
import operator

markdict = {"hindi":67, "english": 54, "telugu": 87, "science": 43, "social":73}
marklist= sorted(markdict.items(), key=operator.itemgetter(1))
sortdict=dict(marklist)
print(sortdict)
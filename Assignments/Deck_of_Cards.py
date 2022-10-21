import random
cardfaces = []
suits = ['Hearts',"Diamonds","Clubs","Spades"]
royals = ["J","Q","K","A"]
deck = []
cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
for i in range(2,11):
    cardfaces.append(str(i))
    # this is adds numbers 2-10 and converts them to string data
for j in range(4):
    cardfaces.append(royals[j])
    # this will add the royal faces to the cardfaces
print(cardfaces)
#dict = {}
#dict[cardfaces] = cards
#print(dict)
for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + suits[k])
        deck.append(card)
#random.shuffle(deck)

for m in range(52):
    print(deck[m])
print(list(deck))


test_keys = ['2Hearts', '3Hearts', '4Hearts', '5Hearts', '6Hearts', '7Hearts', '8Hearts', '9Hearts', '10Hearts', 'JHearts', 'QHearts', 'KHearts', 'AHearts', '2Diamonds', '3Diamonds', '4Diamonds', '5Diamonds', '6Diamonds', '7Diamonds', '8Diamonds', '9Diamonds', '10Diamonds', 'JDiamonds', 'QDiamonds', 'KDiamonds', 'ADiamonds', '2Clubs', '3Clubs', '4Clubs', '5Clubs', '6Clubs', '7Clubs', '8Clubs', '9Clubs', '10Clubs', 'JClubs', 'QClubs', 'KClubs', 'AClubs', '2Spades', '3Spades', '4Spades', '5Spades', '6Spades', '7Spades', '8Spades', '9Spades', '10Spades', 'JSpades', 'QSpades', 'KSpades', 'ASpades']
test_values = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
#print ("Original key list is : " + str(test_keys))
#print ("Original value list is : " + str(test_values))
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
print ("Resultant dictionary is : " +  str(res))
lis = list(res.items())
random.shuffle(lis)
d = dict(lis)
print(d)


#keys = list(d.keys())
#odd_keys = keys[0:26]
#even_keys = keys[26:52]
#print(len(odd_keys))
#print(len(even_keys))

play1 = {}
play2 = {}

list = [i for i in d.keys()]
for i,j in zip(list[1::2],list[0: : 2]):
#    print(f'\n distributing between two players')
    play1[i]=d[i]
    d.pop(i)
    play2[j]=d[j]
    d.pop(j)
print("play1:",play1)
print("play2:",play2)
#    print('\n remaining dictionary:',d)

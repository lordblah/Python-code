a = [66.25, 333,33,1,1234.5]
print a.count(333), a.count(66.25), a.count('x')
#inserts an item at a given position. the first argument is the index of the element before which to insert.

a.insert(2, -1)
#append, adds an item to the end of the list
a.append(333)
print a
#index, return the index in the list of the first item whose vaule is x
a.index(333)
#remove, removes the first item from the list whose value is x.
a.remove(333)

print a

a.reverse()

print a

a.sort()
print a
#opo, remvoes the item at the given positino in the list. if no index is specified, it removes and returns the kast ltien
# in the list
a.pop()
print a

combs1 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs1.append((x,y))
#this is the same as this

combs2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print combs1
print combs2
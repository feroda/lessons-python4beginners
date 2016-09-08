# how to know about "list comprension"

l2 = [1,2,3,4,100,10,2,4,15]

# l3 = [ x*2 for x in l2]
# l3 = [ x*2 for x in l2 if x > 10]
l3 = [ x*2 for i,x in enumerate(l2) if not i % 2]
#KO l3 = [ x*2 for i,x in l2.index(x) if not i % 2]
l3 = [ x*2 for i,x in enumerate(l2) if not i % 2]

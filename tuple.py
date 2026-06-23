# Tuple create

mytuple = (10,"c",99,25.20,"Lukman",55,88)
print(mytuple)

# tuple Slice
mytuple = (10,"c",99,55,20.52,"Lukman",52,55,55,45,)
print(mytuple)
print(mytuple[2])
print(mytuple[4:6])
print(mytuple[3:])

# we can not modify

mytuple = (10,"c",66,88,"Lukman",71)
print(mytuple[0]) # print

mytuple[0] = 99  # error
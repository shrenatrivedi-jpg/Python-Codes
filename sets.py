#Converting a list to a set

sample_list=[1,1,2,2,3,3]

sample_set=set(sample_list)

#Show that sets are not indexable
# print(sample_set[2])  # This will raise a TypeError


#Check if an element exists in a set
if 4 in sample_set:
    print("Yes")
else:
    print("No")

#Adding  elements to a set
myset=set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)

#Remove the elements from the set

myset.remove(2)
#Throws error if element is not present
#myset.remove(5)
#Does not throw error if element is not present
myset.discard(5)

print(myset)
records=[]

for i in range(5):
    groupname = input("\nEnter group name: ")
    Sizeofthegroup = int(input("Enter size of the group: "))
    dateofthecompetition = input("Enter date of the competition: ")
    venue = input("Enter venue: ")
    typeofthemedal = input("Enter type of the medal:")
    
    record=(groupname, Sizeofthegroup, dateofthecompetition, venue, typeofthemedal)
    records.append(record)

print("\nRecords of the competition:")
for record in records:
    print(record)
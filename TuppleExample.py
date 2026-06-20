#Packing
address=('227','Brickfield Shelters','Bangalore','Karnataka','562107')

for x in address:
    print(x, end=' ')

#Unpacking
houseno,apartName,city,state,pin=address

print()
print('HNO', houseno)
print('APT NO',apartName)
print(city)
print(state)
print(pin)
string = '10,11,12,33,44'
listdata = string.split(',')
for index, data in enumerate(listdata):
    listdata[index] = int(data)
print(listdata)
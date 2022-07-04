recordsList = []
fileHandle = open("IT244_U5_Data.txt", "r")
data = fileHandle.readlines()
for line in data:
    recordsList.append(line.strip())
fileHandle.close()
recordsList.append('5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA')
recordCount = len(recordsList)
file = open("IT244_U5_PromoCredit.csv", "w")
file.write('Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n')
for item in recordsList:
    file.write("%s,$500\n" % item)
print('There were', recordCount, 'records written to the promo credits csv file.')
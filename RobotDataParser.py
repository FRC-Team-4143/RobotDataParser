import csv

newData = []
firstrow = None
inputcsv = input("CSV to Parse:")
with open(inputcsv, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    rowlength = 0
    tempRow = [None] * rowlength    
    for row in data:
        if not firstrow:
            firstrow = row
            rowlength = len(row)
        if not (row[1] == ""):
            newData.append(tempRow.copy())
            tempRow = [None] * rowlength
        for index, column in enumerate(row):
            if not column == "":
                tempRow[index] = column
with open('parsed'+inputcsv,'w', newline='') as text_file:
    datawriter = csv.writer(text_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(firstrow)
    for row in newData:
        #row = row.tolist()
        datawriter.writerow(row)
print("done")

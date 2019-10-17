import csv
exampleFile = open('iris.csv')
exampleReader = csv.reader(iris)

for row in exampleReader:
  print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

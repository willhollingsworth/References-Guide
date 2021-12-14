import os,csv

os.chdir(os.path.dirname(os.path.realpath(__file__))) # force files to be written to script folder

with open('output.csv', mode='r') as open_file:
    csv_reader = csv.reader(open_file)

    # print(open_file)

    for row in csv_reader:   # print contents of file
        print(row)
    print(list(csv_reader))


    length = len(list(csv_reader))
    print('number of lines',length)
import os
import csv
import random
import time
os.chdir(os.path.dirname(os.path.realpath(__file__))) # force files to be written to script folder


#https://www.programiz.com/python-programming/writing-csv-files


with open('output.csv', mode='w') as open_file:
    csv_writer = csv.writer(open_file, delimiter=',', lineterminator = '\n')
    fieldnames = ['iter', 'time', 'random'] # create list eith fieldnames
    csv_writer.writerow(fieldnames) # write out the first row of the file with fieldnames

    for x in range(10): 
        cur_time = time.strftime("%H:%M:%S", time.localtime())
        csv_writer.writerow([x,cur_time,int(random.random()*10)])   
        time.sleep(.5)

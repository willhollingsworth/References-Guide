import os
os.chdir(os.path.dirname(os.path.realpath(__file__))) # force files to be written to script folder

# https://careerkarma.com/blog/python-check-if-file-exists/#:~:text=To%20check%20if%2C%20in%20Python,number%20of%20uses%20in%20Python.
def write_to_txt(filename,contents):    
        # simple function to write to a txt file
        f = open(filename, "w")
        f.write(contents)
        f.close()

count = 0   # used to count iteration
while True: # infinite loop
    filename = './files/increment_'+str(count)+'.txt'  # build the filename
    if not os.path.isfile(filename): # check if that file exists 
        write_to_txt(filename,'test')  # write it out
        print('write to',filename)   
        break                           # exit the loop
    count += 1
    print('already a file called',filename)



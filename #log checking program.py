#log checking program
#open log file
#read log file
#search for and print failed attempts

log_file = open("C:/Users/mouaj/windowslogs(1).txt", "r") #open the file in a read format
log_contents = log_file.read() # create a variable to read the file

for line in log_contents.splitlines(): #for loop which loops through the lines of the file
    if "Failed" in line: #searches for "failed" in the lines
        print(line.strip()) #if found, it will print them

log_file.close() #close the file

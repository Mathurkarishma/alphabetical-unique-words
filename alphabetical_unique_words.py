#This program will ask the user for a file and extract separate words line by line
#It will add only unique words to a list and sort it alphabetically

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    #If the user inputted an invalid file name, program will exit
list = []
#List begins empty
for line in fhand:
    words = line.split()
    for word in words:
        if word not in list:
            list.append(word)
            #Only adding unique words to list
        else:
            continue
list.sort()
#Alphabetical sort
print(list)
#Print list

#End of script

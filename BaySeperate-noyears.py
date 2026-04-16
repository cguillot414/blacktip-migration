#Matich shark project
#By C. Guillot

from dayOfYear import DOY

# =============================================================================
# bays = ["Aransas", 
#          "Corpus", 
#          "Galveston",
#          "Lower Laguna", 
#          "Matagorda", 
#          "Sabine", 
#          "San Antonio", 
#          "Upper Laguna", 
#          "Multiple"]
# =============================================================================
# =============================================================================
# By bay
#     bay number is element in "Bays" list above (ex. Aransas = bay0)
#     Year, Age0 Day1, Age1 Day1, Age2 Day1, Age0 lastDay, Age1 lastDay, Age2 lastDay
# 
# write years 1982 - 2021 in column 1 of each bay array (inside overall)
# 
# go through each line in CSV
# go through each col in CSV
# go through bay list and match an element index to Col 1 (bay name)
#     element index in Bays = element index in overall
# 
# 
# 
# for(each line in file):
#   scan through each row[0]
#   if row[0] matches, edit the same row[1] matrix
#       else, continue
#   if reach end, add matrix with default values w/ name 
# 
#   for each line in overall[row][1]
#       find the year and update values
#       if cannot find year, add it to end w/ default values + values
# =============================================================================

# blacktip-test.csv

overall = [[]]
filename = input("Type name of file WITH .xsls, csv, etc: ")
file = open(filename,'r')
lineList = file.readlines()
num_lines = sum(1 for _ in file)

firstline = True
for line in lineList: 
    wordList = line.split(",")
    if(firstline):
        overall[0] = ["Bay", "Day1Age0", "Day1Age1", "Day1Age2", "LDayAge0", "LDayAge1","LDayAge2"]
        firstline = False
        continue
    bayName = wordList[0]           #index 0)
    length = float(wordList[12])
    age = int(wordList[13])
    doy = DOY(wordList[3], int(wordList[2]), int(wordList[5]))
    
    for bay in (range(0,len(overall))):
        if((bayName).lower() == (overall[bay][0]).lower()):
            
            
            if(age == 0):
                if(doy < overall[bay][1]):
                    overall[bay][1] = doy
                if(doy > overall[bay][4]):
                    overall[bay][4] = doy
            elif(age == 1):
                if(doy < overall[bay][2]):
                    overall[bay][2] = doy
                if(doy > overall[bay][5]):
                    overall[bay][5] = doy
            elif(age == 2):
                if(doy < overall[bay][3]):
                    overall[bay][3] = doy
                if(doy > overall[bay][6]):
                    overall[bay][6] = doy
            break
        
        
        if (bay == len(overall)-1):
            
            
            
            #make a new line w/ default things
            overall.append([bayName, 999,999,999,-1,-1,-1])
            if(age == 0):
                overall[bay+1][1] = doy
                overall[bay+1][4] = doy
            elif(age == 1):
                overall[bay+1][2] = doy
                overall[bay+1][5] = doy
            elif(age == 2):
                overall[bay+1][3] = doy
                overall[bay+1][6] = doy
            break
        
        





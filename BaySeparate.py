#Matich shark project
#By CM Guillot Fall 2025


from dayOfYear import DOY

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

# =============================================================================
# overall = [Bay1, [[Year1, D1A0, ....],
#                   [Year2, D1A0, ....],
#                   ...                 
#                  ], 
#            Bay2, 
#            Bay3, 
#            ...
#           ]
# =============================================================================

overall = [[]]
# filename = input("Type name of file WITH .xsls, csv, etc: ")
filename = "Texas-blacktip-shark-data_Blacktip-size-data-for-analys.csv"
file = open(filename,'r')
lineList = file.readlines()
num_lines = sum(1 for _ in file)

yearMin = 9999999
yearMax = -1

firstline = True
for line in lineList: 
    wordList = line.split(",")
    if(firstline):
        overall[0] = ["Bay", ["Year", ["Day1Age0", "Day1Age1", "Day1Age2", "LDayAge0", "LDayAge1","LDayAge2"]
                             ]
                     ]
        firstline = False
        continue
    bayName = wordList[0]
    length = float(wordList[12])
    age = int(wordList[13])
    year = int(wordList[5])
    doy = DOY(wordList[3], int(wordList[2]), year)
    
    if(year < yearMin):     #calculates min year for graph ranges
        yearMin = year
    if(year > yearMax):     #calculates max year for graph ranges
        yearMax = year
    
    for bay in (range(0,len(overall))):
        if((bayName).lower() == (overall[bay][0]).lower()):
            
            for y in (range(0, len(overall[bay]))):
                if(year == overall[bay][y][0]):
                    if(age == 0):
                        if(doy < overall[bay][y][1][0]):
                            overall[bay][y][1][0] = doy
                        if(doy > overall[bay][y][1][3]):
                            overall[bay][y][1][3] = doy
                    elif(age == 1):
                        if(doy < overall[bay][y][1][1]):
                            overall[bay][y][1][1] = doy
                        if(doy > overall[bay][y][1][4]):
                            overall[bay][y][1][4] = doy
                    elif(age == 2):
                        if(doy < overall[bay][y][1][2]):
                            overall[bay][y][1][2] = doy
                        if(doy > overall[bay][y][1][5]):
                            overall[bay][y][1][5] = doy
                    break 
                if(y == len(overall[bay])-1):
                    overall[bay].append([year, [999, 999, 999, -1, -1, -1]])  #add year
                    if(age == 0):
                        overall[bay][y+1][1][0] = doy
                        overall[bay][y+1][1][3] = doy
                    elif(age == 1):
                        overall[bay][y+1][1][1] = doy
                        overall[bay][y+1][1][4] = doy
                    elif(age == 2):
                        overall[bay][y+1][1][2] = doy
                        overall[bay][y+1][1][5] = doy
                    break 
                    
            break
            
            
        if (bay == len(overall)-1):
            #make a new line w/ default things
            overall.append([bayName, [year, [999,999,999,-1,-1,-1]]])     #add bay
            if(age == 0):
                overall[bay+1][1][1][0] = doy
                overall[bay+1][1][1][3] = doy
            elif(age == 1):
                overall[bay+1][1][1][1] = doy
                overall[bay+1][1][1][4] = doy
            elif(age == 2):
                overall[bay+1][1][1][2] = doy
                overall[bay+1][1][1][5] = doy
            break
            
            





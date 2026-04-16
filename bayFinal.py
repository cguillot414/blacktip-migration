#Matich Shark Project
#By CM Guillot Fall 2025

from BaySeparate import (overall)
#from bayGraphs import * #kept so that it will run

# optional: yes/no to save image
# optional: text to enter file name


# TODO: writing first and last days of each year and each bay as csv file 
# all bays in same file 
with open("blacktip-shark-final-nums.csv", "w") as file:
    for bay in range(len(overall)):
        for year in range(1,len(overall[bay])):
            file.write(str(overall[bay][0]) + ", ")             #bay name
            file.write(str(overall[bay][year][0]) + ", ")       #year
            for data in overall[bay][year][1]:
                if((data != 999) and (data != -1)):             #if data is not default value
                  file.write(str(data) + ", ")                      #write what the num is
                else:
                    file.write(" , ")
            file.write("\n")
        
        
# TODO: input file name as text

#Matich Shark Project
#By CM Guillot Spring 2026

from BaySeparate import (overall, yearMin, yearMax)
import matplotlib.pyplot as plot

yearMin -= 2 #adjusts min year for graph readability
yearMax += 2 #adjusts max year for graph readability

pointSize = 3; #size of dots

a0 = []
a1 = []
a2 = []
years0 = []
years1 = []
years2 = []


for b in range(1, len(overall)): #go by bays
    bayTitle = overall[b][0]
    plot.suptitle(str(bayTitle + " Bay"), fontsize = 20, y = 1)
    
    plot.figwidth = 300
    plot.figheight = 300
    
    #setup full graph
    plot.xticks([yearMin, yearMin + 5, yearMin + 10, yearMin + 15, yearMin + 20, yearMin + 25, yearMin + 30, yearMin + 35, yearMin + 40, yearMin + 45, yearMin + 50])
    plot.xlim(yearMin, yearMax)
    plot.ylim(00, 370)
    plot.title("Time Between Last Recording in Year X & First Recording in Year X+1", fontsize = 10)
    plot.ylabel("Number of Days Between Recordings")
    plot.xlabel("Year X")
    
    for y in range(1, len(overall[b])-1):
        yearX = overall[b][y][0]
        yearXdata = overall[b][y][1]
        yearX1data = overall[b][y+1][1]
        
        #index variables for readibility
        age0begin = 0
        age0end = 3
        age1begin = 1
        age1end = 4
        age2begin = 2
        age2end = 5
        
        age0diff = (365 - yearXdata[age0end]) + yearX1data[age0begin]
        if(age0diff < 365):
            a0.append(age0diff)
            years0.append(yearX)
        age1diff = (365 - yearXdata[age1end]) + yearX1data[age1begin]
        if(age1diff < 365):
            a1.append(age1diff)
            years1.append(yearX)
        age2diff = (365 - yearXdata[age2end]) + yearX1data[age2begin]
        if(age2diff < 365):
            a2.append(age2diff)
            years2.append(yearX)
    
    
    plot.plot(years0, a0, 'r-', years1, a1, 'b-', years2, a2, 'g-', markersize = pointSize)
    plot.plot(years0, a0, 'ro', years1, a1, 'bo', years2, a2, 'go', markersize = pointSize)

    a0.clear()
    a1.clear()
    a2.clear()
    years0.clear()
    years1.clear()
    years2.clear()
    plot.legend(['Age 0', 'Age 1', 'Age 2'], loc='lower left')
    plot.savefig("graphs/" + bayTitle + "Offseason" + ".png")
    plot.show()
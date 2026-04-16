#Matich shark project
#By CM Guillot Fall 2025

from BaySeparate import (overall, yearMin, yearMax)
import matplotlib.pyplot as plot
from importlib import reload

plot = reload(plot)

yearMin -= 2 #adjusts min year for graph readability
yearMax += 2 #adjusts max year for graph readability

# sort based off of bay name 
overall.sort(key = lambda bay: bay[0] if bay[0] != "Bay" else "")

pointSize = 3; #size of dots

# item = 1    #temporary testing value
for b in range(1, len(overall)): #go by bays
    bayTitle = overall[b][0]
    plot.suptitle(str(bayTitle + " Bay"), fontsize = 20, y = 1)
    
    plot.figwidth = 300
    plot.figheight = 300
    
    #setup full graph
    plot.ylim(yearMin,yearMax)
    plot.xticks([])
    plot.axis('off')
    
    #setup plot for age 0
    plot.subplot(1,3,1)
    plot.xticks([0, 365])
    plot.xlim(0,365)
    plot.ylim(yearMin, yearMax)
    plot.title("Age 0", fontsize = 10)
    plot.ylabel("Year")
    
    #setup plot for age 1
    plot.subplot(1, 3, 2)
    plot.yticks([])
    plot.xticks([0, 365])
    plot.xlim(0,365)
    plot.ylim(yearMin,yearMax)
    plot.title("Age 1", fontsize = 10)
    plot.xlabel("Day of Year")
    
    #setup plot for age 2
    plot.subplot(1,3,3)
    plot.yticks([])
    plot.xticks([0,365])
    plot.xlim(0,365)
    plot.ylim(1980,2022)
    plot.title("Age 2", fontsize = 10)
    
    
    
    for y in range(1, len(overall[b])): #go by years
        year = overall[b][y][0]
        bayInfo = overall[b][y][1]
        
        # set variables for different nums (easy graphing and code readability)
        doyBegin0 = bayInfo[0]
        doyEnd0 = bayInfo[3]
        doyBegin1 = bayInfo[1]
        doyEnd1 = bayInfo[4]
        doyBegin2 = bayInfo[2]
        doyEnd2 = bayInfo[5]
        
        # filtering out placeholder nums
        if (doyBegin0 == 999):
            doyBegin0 = doyEnd0
        elif (doyEnd0 == -1):
            doyEnd0 = doyBegin0
        if (doyBegin1 == 999):
            doyBegin1 = doyEnd0
        elif (doyEnd1 == -1):
            doyEnd1 = doyBegin1
        if (doyBegin2 == 999):
            doyBegin2 = doyEnd2
        elif (doyEnd2 == -1):
            doyEnd2 = doyBegin2
        
        plot.subplot(1,3,1) #age 0
        if ((doyEnd0 != -1) & (doyBegin0 != 999)):
            plot.plot([doyBegin0, doyEnd0], [year,year], 'o-', markersize = pointSize)
            
        plot.subplot(1,3,2) #age 1
        if ((doyEnd1 != -1) & (doyBegin1 != 999)):
            plot.plot([doyBegin1, doyEnd1], [year,year], 'o-', markersize = pointSize)
            
        plot.subplot(1,3,3) #age 2
        if ((doyEnd2 != -1) & (doyBegin2 != 999)):
            plot.plot([doyBegin2, doyEnd2], [year,year], 'o-', markersize = pointSize)
            
    plot.savefig(bayTitle + ".png")
    plot.show()



# optional: yes/no to save image
# optional: text to enter file name


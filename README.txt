Project written by Caden Guillot under Dr. Phillip Matich
Texas A&M University



1. Running the program: 

Run bayGraphs.py to get the year vs doy plots based off of the data in inputted into BaySeparate.py
- Files formatted like Bay,STATION_CODE,Day,Month,Month2,Year,Season,COMPLETION_DTTM,Temperature,Salinity,Turbidity,DO,Length,Age
Run bayOffSeason.py to get year vs time between recordings on same data inputted into BaySeparate.py

If you run this is VS code, then graphs will pop-up one at a time, one for each bay in the dataset. 
You will have to close the window showing a graph for the next one to appear. 

If you run this in Spyder, the graphs will appear normally. 




2. Dataset & Plot Info: 

The data set is of lengths of Blacktip sharks in various bays in the Gulf of Mexico, throughout a ~40 year time span. 
The dates of the measurements were taken, and sorted into graphs showing the time frame that the sharks were found year by year. 
Data is separated by bay and age group. 




3. Program info: 


The entire program is made to be as dynamic and customizable as possible, to allow any data set to be inputted to get similar graphs, 
as long as the data set has variables in the same order. 

Currently, only the file "Texas-blacktip-shark-data_Blacktip-size-data-for-analys.csv" can be used to make graphs, but 
it is set up to allow any file to be inputted, by typing into the python file itself. 

The number of graphs and year range is dynamic, and completely dependent on the different bays that can be found in the inputted dataset. 
These two details are able to change depending on what data is inputted.







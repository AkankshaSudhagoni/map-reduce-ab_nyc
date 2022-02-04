# map-reduce-ab_nyc
## Practicing mapping & sort data & reduce data

From 2008, visitors and hosts have utilized Airbnb to broaden their travel options and offer a more distinctive, personalized way of seeing the world. For the year 2019, this information describes the listing activity and analytics in NYC, NY. <br>
This data file contains all of the information needed to learn more about hosts, as well as the relevant metrics for making predictions and drawing conclusions. <br>
<br>
###  In this I tried to find which Airbnb was been noticed to have high rate of hosts visting over 2008 to 2019. <br>
 
 When we look at the reduced data sets , we can clearly notice that they are high rate of hosts attending Bedford-Stuyvesant in the its neighborhoods of Newyork and number of vistors have been incresing over the decade and the chart below also shows how many neighborhoods have been increasing its rate of vistors and what all other neighborhoods in the area of Newyork have been decreasing.
 
 
```
cat dataset.csv | python mapper.py | sort  | python reducer.py > SUDHAGONIoutput.txt
```
 
 ![Image](/image/Capture.PNG)

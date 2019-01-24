# class project
# this is an analysis of the NYPD Motor Vehicle Collision
# found in this file:
#NYPD_Motor_Vehicle_Collisions.csv
# downloaded from https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95/data


from collections import Counter 
  
data_set = "Sedan Sedan Sedan Station wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Sedan Sedan Box Truck Sedan Station Wagon/Sport Utility Vehicle Tractor Truck Diesel Station Wagon/Sport Utility Vehicle Box Truck Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Bike Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Taxi Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Box Truck Van Sedan Sedan Sedan Sedan Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Box Truck Sedan Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Box Truck Sedan Sedan Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Bus Sedan Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Sedan Box Truck Bike Station Wagon/Sport Utility Vehicle Bus Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Sedan Sedan Sedan Sedan Sedan Sedan Sedan StationWagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Sedan Sedan Sedan Sedan Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/SportUtility Vehicle Sedan Station Wagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Motorcycle Station Wagon/SportUtility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Pick-up Truck TractorTruck Diesel Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Box Truck Station Wagon/Sport Utility Vehicle StationWagon/Sport Utility Vehicle Sedan Sedan Station Wagon/Sport Utility Vehicle Sedan Sedan Pick-up Truck Sedan Station Wagon/Sport Utility Vehicle Taxi Sedan Sedan Station Wagon/SportUtility Vehicle Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan StationWagon/Sport Utility Vehicle Box Truck Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle StationWagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle StationWagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle Sedan Station Wagon/Sport Utility Vehicle TaxiStation Wagon/Sport Utility Vehicle Station Wagon/Sport Utility Vehicle Taxi Box Truck Sedan Sedan Sedan Taxi Sedan Sedan Station Wagon/Sport Utility Vehicle Bike Sedan Sedan Station Wagon/SportUtility Vehicle Station Wagon/Sport Utility Vehicle Motorcycle Station Wagon/Sport Utility Vehicle Sedan Sedan Sedan Box Truck Sedan"

# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
  
print(most_occur)

# For this data, I've basically focused on the type of vehicles that were in accidents. I used Pythton to analyze this data. The data was based on NYPD Motor Vehicle Collisions.Based on the data, I concluded that most motor vehicle accidents happened with Vehicle 82, Utility 78, Station 76, and Sedan 74.





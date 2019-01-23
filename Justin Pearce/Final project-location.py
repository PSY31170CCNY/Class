from collections import Counter 
  
data_set = "BRONX BROOKLYN BROOKLYN BRONX QUEENS MANHATTAN BROOKLYN MANHATTAN MANHATTAN STATEN ISLAND MANHATTAN MANHATTAN BROOKLYN QUEENS MANHATTAN BROOKLYN QUEENS BRONX BROOKLYN BROOKLYN BROOKLYNQUEENS QUEENS STATEN ISLAND QUEENS BROOKLYN QUEENS STATEN ISLAND QUEENS BROOKLYN BROOKLYN BROOKLYN QUEENS STATEN ISLAND QUEENS QUEENS QUEENS STATEN ISLAND BROOKLYN BROOKLYN BRONX BROOKLYN BROOKLYN QUEENS QUEENS BROOKLYN BRONX BRONX BROOKLYN QUEENS QUEENS BROOKLYN BRONX BROOKLYN BROOKLYN BROOKLYN STATEN ISLAND BROOKLYN"  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
  
print(most_occur) 
# Using python I analyzed the data based on the most used location where accidents happen in the list. The data was on nyc motor vehicle  collisions. Based on the data and code I concluded that most motor vehicle accidents happened  in Brooklyn 22 accidents followed by Queens with 15 accidents bronx had 7 and Manhattan had 6.

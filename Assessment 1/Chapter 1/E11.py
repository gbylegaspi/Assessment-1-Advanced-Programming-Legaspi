# Create a tuple with given values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Access the value at index -3
value = year[-3]

# Reverse the tuple
reversed = tuple(reversed(year))

# Count number of times 2009 is in the tuple
count_2009 = year.count(2009)

# Get the index value of 2018
index_2018 = year.index(2018)

# Find length of given tuple
length = len(year)

# Output the results
print("value at index -3:", value)
print("original tuple:", year)
print("reversed tuple:", reversed)
print("count of 2009 in tuple:", count_2009)
print("index of 2018:", index_2018)
print("ength of tuple:", length)

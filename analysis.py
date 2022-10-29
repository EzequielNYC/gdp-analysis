import csv
def get_highest_gdp(data, year):
    highest = float(data[0][year])
    highest_name = (data[0]["GeoName"])
    for row in data:
        val = float(row[year])
        name = row["GeoName"]
        if val > highest:
            highest = val
            highest_name = name 

    return highest_name

def get_lowest_gdp(data, year):
    lowest = float("inf")
    lowest_name = (data[0]["GeoName"])
    for row in data:
        val = float(row[year])
        name = row["GeoName"]
        if val < lowest:
            lowest = val
            lowest_name = name
    return lowest_name





def get_state_gdp (data,state, year):
    for row in data:
        if row['GeoName'] == state:
            return float(row[year])
        

list_data = []

with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)


# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data , '2020'))
# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp( list_data  ,'2020'))

print(get_state_gdp(list_data,'New York','2020'))

prev = get_state_gdp(list_data, "New York", "2019")
new = get_state_gdp(list_data, "New York", "2020")

print(new - prev)

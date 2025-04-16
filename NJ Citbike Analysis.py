### Part1
import pandas as pd
import csv

# Read February data
feb_df = pd.read_csv("JC-citibike-tripdata-2022-Febuary.csv")

# Read May data
may_df = pd.read_csv("JC-citibike-tripdata-2022-May.csv")

from datetime import datetime

# Reading the February and May data files and storing them as list of lists
feb_data = []
file = open("JC-citibike-tripdata-2022-Febuary.csv")
reader = csv.reader(file)
for row in reader:
    feb_data.append(row)

may_data = []
file = open("JC-citibike-tripdata-2022-May.csv")
reader = csv.reader(file)
for row in reader:
    may_data.append(row)


### Part2
# Define a function to collect and print the required details
def print_details(data):
    # Initialize variables to store the statistics
    members = 0
    casual_users = 0
    electric_bikes = 0
    classic_bikes = 0
    total_duration = 0
    start_stations = {}
    end_stations = {}

    # Loop through each ride in the data
    for ride in data[1:]:
        # Collect the duration, starting station, and ending station for each ride
        start_time = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        duration_sec = (end_time - start_time).seconds
        # convert seconds to hours
        duration = duration_sec / 3600
        total_duration = total_duration + duration
        start_station = ride[4]
        end_station = ride[6]

        # Update the count for each starting station
        if start_station in start_stations:
            start_stations[start_station] += 1
            # updates the count for each starting station in the start_stations dictionary
        else:
            start_stations[start_station] = 1
            # If the start_station key does not exist in the dictionary
            # it adds the station in the dictionary and starts the count for that station from 1

        # Update the count for each ending station
        if end_station in end_stations:
            end_stations[end_station] += 1
        else:
            end_stations[end_station] = 1

        # Update the count for each type of user and each type of bike
        if ride[12] == 'member':
            members = members + 1
        else:
            casual_users = casual_users + 1

        if ride[1] == 'electric_bike':
            electric_bikes = electric_bikes + 1
        else:
            classic_bikes = classic_bikes + 1

    # Calculate the average daily trip duration
    num_days = len(set([ride[1] for ride in data[1:]]))
    # --> Return the number of unique dates in our set after creating a list of unique dates
    avg_duration = total_duration / num_days

    # Find the 5 most popular starting stations and ending stations
    popular_start_stations = sorted(start_stations.items(), key=lambda x: x[1], reverse=True)[:5]
    popular_end_stations = sorted(end_stations.items(), key=lambda x: x[1], reverse=True)[:5]
    # converts and sorts the start_stations and end_stations into dictionary and arranging the data
    # using reverse in descending order based on the values of each key-value pair


    # Print the data
    print()
    print('Average daily trip duration:', avg_duration)
    print('\n 5 Most popular starting stations:')
    for station in popular_start_stations:
        print(station[0], station[1])
    print('\n 5 Most popular ending stations:')
    for station in popular_end_stations:
        print(station[0], station[1])

    print('\nNumber of members:', members)
    print('Number of casual users:', casual_users)
    print('Number of electric bikes:', electric_bikes)
    print('Number of classic bikes: ', classic_bikes)
    return members, casual_users, electric_bikes, classic_bikes


### Part4
# Print the statistics for the February data
mem_feb, cas_feb, electric_feb, classic_feb = print_details(feb_data)

# Print the statistics for the May data
mem_may, cas_may, electric_may, classic_may = print_details(may_data)

### Part 3
print("\nThe Ridership Data: ")
if mem_feb < mem_may:
    print("--> The Members using the bike increase in the month of May")
else:
    print("--> The Members using the bike are more in the month of Feb")

if cas_feb < cas_may:
    print("--> The casual users using the bike increase in the month of May")
else:
    print("--> The casual users using the bike are more in the month of Feb")

if electric_feb < electric_may:
    print("--> The number of users using electric bikes are more in the month of May")
else:
    print("--> The number of users using electric bikes are more in the month of Feb")

if classic_feb < classic_may:
    print("--> The number of users using classic bikes are more in the month of May")
else:
    print("--> The number of users using classic bikes are more in the month of feb")

# Merge the data files into a pandas structure and print it
print()
feb_df = pd.DataFrame(feb_data[1:], columns=feb_data[0])

# convert may_data to dataframe
may_df = pd.DataFrame(may_data[1:], columns=may_data[0])

# merge the dataframes
merged_df = pd.concat([feb_df, may_df], axis=0)
print(merged_df)

###part5
print("This is the end of processing")

"""
Project 2 Explore US Bikeshare Data
Martin Meyer - mmeyer@te.com

"""


# import warnings and ignore Future Warnings to clear output
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import time
import pandas as pd

# dictionary with cities and filenames
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Welcome to the script
    print('\nHello! Let\'s explore some US bikeshare data!')
    print("You can analyze data for Chicago, Washington and New York City")

    # get user input for city (chicago, new york city, washington).
    city = input("\nPlease enter the city you want to analyze:\n ").lower()

    # while loop to handle invalid input for city
    while city not in CITY_DATA:
        print("Your entered city \"{}\" is invalid!".format(city))
        city = input("Please enter a valid city - Chicago, New York City or Washington:\n").lower()

    # Define user input for time filter and get user input
    choice = ["month", "day", "both", "no"]
    print("\nWould you like to filter data by month, day, both, or not at all?")
    time_filter = input("Please enter 'month', 'day', 'both' or 'no':\n ").lower()

    # while loop to handle invalid input for time_filter
    while time_filter not in choice:
        print("Invalid input!")
        time_filter = input("Please enter 'month', 'day', 'both' or 'no':\n ").lower()

    # define possible input for month and day
    months = ["january", "february", "march", "april", "may", "june"]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    # get input for month and day according time_filter with while loops to handle invalid input
    if time_filter == 'month':
        month = input("Which month? January, February, March, April, May, June:\n ").lower()
        day = "all"
        while month not in months:
            print("Invalid month")
            month = input("Please enter - January, February, March, April, May, June:\n " ).lower()
    elif time_filter == "day":
        month = "all"
        day = input("Please enter weekday. Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday:\n ").lower()
        while day not in days:
            print("invalid weekday!")
            day = input("Please enter weekday. Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday:\n ").lower()
    elif time_filter == "both":
        month = input("Which month? January, February, March, April, May, June:\n ").lower()
        #day = "all"
        while month not in months:
            print("Invalid month")
            month = input("Please enter - January, February, March, April, May, June:\n " ).lower()
        day = input("Please enter weekday. Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday:\n ").lower()
        while day not in days:
            print("invalid weekday!")
            day = input("Please enter weekday. Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday:\n ").lower()
    else:
        month = "all"
        day = "all"

    # Show user input
    print("\nYour selected time filter = '{}': ".format(time_filter))
    print("Selected city = ", city.title())
    print("Selected month = ", month.title())
    print("Selected day = ", day.title())
    # print separator line for well arranged output
    print('-'*80)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
      """
    # initial start time before executing the code
    start_time = time.time()


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime("%B")
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != "all":
        df = df[df['month'] == month.title()]
    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    # calculate and print time to import and filter data
    print("\nTime to import and filter data: {} sec.".format(round(time.time() - start_time, 5)))
    # print separator line for well arranged output
    print('-'*80)

    #print("Do you want to inspect the first 5 lines of the selected data?")
    #insp_data = input("Enter y to display data:\n")

    #if insp_data == 'y':
        #df.head()

    return df

def time_stats(df):
    """
    Calculates Statistics for month, day and hour:
        most common month
        most common day of week
        most common hour of day
    and prints these popular times of travel and the time for executing the code
    """
    # initial start time before executing the code
    start_time = time.time()

    # calculate month statistics
    max_travels_month = df['month'].value_counts().max()
    most_freq_month = df['month'].value_counts().argmax()
    month_count = len(df['month'].value_counts())

    # calculating day statistic
    max_travels_day = df['day_of_week'].value_counts().max()
    most_freq_day = df['day_of_week'].value_counts().argmax()
    day_count = len(df['day_of_week'].value_counts())

    # calculating hour statistic
    max_travels_hour = df['hour'].value_counts().max()
    most_freq_hour = df['hour'].value_counts().argmax()


    print("Most Frequent Time's of Travel:")

    # print month statement dependent on selection of one or all months
    if month_count > 1:
        print("The most frequent month of all is {} with {} travels.".format(most_freq_month, max_travels_month))
    else:
        print("In selected month {} there were {} travels.".format(most_freq_month, max_travels_month))

    # print day statement dependent on selection of one or all days
    if day_count > 1:
        print("The most frequent Day of all is {} with {} travels.".format(most_freq_day, max_travels_day))
    else:
        print("In selected day {} there were {} travels.".format(most_freq_day, max_travels_day))

     # print hour statement
    print("The most frequent Hour of all is {} o\'clock with {} travels.".format(most_freq_hour, max_travels_hour))

    # calculate and print time to execute time_stats
    print("\nTime to execute: {} sec.".format(round(time.time() - start_time, 5)))

    # print separator line for well arranged output
    print('-'*80)

def station_stats(df):
    """
    Calculates and prints statistics for popular stations and trip
    most common start station
    most common end station
    most common trip from start to end (i.e., most frequent combination of start station and end station)
    """
    # initial start time before executing the code
    start_time = time.time()

    # calculating start station statistics
    pop_start_station = df['Start Station'].value_counts().argmax()
    pop_start_station_count = df['Start Station'].value_counts().max()

    # calculating end station statistics
    pop_end_station = df['End Station'].value_counts().argmax()
    pop_end_station_count = df['End Station'].value_counts().max()

    # calculating top 5 most frequent combination
    comb = pd.Series("Start: " + df["Start Station"]+ " --- " + "End: " + df["End Station"])
    count_comb = comb.value_counts()[0:5]

    # print station statistics and time to execute code
    print("Popular Stations and Trips:")
    print()
    print("The most popular Start Station is -{}- with {} travels".format(pop_start_station, pop_start_station_count))
    print("The most popular End Station is -{}- with {} arivals".format(pop_end_station, pop_end_station_count))
    print("\nTop 5 Trips with total amount for each combination:")
    print()
    print(count_comb.to_string())

    # calculate and print time to execute station_stats
    print("\nTime to execute: {} sec.".format(round(time.time() - start_time, 5)))

    # print separator line for well arranged output
    print('-'*80)

def trip_duration_stats(df):
    """
    Calculates and prints the total and average travel duration.

    """
    # initial start time before executing the code
    start_time = time.time()

    # Calculate total and mean travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    avg_travel_time = df['Trip Duration'].mean()/60

    # print total and mean travel time
    print("Trip Duration Times:")
    print("\nTotal Travel Time is {} hours ".format(round(total_travel_time, 5)))
    print("Mean Travel Time is {} minutes ".format(round(avg_travel_time, 5)))

    # calculate and print time to execute trip_duration_stats
    print("\nTime to execute: {} sec.".format(time.time() - start_time))
    #print("\nTime to execute: {} sec.".format(round(time.time() - start_time, 10)))

    # print separator line for well arranged output
    print('-'*80)


def user_stats(df):
    """
    Calculates and prints user statistics:

    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)
    """


    # initial start time before executing the code
    start_time = time.time()

    print("User Info:")

    #User Types
    print("\nUser Type and Count:")
    print(df["User Type"].value_counts().to_string())

    # print separator line for well arranged output
    print('-'*10)

    # calculate counts of each gender and check if Gender is in df
    if 'Gender' not in df.columns:
        print("No gender data for selected city available!")
    else:
        print("Counts of each gender:")
        print(df['Gender'].value_counts().to_string())

    # calculate earliest, most recent, most common year of birth and check if Birth Year is in df
    if 'Birth Year' not in df.columns:
        print("No birth year data for selected city available!")
    else:
        min_birthyear = int(df['Birth Year'].min())
        max_birthyear = int(df['Birth Year'].max())
        common_birthyear = int(df['Birth Year'].mode())

        # print separator line for well arranged output
        print('-'*10)


        print("Birth Year Data:")
        print("\nEarliest Birth Year: {}".format(min_birthyear))
        print("Youngest Birth Year: {}".format(max_birthyear))
        print("Most common Birth Year: {}".format(common_birthyear))

    # calculate and print time to execute user_stats
    print("\nTime to execute: {} sec.".format(round(time.time() - start_time, 5)))

    # print separator line for well arranged output
    print('-'*80)

def print_results(df):
    """
    prints separator line for well arranged output
    and prints analysis result
    """
    print('-'*80)
    print('ANALYSIS OF BIKE SHARE DATA')
    print('-'*80)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)


def main():
    """
    Executes Functions to get filters and load data
    asks user to inspect data
    Executes Functions to analyze data
    """

    while True:
        #get filters and load data
        city, month, day = get_filters()
        df =  load_data(city, month, day)

        # Inspect data yes or no:
        insp_choice = ['yes', 'no']
        print("Do you want to inspect the first 5 lines of the selected data?")
        inspect_data = input("Enter yes to display data or no to continue:\n").lower()
        while inspect_data not in insp_choice:
            print("Invalid input")
            inspect_data = input("Enter yes to display data or no to continue:\n").lower()
        if inspect_data == 'yes':
            print('-'*80)
            print('DATA OVERVIEW')
            print('-'*80)
            pd.set_option('display.max_columns', 15)
            print(df.head())
            print('-'*80)

            # analyze data or restart?
            print('\nDo you want to analyze the data or restart?')
            new_data = input("Enter yes to analyze or no to restart or exit:\n").lower()
            while new_data not in insp_choice:
                print("Invalid input")
                new_data = input("Enter yes to analyze or no to restart or exit:\n").lower()

            if new_data == 'yes':
                print_results(df)


        elif inspect_data == 'no':
            # print separator line for well arranged output
            print('-'*80)
            print('ANALYSIS OF BIKE SHARE DATA')
            print('-'*80)
            # analyze data
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thanks for using this script! \nMay the force be with you!")
            break


if __name__ == "__main__":
	main()

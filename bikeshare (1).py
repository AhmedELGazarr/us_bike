import time
import pandas as pd
import numpy as np

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
    print('Let\'s explore some US bikeshare data!')
   # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nWould you like to see data for Chicago, new york city , Washington?\n').lower()
        if city not in cities:
            print('\nwrong input, please try again.')
            continue
        else:
            break
           
    # get user input for month (all, january, february, ... , june)          
    months = ("all", 'january', 'february', 'march', 'april', 'may', 'june')   
    while True:
        month = input(('\nWhich month would you like to filter by: January, February, March, April, May, June? \nor all for no month filter.\n').lower())
        if month not in months:
            print('wrong input, please try again.')
            continue
        else:
            break
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('\nWhich day would you like to filter by:Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday,  \nor all for no day filter.\n').lower()
        if day not in days:
            print('Invalid entry, please try again.')
            continue
        else:
            break 

            
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Arguments:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day to filter by, or "all" to apply no day filter
    Returns:
        df-Pandas DataFrame containing city data filtered by month and day
    """
    # load file into df
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

      # extract month and day of week from Start Time to create new columns:
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['start hour']=df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        # filter by day to create the new dataframe
        df = df[df['day'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel..\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is:{}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('The most common day is: {}'.format(df['day'].mode()[0]))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     #display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start)

     #display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)

     #display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Frequent Trip'].mode()[0]
    print('Most common trip:', common_trip)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, 'seconds')
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', mean_travel_time, 'seconds')

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
     """Displays statistics on bikeshare users."""
     
     print('\nCalculating User Stats...\n')
     start_time = time.time()

    
     # Display counts of user types
     user_type_count = df['User Type'].value_counts()
     print('User Type Count:\n', user_type_count)
    
    
     # Display counts of gender
     try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
     except KeyError: 
        print('\nGender Count: No data available.')
     # Display earliest, most recent, and most common year of birth
     try:
        birth_min = int(df['Birth Year'].min())
        print('\nEarliest year of birth:', birth_min)
     except KeyError:
        print('\nEarliest year of birth: No data available.')
        
        
     try:
        birth_max = int(df['Birth Year'].max())
        print('Most recent year of birth:', birth_max)
     except KeyError:
        print('Most recent year of birth: No data available.')
        
     try:
        birth_mode = int(df['Birth Year'].mode()[0])
        print('Most common year of birth:', birth_mode)
     except KeyError:
        print('Most common year of birth: No data available.')
        
        
     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)
 

def display_data(df):
    """Displays raw data 5 rows at a time, if requested."""
    
    show_data = input('\nWould you like to see 5 rows of raw data? yes or no:\n').lower()
    if show_data != 'no':
        i = 0
        while (i < df['Start Time'].count() and show_data != 'no'):
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('\nWould you like to see 5 more rows of data? yes or no:\n').lower()
            if more_data != 'yes':
                break
                
                
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('Would you like to restart? Enter yes or no.')
        if restart.lower() != 'yes':
            print('Thank You')
            break


if __name__ == "__main__":
	main()
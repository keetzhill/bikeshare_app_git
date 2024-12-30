# Adding note to bikeshare file for git exercise.
import time
import pandas as pd
import numpy as np

# Updated for readability on 30 Dec 2024 for git exercise.

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday',
              'thursday', 'friday', 'saturday', 'sunday', 'all']
VALID_RAW_DATA_OPTIONS = ['yes', 'no']


def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input! Please choose from the following options: {
                  ', '.join(valid_options)}")



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze and if they want to see raw data.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) raw_data - if the user wants to see the first five rows of the data
    """
    print("Hello! Let's explore some US bikeshare data!")

    city = get_user_input(
        "Select from the following cities: Chicago, New York City, or Washington: ", CITY_DATA.keys())
    raw_data = get_user_input(
        "Would you like to see the first five rows of raw data? Enter yes or no: ", VALID_RAW_DATA_OPTIONS)
    month = get_user_input(
        "Enter the month to display: January, February, March, April, May, June, or All: ", VALID_MONTHS)
    day = get_user_input(
        "Enter the day to display: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All: ", VALID_DAYS)

    return city, month, day, raw_data

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input(
            "Select from the following cities: Chicago, New York City, or Washington: ").lower()
        if city in CITY_DATA:
            break
        else:
            print(
                "DATA NOT AVAILABLE! Select from the following: Chicago, New York City, Washington:")

    # Ask if the user wants to see the first five rows of data
    while True:
        raw_data = input(
            "Would you like to see the first five rows of raw data? Enter yes or no: ").lower()
        if raw_data in ['yes', 'no']:
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    # Get user input for month (all, january, february, ..., june)
    while True:
        month = input(
            "Enter the month to display: January, February, March, April, May, June, or All: ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("DATA NOT AVAILABLE! Select from the following: January, February, March, April, May, June, or All:")

    # Get user input for day of week (all, monday, tuesday, ..., sunday)
    while True:
        day = input(
            "Enter the day of the week to display: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All: ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Check the spelling! Enter one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All.")

    print("-" * 40)
    return city, month, day, raw_data


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data for the specified city
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is:', popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day is:', popular_day)

    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is:', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is:', popular_end_station)

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('The most popular trip is:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender_counts)
    else:
        print('Gender data not available for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth:', earliest_year)
        print('Most recent year of birth:', most_recent_year)
        print('Most common year of birth:', most_common_year)
    else:
        print('Birth year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def descriptive_stats(df):
    """
    Generates and displays descriptive statistics for the DataFrame.

    Args:
        df - Pandas DataFrame containing city data
    """
    print("\nGenerating Descriptive Statistics...\n")

    # Display descriptive statistics
    print(df.describe())

    print("\nDescriptive statistics generated.\n")


def display_data(df):
    """
    Prompt the user if they want to see the first five rows of data and display it.
    Continue iterating, showing the next five rows at each prompt.
    Stop the program when the user says no or when there is no more data to display.

    Args:
        df - Pandas DataFrame containing city data
    """
    start_loc = 0
    while True:
        view_data = input(
            "Would you like to see the next five rows of data? Enter yes or no: ").lower()
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            if start_loc >= len(df):
                print("No more data to display.")
                break
        elif view_data == 'no':
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Define the main function with the call to display_data added


def main():
    while True:
        city, month, day, raw_data = get_filters()
        df = load_data(city, month, day)

        # Display raw data in batches of five rows if the user wants to see it
        if raw_data == 'yes':
            display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        descriptive_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

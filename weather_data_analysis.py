import pandas as pd

weather = pd.read_csv("Weather Data.csv")
print(weather)

# Before analysing the data, explore the given data

print(weather.head())
print(weather.index)
print(weather.columns)
print(weather.shape)  # total rows and columns
print(weather.info)
print(weather.describe())
print(weather.dtypes)  # data types of each col
print(weather.isnull().sum())
print(weather['Weather'].unique())
print(weather.nunique())
print(weather.count())  # total non-null values in each column
print(weather['Weather'].value_counts())

# Q1. Find all the unique wind speed values in the data?

print(weather['Wind Speed_km/h'].nunique())
print(weather['Wind Speed_km/h'].unique())

# Q2. Find the number of time when the weather is exactly clear?

print(weather[weather['Weather'] == 'Clear'])  # Filtering
# OR
print(weather['Weather'].value_counts())       # Value counts
# OR
print(weather.groupby('Weather').get_group('Clear'))  # Group by

# Q3. Find the number of time when the wind speed was exactly 4 km/hr?

print(weather.groupby('Wind Speed_km/h').get_group(4))
print(weather['Wind Speed_km/h'].value_counts())
print(weather[weather['Wind Speed_km/h'] == 4])

# Q4. Find the null values in the data?

print(weather.isnull().sum())
print(weather.notnull().sum())

# Q5. Rename the column weather to 'weather condition'?

weather.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)
print(weather.columns)

# Q6. What is the mean visibility?

print(weather['Visibility_km'].mean())

# Q7. What is the standard deviation of 'Pressure' in the data?

print(weather['Press_kPa'].std())

# Q8. What is the variance of relative humidity in this data?

print(weather['Rel Hum_%'].var())

# Q9. Find all instances when 'Snow' was recorded?

# contains both full and partial match
print(weather[weather['Weather Condition'].str.contains('Snow')])

# Q10. Find all instances when wind speed is above 24 and visibility is 25?

print(weather[(weather['Wind Speed_km/h'] > 24) & (weather['Visibility_km'] == 25)])

# Q11. What is the mean value of each column against each weather condition?

print(weather.groupby('Weather Condition').mean())

# Q12. What is the min and max value of each column against each weather condition?

print(weather.groupby('Weather Condition').min())
print(weather.groupby('Weather Condition').max())


# Q12. Show all records where weather condition is fog?

print(weather[weather['Weather Condition'] == 'Fog'])
# Import required modules.
import test_periods
import weather_html

# Dictionary of cities for forecast.

cities = {
    'Seattle, Washington' : 'https://api.weather.gov/gridpoints/SEW/124,67/forecast',
    'Rexburg, Idaho' : 'https://api.weather.gov/gridpoints/PIH/125,88/forecast',
    'Denver, Colorado' : 'https://api.weather.gov/gridpoints/BOU/62,61/forecast',
    'New York, New York' : 'https://api.weather.gov/gridpoints/OKX/32,34/forecast',
    'Las Vegas, Nevada' : 'https://api.weather.gov/gridpoints/VEF/120,95/forecast'
}

print('[1] Seattle, Washington\n[2] Rexburg, Idaho\n[3] Denver, Colorado\n[4] New York, New York\n[5] Las Vegas, Nevada')
city_choice = int(input('Enter 1 - 5: '))
print(city_choice)
print(f'Forecast document written to {city_choice}.html') 
'''
# Define test periods to be used.

periods = test_periods.periods_that_start_with_a_day
#periods = test_periods.periods_that_start_with_a_night


# Create a document that will show the period name, temperature, wind speed, and detailed forecast for city.

document = weather_html.create_document("forecast.html", "Rexburg, Idaho",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Define loop parameters.

i = 0
if periods == test_periods.periods_that_start_with_a_day:

    # Create new row.

    for i in range(5):
        weather_html.start_new_row(document)

        # Add the first period to the row.
        
        weather_html.add_period(document, periods[i + i])

        # Add the second period to the row.

        weather_html.add_period(document, periods[i + i + 1])

else:

    # Create new row.

    for _ in range(1):
        weather_html.start_new_row(document)

        # Add the first period to the row.

        weather_html.add_period(document, {})

        # Add the second period to the row.

        weather_html.add_period(document, periods[0])

        for _ in range(5):
            weather_html.start_new_row(document)
            i += 1
            

            # Add the first period to the row.

            weather_html.add_period(document, periods[i])
            i += 1

            # Add the second period to the row.

            weather_html.add_period(document, periods[i])

# Complete the document and write it to the file.

weather_html.write_document(document)'''
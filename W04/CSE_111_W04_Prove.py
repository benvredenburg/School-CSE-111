# Import required modules.

import weather_html
import requests

# Dictionary of cities for forecast.

cities = {
    'Seattle, Washington' : 'https://api.weather.gov/gridpoints/SEW/124,67/forecast',
    'Rexburg, Idaho' : 'https://api.weather.gov/gridpoints/PIH/125,88/forecast',
    'Denver, Colorado' : 'https://api.weather.gov/gridpoints/BOU/62,61/forecast',
    'New York, New York' : 'https://api.weather.gov/gridpoints/OKX/32,34/forecast', # New York is no longer working - API Link no longer correct for some reason. I am unconcerned.
    'Las Vegas, Nevada' : 'https://api.weather.gov/gridpoints/VEF/120,95/forecast'
}

# Prompt user for choice of city by using options 1 - 5.

print('[1] Seattle, Washington\n[2] Rexburg, Idaho\n[3] Denver, Colorado\n[4] New York, New York\n[5] Las Vegas, Nevada')

city_choice = int(input('Enter 1 - 5: '))

# Assign city data to variables based on user input.

if city_choice == 1:
    city_name = 'Seattle'
    city_state = 'Washington'
    url = 'https://api.weather.gov/gridpoints/SEW/124,67/forecast'

### Start copy/paste ###
# Display city name and state choice to user.

    print()
    print('Seattle, Washington')
    print('Forecast document written to SeattleWashington.html')

# Make request to chosen url
    
    response = requests.get(url)

# Begin writing document.

    document = weather_html.create_document("SeattleWashington.html", "Seattle, Washington",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Check status of request.

    if response.status_code == 200:

# Convert data from json to dictionary.

        forecast_dict = response.json()

# Create new dictionary with only required information.

        for key, value in forecast_dict.items():
            values_dict = value

# Define periods.

        period = values_dict['periods']

# Redefine response for for correct city.

        response = requests.get(url)

# Create new row.

        for i in range(0, 5):
            weather_html.start_new_row(document)

# Add the first period to the row.
        
            weather_html.add_period(document, period[i + i])

# Add the second period to the row.

            weather_html.add_period(document, period[i + i + 1])

# Finalize and write document to file.

    weather_html.write_document(document)

# End Copy/Paste

elif city_choice == 2:
    city_name = 'Rexburg'
    city_state = 'Idaho'
    url = 'https://api.weather.gov/gridpoints/PIH/125,88/forecast'

# Display city name and state choice to user.

    print()
    print('Rexburg, Idaho')
    print('Forecast document written to RexburgIdaho.html')

# Make request to chosen url
    
    response = requests.get(url)

# Begin writing document.

    document = weather_html.create_document("RexburgIdaho.html", "Rexburg, Idaho",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Check status of request.

    if response.status_code == 200:

# Convert data from json to dictionary.

        forecast_dict = response.json()

# Create new dictionary with only required information.

        for key, value in forecast_dict.items():
            values_dict = value

# Define periods.

        period = values_dict['periods']

# Redefine response for for correct city.

        response = requests.get(url)

# Create new row.

        for i in range(0, 5):
            weather_html.start_new_row(document)

# Add the first period to the row.
        
            weather_html.add_period(document, period[i + i])

# Add the second period to the row.

            weather_html.add_period(document, period[i + i + 1])

# Finalize and write document to file.

    weather_html.write_document(document)

elif city_choice == 3:
    city_name = 'Denver'
    city_state = 'Colorado'
    url = 'https://api.weather.gov/gridpoints/BOU/62,61/forecast'

    # Display city name and state choice to user.

    print()
    print('Denver, Colorado')
    print('Forecast document written to DenverColorado.html')

# Make request to chosen url
    
    response = requests.get(url)

# Begin writing document.

    document = weather_html.create_document("DenverColorado.html", "Denver, Colorado",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Check status of request.

    if response.status_code == 200:

# Convert data from json to dictionary.

        forecast_dict = response.json()

# Create new dictionary with only required information.

        for key, value in forecast_dict.items():
            values_dict = value

# Define periods.

        period = values_dict['periods']

# Redefine response for for correct city.

        response = requests.get(url)

# Create new row.

        for i in range(0, 5):
            weather_html.start_new_row(document)

# Add the first period to the row.
        
            weather_html.add_period(document, period[i + i])

# Add the second period to the row.

            weather_html.add_period(document, period[i + i + 1])

# Finalize and write document to file.

    weather_html.write_document(document)
    
elif city_choice == 4:
    city_name = 'New York'
    city_state = 'New York'
    url = 'https://api.weather.gov/gridpoints/OKX/32,34/forecast'

# Display city name and state choice to user.

    print()
    print('New York, New York')
    print('Forecast document written to NewYorkNewYork.html')

# Make request to chosen url
    
    response = requests.get(url)

# Begin writing document.

    document = weather_html.create_document("NewYorkNewYork.html", "New York, New York",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Check status of request.

    if response.status_code == 200:

# Convert data from json to dictionary.

        forecast_dict = response.json()

# Create new dictionary with only required information.

        for key, value in forecast_dict.items():
            values_dict = value

# Define periods.

        period = values_dict['periods']

# Redefine response for for correct city.

        response = requests.get(url)

# Create new row.

        for i in range(0, 5):
            weather_html.start_new_row(document)

# Add the first period to the row.
        
            weather_html.add_period(document, period[i + i])

# Add the second period to the row.

            weather_html.add_period(document, period[i + i + 1])

# Finalize and write document to file.

    weather_html.write_document(document)

elif city_choice == 5:
    city_name = 'Las Vegas'
    city_state = 'Nevada'
    url = 'https://api.weather.gov/gridpoints/VEF/120,95/forecast'

        # Display city name and state choice to user.

    print()
    print('Las Vegas, Nevada')
    print('Forecast document written to LasVegasNevada.html')

# Make request to chosen url
    
    response = requests.get(url)

# Begin writing document.

    document = weather_html.create_document("LasVegasNevada.html", "Las Vegas, Nevada",
    [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE,weather_html.WIND, weather_html.DETAILED_FORECAST])

# Check status of request.

    if response.status_code == 200:

# Convert data from json to dictionary.

        forecast_dict = response.json()

# Create new dictionary with only required information.

        for key, value in forecast_dict.items():
            values_dict = value

# Define periods.

        period = values_dict['periods']

# Redefine response for for correct city.

        response = requests.get(url)

# Create new row.

        for i in range(0, 5):
            weather_html.start_new_row(document)

# Add the first period to the row.
        
            weather_html.add_period(document, period[i + i])

# Add the second period to the row.

            weather_html.add_period(document, period[i + i + 1])

# Finalize and write document to file.

    weather_html.write_document(document)
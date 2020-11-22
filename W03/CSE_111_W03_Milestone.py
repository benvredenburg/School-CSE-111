# Import required modules.

import test_periods
import weather_html

# Name of city for forcast.

city_name = "Rexburg, Idaho"

# Define test periods to be used.

periods = test_periods.periods_that_start_with_a_day
#periods = test_periods.periods_that_start_with_a_night


# Create a document that will show the period name, temperature, wind speed, and detailed forecast for city.

document = weather_html.create_document("W03/forecast.html", "Rexburg, Idaho",
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

weather_html.write_document(document)

'''
# Start a new row in the document.
weather_html.start_new_row(document)

# Add a period from the forecast to the current row.
weather_html.add_period(document, periods[0])

# Add a second period from the forecast to the current row.
weather_html.add_period(document, periods[1])

# Finish the document and write it to the HTML file.
weather_html.write_document(document) 
'''
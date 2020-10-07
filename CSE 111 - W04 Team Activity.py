import requests

# URL that the requests module is going to check.

url = 'https://swapi.dev/api/planets'

# Request information from URL.

reply = requests.get(url)

# Check request status.

if reply.status_code == 200:

    # Successful request, transfer data to dictionary.

    data = reply.json()

    # Count number of planets in dictionary.

    count = int(data['count'])

    # Retrieve population of each planet and it to galaxy total.

    population = 0

    # Count planets with surface water.

    water = 0

    # Retrieve data about each planet.

    for i in range(1, count+1): 

        # Create URL to store data for each planet.

        url = f'https://swapi.dev/api/planets/{i}'

        # Retrieve data for a planet.

        reply = requests.get(url)

        if reply.status_code == 200:
            planet = reply.json()

            text_pop = planet['population']
            text_water = planet['surface_water']
            print(planet['name'], 'pop:', text_pop, 'water:', text_water)

            # Check populations for real numbers.

            if text_pop.isnumeric():
                pop = int(text_pop)
                population += pop

            if text_water.isnumeric():
                percent = int(text_water)
                if percent > 0:
                    water += 1
        else:

            # Request failed, print status code.

            print('Request failed with status code:', reply.status_code)

    # Print total population of galaxy and number of planets with surface water.

    print(f'Population {population}, Water {water}')
    print()

else:

    # Original request failed, print status code.

    print('Request failed with status code:', reply.status_code)
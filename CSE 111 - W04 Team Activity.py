import requests

# URL that the requests module is going to check.

url = 'https://swapi.dev/api/planets/'

# Request information from URL.

response = requests.get(url)

# Check request status.

if response.status_code == 200:

    # Successful request, transfer data to dictionary.

    data = response.json()

    # Count number of planets in dictionary.

    count = int(data['count'])

    # Retrieve population of each planet and it to galaxy total.

    population = 0


    # Retrieve data about each planet.

    for i in range(1, count+1): 

        # Create URL to store data for each planet.

        url = f'https://swapi.dev/api/planets/{i}'

        # Retrieve data for a planet.

        response = requests.get(url)

        if response.status_code == 200:
            planet = response.json()

            text_pop = planet['population']
            print(planet['name'], ':', text_pop)

            # Check populations for real numbers.

            if text_pop.isnumeric():
                pop = int(text_pop)
                population += pop

        else:

            # Request failed, print status code.

            print('Request failed with status code:', response.status_code)

    # Print total population of galaxy and number of planets with surface water.

    print(f'Population {population}')
    print()

else:

    # Original request failed, print status code.

    print('Request failed with status code:', response.status_code)
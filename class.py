import requests

url = 'https://swapi.dev/api/planets/'

response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()

    planets = data['count']

    print(planets)

    pop = 0

    for i in range(1, planets + 1):
        url = f'https://swapi.dev/api/planets/{i}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)


else:
     # The request failed, print status code.
     print('Request failed with status code:', response.status_code)
import requests

mylist = ['Hulk', 'Captain America', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/search/"

def comparing_superheroes_by_intelligence(heroes_list, url_):
    url_list = []
    heroes_dict = {}

    for i in heroes_list:
        url_list.append(url_ + i)
    for x in url_list:
        response = requests.get(x)
        names = response.json()['results'][0]['name']
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        heroes_dict[names] = intelligence
    return f'Самым умным супергероем оказался - {max(heroes_dict)}'


print(comparing_superheroes_by_intelligence(mylist, url))
import requests
import time

# Задача №1
def get_smart_heroes(list_heroes):
    base_url = "https://akabab.github.io/superhero-api/api/"
    uri = "all.json"
    heroes = {}
    response = requests.get(base_url + uri)
    for hero in response.json():
        if hero['name'] in list_heroes:
            heroes[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes, key=heroes.get))


get_smart_heroes(['Hulk', 'Captain America', 'Thanos'])


# Задача №3
# def get_questions():
#     base_host = "https://api.stackexchange.com/"
#     req_uri = "questions/"
#     our_time = int(time.time()) - 48 * 3600
#     params = {
#         "pagesize": 100,
#         "tagged": "Python",
#         "fromdate": our_time,
#         "site": "stackoverflow"
#     }
#     response = requests.get(base_host + req_uri, params=params)
#     for question in response.json()["items"]:
#         print(question['title'])
#
#
# get_questions()

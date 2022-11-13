import requests
import time

# Задача №1



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

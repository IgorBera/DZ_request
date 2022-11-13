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


# Задача №2
class YaUploader:
    base_host = "https://cloud-api.yandex.net/"

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """задаем хедеры необходимые для запуска работы на полигоне"""
        return {
            "Content-Type": "application/json", # предпочтительный тип контента
            "Authorization": f"OAuth {self.token}" # ключ авторизации
        }

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        uri = "v1/disk/resources/upload/"
        request_url = self.base_host + uri
        params = {"path": file_path, "overwrite": True}  # подаем путь, перезапись тру
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        upload_url = response.json()["href"]
        response = requests.put(upload_url, data=open(file_path, "rb"), headers=self.get_headers())
        if response.status_code == 201:
            print("Загрузка произошла успешно!")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "Text.txt"
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


# Задача №3
def get_questions():
    base_host = "https://api.stackexchange.com/"
    req_uri = "questions/"
    our_time = int(time.time()) - 48 * 3600
    params = {
        "pagesize": 100,
        "tagged": "Python",
        "fromdate": our_time,
        "site": "stackoverflow"
    }
    response = requests.get(base_host + req_uri, params=params)
    for question in response.json()["items"]:
        print(question['title'])


get_questions()

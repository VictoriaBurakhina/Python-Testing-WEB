
# Задание


# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».

# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, contenе
#



import requests
import yaml
import pytest

with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
website = 'https://test-stand.gb.ru/api/posts'
username = 'GB20230583da02'
password = 'b262d327c0'


def token_auth(token):
    res = requests.get(url=my_dict["url1"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var

def test_step1(login):
    assert '' in token_auth(login)

def test_step2(myPost):
    assert 'Жара' in myPost

    print(token_auth(my_dict['token']))

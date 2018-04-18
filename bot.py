import requests
import config
import random


def register_user(username, password, email=None):
    r = requests.post('http://localhost:8000/tcase/api/v1/users/',
                      data={'username': username,
                            'password': password,
                            'email': email
                            })
    r.close()
    return r.ok


def get_token(username, password):
    r = requests.post('http://localhost:8000/tcase/api/v1/token/obtain/',
                      data={'username': username,
                            'password': password
                            })
    r.close()
    return r.json().get('token')


def create_post(text, token):
    r = requests.post('http://localhost:8000/tcase/api/v1/posts/',
                      headers={'Authorization': 'JWT ' + token},
                      data={'text': text})
    r.close()
    return r.ok


def many_posts(username, password, max_count):
    token = get_token(username, password)
    n = 0
    for n in range(random.randint(2, max_count)):
        create_post('text'+username+'number'+str(n), token)
    return n


def many_users(count):
    for n in range(count):
        username = 'user'+str(n)
        password = 'pass'+str(n)
        register_user(username, password)
        count = many_posts(username, password, config.max_posts_per_user)
        print(username+' create '+str(count)+' posts')

print(config.number_of_users)
many_users(config.number_of_users)


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


def like(post, token):
    lod = random.randint(0, 1)
    r = requests.post('http://localhost:8000/tcase/api/v1/likes/',
                      headers={'Authorization': 'JWT ' + token},
                      data={'post': post,
                            'like': lod}
    )
    r.close()
    return r.ok, lod


def list_posts_id():
    rez = []
    for i in requests.get('http://localhost:8000/tcase/api/v1/posts/').json():
        rez.append(i.get('pk'))
    return rez


def many_likes(username, password):
    token = get_token(username, password)
    clike = 0
    cdlike = 0
    mylist = random.sample(list_posts_id(), random.randint(2, config.max_likes_per_user))
    for n in mylist:
        ok, lod = like(n, token)
        if lod:
            clike += 1
        else:
            cdlike += 1
    return clike, cdlike


def many_likes_users(count):
    for n in range(count):
        username = 'user'+str(n)
        password = 'pass'+str(n)
        clike, cdlike = many_likes(username, password)
        print(username+' like '+str(clike)+' posts and dislike ' + str(cdlike))


# print(config.number_of_users)
many_users(config.number_of_users)
many_likes_users(config.number_of_users)

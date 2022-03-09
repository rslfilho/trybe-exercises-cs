import requests


url = 'https://api.github.com/users'


def fetch_users(url):
    try:
        response = requests.get(url)
        users = response.json()
    except requests.HTTPError:
        return ''
    else:
        return users


def print_user_url(users):
    if users:
        for user in users:
            # print(user['login'] + ' ' + user['html_url'])
            print(f"{user['login']} {user['html_url']}")
    else:
        print('No users')


print_user_url(fetch_users(url))

import vk
import getpass


APP_ID = 6160966


def get_user_login():
    login = input('Enter login: ')
    return login


def get_user_password():
    password = getpass.getpass('Enter password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_online_id)
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends online: ')
    for friends in friends_online:
        print(friends['first_name'], friends['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        _friends_online = get_online_friends(login, password)
        output_friends_to_console(_friends_online)
    except:
        print("Wrong login or password")

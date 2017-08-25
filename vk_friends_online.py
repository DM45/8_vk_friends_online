import vk
import json
import getpass


APP_ID = 6160966


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends_online = [
        friends for friends in api.friends.get(fields='online') 
        if friends.get("online") == 1
    ]
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends online: ')
    for friends in friends_online:
        print(friends.get("last_name"), friends.get("first_name"))


if __name__ == '__main__':
    login = input('Enter login: ')
    password = getpass.getpass('Enter password:')
    try:
        _friends_online = get_online_friends(login, password)
        output_friends_to_console(_friends_online)
    except vk.exceptions.VkAuthError:
        print("Wrong login or password")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import random
import time

from InstagramAPI import InstagramAPI

api = InstagramAPI("shapran.irina", "585925")
usersToUnfollow = []


def get_all_unfollowed_users():
    my_followers = api.getTotalSelfFollowers()
    i_follow = api.getTotalFollowings(api.username_id)
    for following in i_follow:
        flag = True
        for follower in my_followers:
            if follower['username'] == following['username']:
                flag = False
                break
        if flag:
            usersToUnfollow.append(following)
    print("Number of non-following users: " + str(len(usersToUnfollow)))


def smart_sleep():
    time.sleep(random.randint(2, 10))


def unfollow_users(max_users=118):
    i = 1
    for user in usersToUnfollow[:max_users]:
        print(str(i) + " of " + str(max_users))
        api.unfollow(user['pk'])
        smart_sleep()
        i += 1


def login():
    if api.login():
        get_all_unfollowed_users()
        # unfollow_users(280)
    else:
        print("Can't login!")


if __name__ == '__main__':
    login()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

api = InstagramAPI("shapran.irina", "585925")
usersToUnfollow = []


def get_all_unfollowed_users():
    followings = api.getTotalFollowings(api.username_id)
    i = 1
    for following in followings:
        print(str(i) + " of " + str(len(followings)) + " username: " + following['username'])
        is_follow_you = False
        for f in api.getTotalFollowings(following['pk']):
            if f['pk'] == api.username_id:
                is_follow_you = True
                break
        if not is_follow_you:
            usersToUnfollow.append(following)
        i += 1
    print("Number of non-following users: " + str(len(usersToUnfollow)))


def unfollow_users(max_users=100):
    i = 1
    for user in usersToUnfollow[:max_users]:
        print(str(i) + " of " + str(len(usersToUnfollow)) + " username: " + user['username'])
        # api.unfollow(usersToUnfollow[i - 1]['pk'])
        i += 1


def login():
    if api.login():
        get_all_unfollowed_users()
        # unfollowUsers()
    else:
        print("Can't login!")


if __name__ == '__main__':
    login()

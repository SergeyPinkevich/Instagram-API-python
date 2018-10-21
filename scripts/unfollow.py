#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

api = InstagramAPI("89179065733", "Dscjwrbq")
usersToUnfollow = []


def getAllUnfollowedUsers():
    followings = api.getTotalFollowings(api.username_id)
    for following in followings:
        isFollowYou = False
        for f in api.getTotalFollowings(following['pk']):
            if f['pk'] == api.username_id:
                isFollowYou = True
                break
        if not isFollowYou:
            usersToUnfollow.append(following)
    print("Number of non-following users: " + str(len(usersToUnfollow)))


def unfollowUsers(max_users=100):
    i = 1
    for user in usersToUnfollow[:max_users]:
        print(str(i) + " of " + str(len(usersToUnfollow)) + " username: " + user['username'])
        api.unfollow(usersToUnfollow[i - 1]['pk'])
        i += 1


def login():
    if api.login():
        getAllUnfollowedUsers()
        unfollowUsers()
    else:
        print("Can't login!")


if __name__ == '__main__':
    login()

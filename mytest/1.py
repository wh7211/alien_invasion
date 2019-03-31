#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
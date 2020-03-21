#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: GF
@project: gaofeng_pyer
@file: return.py
@time: 2020/3/21 上午11:49
"""
prompt = "\nTell me something , and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""   #设定变量为空值
while message !='quit':   #循环打印询问
    message = input(prompt)
    if message != 'quit': #用户不输入quit,每次打印message. 用户输入quit则退出
        print(message)



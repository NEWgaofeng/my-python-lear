#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: GF
@project: gaofeng_pyer
@file: return.py
@time: 2020/3/21 上午11:49
"""
alien_0 = {'x_postition': 0,'y_position': 25, 'speed': 'medium'}
print("Original x_position " + str(alien_0['x_postition']))

# 向右移动外星人
# 根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

alien_0['x_position'] = alien_0['x_postition'] + x_increment
print("New x_position: " +  str(alien_0['x_postition']))

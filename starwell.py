#!/usr/bin/env python 
#-*-coding: utf-8-*-
#version = 0.1
#author =shanbin
"""this script can display  array photo like：
#            #
 ##        ##
  ###    ###
   ########
   ########
  ###    ###
 ##        ##
#            #

"""
#set blank and '#' location
up_icon = 1
up_blank = 12
down_icon = 4
down_blank = 0

for i in range(4):
	print " "*i+"#"*up_icon+" "*up_blank+"#"*up_icon 
	up_icon +=1
	up_blank-=4
for i in  range(3,-1,-1):
	print " "*i+"#"*down_icon+" "*down_blank+"#"*down_icon 
	down_icon -= 1
	down_blank+= 4

if __name__ == '__main__':
	pass
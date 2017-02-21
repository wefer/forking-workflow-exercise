#!/usr/bin/env python
# encoding: utf-8 

def improved_tweet(message):
   if len(message) < 140:
      return message
   else:
      raise Exception

def tweet():
   return improved_tweet('We have made some conflicts!')

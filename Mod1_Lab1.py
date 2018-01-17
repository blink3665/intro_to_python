

#!/usr/bin/env python

'''
This will be the welcome questionaire for the Masters

There is an assumption that the user has played golf and has a handicap

Requires Python 3.6
'''

full_name=input("What is your full name?")
#Handicap is a measure of a golfer's scoring capabilities
handicap=input("What is your golf handicap?")
state=input("What state do you live in? (2 character state code)")

print(full_name.title(),"Welcome to Augusta National!  \
We are glad that you have traveled all the way from",state.upper(), \
"state!  Your handicap of",handicap,"more than qualifies you to play in the Masters!")



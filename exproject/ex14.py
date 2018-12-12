#!/usr/bin/env python
from sys import argv
script , user_name = argv
prompt = '> '

print(f"Hi {user_name} i'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you like {user_name}?")
lives = input(prompt)

print("What kind of computer dou you have?")
computer = input (prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.  Nice.
""")

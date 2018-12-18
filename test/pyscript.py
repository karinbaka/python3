from sys import argv
'''
print(argv[0])
print(argv[1])


script , user_name = argv
prompt = '> '

print(f"Hi {user_name} i'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

script, filename = argv
txt = open(filename)
print(txt.read())
'''
txt = open('./pymysql的方法', mode='r', encoding='utf8')
print(txt.read())
txt.close()
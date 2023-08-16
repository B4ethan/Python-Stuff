# This file is for my tests
#Just stuff I want to check before I add it to the bot and the original file

import json

with open('/workspaces/Python-Stuff/discord/leng/lengs.txt') as f:
    x = f.read()

data = json.loads(x)

print(data)
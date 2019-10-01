# Python-in-Python
Snake Game

Result of refactring of the following initial source code: https://pastebin.com/embed_js/jB6k06hG
from the following tutorial: https://www.youtube.com/watch?v=CD4qAhfFuLo

Control commands are sent via mosquitto server at test.mosquitto.org. To see the commands: 
mosquitto_sub -h "test.mosquitto.org" -i testSub -t commands

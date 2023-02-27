import json
import sys
from common.log import logger

content = "你好测试 hello"
print(content.split(' ', 1))

print(content.split('\u2005', 1))
print('\u2005'.encode().decode())


# from bot.bot_factory import create_bot
# print(create_bot("IDEA").reply("十大流行歌曲"))


# with open("./test.json", 'w') as f:
#     dictdata = {"question":"测试"}
#     json.dump(dictdata, f)


logger.info("info test")
logger.error("error test")
logger.debug("debug test")
print(sys.stdout.encoding)
print('\U0001f409')
logger.info('\U0001f409')
print('\U0001f409'.decode())


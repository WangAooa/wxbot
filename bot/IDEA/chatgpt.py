import requests
import json
from bot.bot import Bot
from common.log import logger

class IDEAbot(Bot):
    def reply(self, query, context=None):
        logger.debug("[IDEA] query={}".format(query))

        url = "https://test.fengshenbang-lm.com/chatgpt/submitQuestion"
        headers = {'content-type': 'application/json'}
        data = {"question":query}

        respond = requests.post(url, json.dumps(data), headers=headers)

        if respond.status_code == 200:
            logger.debug("respond : {}".format(respond.json()['data']['answers'][0]))
            return respond.json()['data']['answers'][0]
        else :
            logger.error("no respond")

            return "问题没有回复 "+ query
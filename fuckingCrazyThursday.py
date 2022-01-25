import random
import json
import os
import requests

from hoshino import Service
from hoshino.typing import MessageSegment, CQEvent

sv = Service('疯狂星期四')


@sv.on_fullmatch(('来点疯狂星期四文案', "疯狂星期四"))
async def random_post(bot, ev: CQEvent):
    # 获取json数据
    r = requests.get('https://raw.githubusercontent.com/Nicr0n/fucking_crazy_thursday/master/post.json')
    # 将json对象加载到数组
    kfc = json.loads(r.content.decode()).get('post')
    # 随机选取数组中的一个对象
    randomPost = random.choice(kfc)
    await bot.send(ev,randomPost)
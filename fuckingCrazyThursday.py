import random
import json
import os

from hoshino import Service
from hoshino.typing import MessageSegment, CQEvent

sv = Service('疯狂星期四')


@sv.on_fullmatch(('来点疯狂星期四文案', "疯狂星期四"))
async def random_post(bot, ev: CQEvent):
    # json数据存放路径
    filePath = os.path.join(os.path.dirname(__file__), 'post.json')
    # 将json对象加载到数组
    kfc = json.load(open(filePath, 'r', encoding="UTF-8")).get('post')
    # 随机选取数组中的一个对象
    randomPost = random.choice(kfc)
    await bot.send(ev,randomPost)
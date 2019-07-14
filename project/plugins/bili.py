from nonebot import on_command, CommandSession
from pyquery import PyQuery as pq
import requests,json
import time;

@on_command('新番', aliases=('新番时间表'))
async def _(session: CommandSession):
    q_type = session.get('type', prompt='国创or番剧？')
    result_str = ''
    q_type_int = 0 if q_type.find("国创") > -1 else 1
    time_line = await get_time_line(q_type_int)
    for t in time_line:
        result_str = result_str + t['title'] + t['index'] + '\n' \
        + t['time'] +  '更新\n' + t['link'] + '\n'

    # 向用户发送天气预报
    await session.send(result_str)

async def get_time_line(a_type):
    count = 1
    type_str = "cn" if a_type == 0 else "global"
    res = requests.get('https://bangumi.bilibili.com/web_api/timeline_'+type_str)
    article_dict = json.loads(res.text)
    # get date
    month = time.localtime()[1]
    day = time.localtime()[2]
    day_of_week = time.localtime()[6]
    time_lines = article_dict['result']
    today_line = []
    result_line = []
    for line in time_lines:
        if line['is_today'] == 1:
            today_line = line['seasons']
    if len(today_line) > 0:
        result_line = [{
        'title': s['title'],
        'link':'https://www.bilibili.com/bangumi/play/ss' + str(s['season_id']),
        'time': s['pub_time'],
        'index':s['pub_index']
        } for s in today_line]
    
    return result_line
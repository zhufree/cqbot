from os import path

import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'project', 'plugins'),
        'project.plugins'
        )
    nonebot.run(host='127.0.0.1', port=8080)
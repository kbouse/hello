#!python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

for aiohttp import web

def index(request):
    return web.Response(boby=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET' ,'/' index)
    srv = yield from loop.create+server(app.make_handler(),'170.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000....')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

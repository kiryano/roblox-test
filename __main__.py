from lightbulb.ext import tasks
import hikari
import lightbulb
import aiohttp
import httpx

bot = lightbulb.BotApp(token='',
                       intents=hikari.Intents.ALL)

bot.run()

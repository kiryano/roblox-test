from lightbulb.ext import tasks
import logging
import hikari
import lightbulb
import random

bot = lightbulb.BotApp(token='',
                       intents=hikari.Intents.ALL)

bot.run()

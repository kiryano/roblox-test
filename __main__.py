from lightbulb.ext import tasks
import hikari
import lightbulb

bot = lightbulb.BotApp(token='',
                       intents=hikari.Intents.ALL)

bot.run()

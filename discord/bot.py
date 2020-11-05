from cogs.utils import Utils
from cogs.music import Music
from cogs.rule_based import Rules

from discord.ext import commands

# discord api TOKEN
TOKEN = "Njc0OTU1MzA5OTczNzY2MTQ0.XjwHHQ.AvpNZzxWbL7ev3N0_4TxRdd4WNI"

class MyBot(commands.Bot):
    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(bot.user))
        print('------')
    
bot = MyBot(command_prefix=commands.when_mentioned_or("!"),
                   description='Python Music Bot');

bot.add_cog(Music(bot))
bot.add_cog(Utils(bot))
bot.add_cog(Rules(bot))

bot.run(TOKEN)
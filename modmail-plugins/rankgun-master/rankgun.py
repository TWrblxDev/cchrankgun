import requests
 
BaseUrl = "https://api.rankgun.works"

from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        
     Response = requests.get(f"{BaseUrl}/status")
     Data =  Response.json()
     

    @commands.command()
    async def rankstatus(self, ctx, *, message):
        await ctx.send(data)

async def setup(bot):
    await bot.add_cog(Hello(bot))

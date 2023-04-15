import requests
import time

 
ranklogin = "RJciwnzdm8TOvs6dw04YA1phhLBbyR"

from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
        
    
    @commands.command()
    async def rankshout(self, ctx, *, message:str):
        await ctx.send("Message To set a shout.")
        time.sleep(5)
        await ctx.send(f='{message}')
        

    @commands.command()
    async def rankstatus(self, ctx ):
        BaseUrl = "https://api.rankgun.works"
        Response = requests.get(f"{BaseUrl}/status")
        Data =  Response.json()
        await ctx.send(Data)
        print(Data)

async def setup(bot):
    await bot.add_cog(Hello(bot))

import requests
 


from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        
    
     

    @commands.command()
    async def rankstatus(self, ctx ):
        BaseUrl = "https://api.rankgun.works"
        Response = requests.get(f"{BaseUrl}/status")
        Data =  Response.json()
        await ctx.send(Data)
        print(Data)

async def setup(bot):
    await bot.add_cog(Hello(bot))

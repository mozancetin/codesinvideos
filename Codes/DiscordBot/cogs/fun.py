import discord
from discord.ext import commands, tasks
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.kurallar.start()

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def selamla(self, ctx):
        await ctx.send(f"{ctx.author.mention} selam veriyor")

    @tasks.loop(minutes=1)
    async def kurallar(self):
        channel = await self.bot.fetch_channel(CHANNEL_ID)

        kurallarListesi = [
            "Taşkınlık çıkartmayın",
            "Herkese iyi davranın",
            "Spam yapmayın"
        ]

        await channel.send(random.choice(kurallarListesi))

    @kurallar.before_loop
    async def before_kurallar(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def loopiptal(self, ctx):
        self.kurallar.cancel()
        await ctx.send("Loop iptal edildi")

    @commands.command()
    async def loopbaşlat(self, ctx):
        self.kurallar.start()
        await ctx.send("Loop başlatıldı")
    

def setup(bot):
    bot.add_cog(Fun(bot))

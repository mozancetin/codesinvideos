import discord
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            # error.retry_after -> kaç saniye sonra tekrar denememiz gerektiği
            if error.retry_after >= 3600: # 3600 saniye -> 1 saat
                await ctx.send(f"Bu komut bekleme süresine sahiptir. Yaklaşık {round(error.retry_after / 3600)} saat sonra tekrar deneyin.")
            elif 60 <= error.retry_after < 3600:
                await ctx.send(f"Bu komut bekleme süresine sahiptir. Yaklaşık {round(error.retry_after / 60)} dakika sonra tekrar deneyin.")
            elif error.retry_after < 60:
                await ctx.send(f"Bu komut bekleme süresine sahiptir. Yaklaşık {round(error.retry_after)} saniye sonra tekrar deneyin.")

        else:
            print(error)

def setup(bot):
    bot.add_cog(Errors(bot))
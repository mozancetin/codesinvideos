import discord
from discord.ext import commands

class Moderasyon(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} sunucudan atıldı.")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} sunucuda banlandı.")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.name} adlı kullanıcının banı kaldırıldı.")
                return True

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int = 10):
        await ctx.send("Mesaj siliniyor") 
        await ctx.channel.purge(limit = amount + 2) # limit = 10 --> 9 tane sil


def setup(bot):
    bot.add_cog(Moderasyon(bot))
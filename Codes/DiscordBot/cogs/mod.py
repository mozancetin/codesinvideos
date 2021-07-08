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
        embed = discord.Embed(color = discord.Colour.red(), title = f"Mesajlar siliniyor lütfen bekle {ctx.author.display_name}")
        await ctx.send(embed=embed) 
        await ctx.channel.purge(limit = amount + 2) # limit = 10 --> 9 tane sil

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx, user : discord.User, *, message = None):
        user_id = user.id
        if user_id != None and message != None:
            try:
                target = await self.bot.fetch_user(user_id)
                await target.send(message)

                await ctx.author.send("Mesaj şu kullanıcıya gönderildi: " + target.name)
            except Exception:
                await ctx.author.send("Mesaj gönderilemedi")
        else:
            await ctx.send("Kişi ve mesaj belirtmek zorundasınız!")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def dmall(self, ctx, *, message = None):
        if message != None:
            members = ctx.guild.members # [ozybo, ahmet, mehmet]

            for member in members:
                if member == self.bot.user or member.bot or member == ctx.author:
                    continue

                try:
                    await member.send(message)
                    await ctx.author.send("Mesaj şu kullanıcıya gönderildi: " + member.name)
                except Exception:
                    await ctx.author.send("Mesaj şu kullanıcıya gönderilemedi: " + member.name)

        else:
            await ctx.send("Mesaj girmelisiniz!")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def dmrole(self, ctx, role : discord.Role = None, *, message = None):
        self.exists = False

        if message != None and role != None:
            members = ctx.guild.members

            for member in members:
                if member == self.bot.user or member.bot or member == ctx.author:
                    continue

                if role in member.roles: # [rol1, rol2]
                    try:
                        self.exists = True
                        await member.send(message)
                        await ctx.author.send("Mesaj şu kişiye başarıyla gönderildi: " + member.name)
                    except Exception:
                        await ctx.author.send("Mesaj şu kişiye gönderilemedi: " + member.name)

            if not self.exists: # if not False --> if True
                await ctx.author.send("Sunucuda bu role sahip kimse yok")

        else:
            await ctx.send("Rol ve mesaj belirlemelisiniz!")


def setup(bot):
    bot.add_cog(Moderasyon(bot))

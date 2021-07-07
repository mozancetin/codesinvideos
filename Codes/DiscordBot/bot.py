import discord
from discord.ext import commands
import os
import bottoken

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot hazır: " + bot.user.name)

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)} ms")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}") # extension = economy --> cogs.economy

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
async def reload(ctx, extension): # Sil, tekrar yükle
    if extension == "all":
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                bot.unload_extension(f"cogs.{filename[:-3]}") # filename = deneme.py 
                bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Extension: {filename[:-3]} güncellendi.")
    else:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        print(f"Extension: {extension} güncellendi.")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(bottoken.TOKEN)

import discord
import settings
from functions import *
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix= "!", intents=intents)

#sync with discord, use when changes are made to slash commands
@bot.command(hidden=True)
async def sync(ctx):
    user_id = ctx.author.id
    owner_id = ctx.guild.owner_id
    user_name = ctx.author.name
    if user_id == owner_id:
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)
        await ctx.send(f"{user_name}, I have requested to sync with the hive.", ephemeral=True)
    else:
        await ctx.send(f"Sorry, {user_name}, you don't have permission to use that command.")
        

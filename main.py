import discord
import settings
from discommands import bot


# basic logging & status
@bot.event
async def on_ready():
        print(f"Bot User: {bot.user}")
        print(f"Bot Id: {bot.user.id}")
        print(f"Bot Guild ID:{bot.guilds[0].id}")
        print("____________________")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='/help'))         
## -- ONLY USE WHEN PUSHING NEW SLASH COMMANDS -- 
        # bot.tree.copy_global_to(guild=settings.GUILD_ID)
        # await bot.tree.sync(guild=settings.GUILD_ID)
        print('--This station is bot operational--')


if __name__ == "__main__":
    # Run the bot
    TOKEN = settings.DISCORD_API_SECRET
    bot.run(TOKEN)
    
